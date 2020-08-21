import networkx as nx
import pandas as pd

from face2face.imports.load_all_data import Data


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


def create_network_from_data(Data, replace_attr=False, label=None):
    r"""Allow to create a networkx Graph

        Creating a networkx graph based on the interaction data. Metadata can also be provided to add node attributes.

        Parameters
        ----------
        Data : Data
            Data Object that contains Tij- and Metadata for a dataset.
        replace_attr: bool
            If True, attributes of type string will be replaced by float numbers.
        label: optional, string
            If string label is given, the rows where label column value is NaN will be removed before creating the
            network.

        Returns
        -------
        G : NetworkX Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported dataset.

        Examples
        ---------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>                meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> print(test_network.edges)
        [(0, 1), (1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (6, 7), (10, 11), (10, 12), (11, 12)]
        >>> print(test_network.nodes)
        [0, 1, 2, 3, 4, 6, 7, 10, 11, 12]
        >>> for i in test_network.nodes:
            >>> print(test_network.nodes[i])
        {'Age': 1.0, 'Sex': 1.0}
        {'Age': 0.0, 'Sex': 'NaN'}
        {'Age': 'NaN', 'Sex': 0.0}
        {'Age': 0.0, 'Sex': 1.0}
        {'Age': 'NaN', 'Sex': 0.0}
        {'Age': 1.0, 'Sex': 1.0}
        {'Age': 1.0, 'Sex': 'NaN'}
        {'Age': 2.0, 'Sex': 1.0}
        {'Age': 2.0, 'Sex': 0.0}
        {'Age': 2.0, 'Sex': 1.0}

    """
    if hasattr(Data,"metadata") is False:
        G = nx.Graph()
        individuals = list(set(list(Data.interaction.i) + list(Data.interaction.j)))
        G.add_nodes_from(individuals)
        df_edge = Data.interaction.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
        for col, row in df_edge.iterrows():
            G.add_edge(row["i"], row["j"])

        return G

    else:

        if label is None:
            if replace_attr:
                Data.replace_str_attr_to_float()

            G = nx.Graph()
            G.add_nodes_from(Data.metadata["ID"].values)
            df_edge = Data.interaction.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])

            attribute_list = list(Data.metadata.columns.values)
            attr_dict = {}
            for index, row in Data.metadata.iterrows():
                id_dict = {}
                for i in attribute_list[1:]:
                    id_dict[str(i)] = row[str(i)]
                attr_dict[row[attribute_list[0]]] = id_dict

            nx.set_node_attributes(G, attr_dict)
            return G

        else:
            metadata = Data.metadata
            metadata = metadata.fillna("NaN")
            metadata = metadata.loc[metadata[label] != "NaN"]
            if replace_attr:
                metadata = replace_str_attr_to_float_2(metadata)

            metadata = metadata[["ID", label]]

            df_merge_data_to_filter = Data.interaction.merge(metadata, left_on=["i"], right_on=["ID"], how="inner")
            interaction = df_merge_data_to_filter.merge(metadata, left_on=["j"], right_on=["ID"], how="inner")
            interaction = interaction[["Time", "i", "j"]]

            G = nx.Graph()
            G.add_nodes_from(metadata["ID"].values)
            df_edge = interaction.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])

            attribute_list = list(metadata.columns.values)
            attr_dict = {}
            for index, row in metadata.iterrows():
                id_dict = {}
                for i in attribute_list[1:]:
                    id_dict[str(i)] = row[str(i)]
                attr_dict[row[attribute_list[0]]] = id_dict

            nx.set_node_attributes(G, attr_dict)
            return G


def hopping_time_networks(Data, minutes=1000):
    r"""Create multiple Networkx Graphs and DataFrames

        Creating multiple Networkx Graphs and DataFrames based on the given hopping time interval.

        Parameters
        ----------
        Data: Data
            Data Object that contains Tij- and Metadata for a data set.
        minutes: int
            The interval time in which the Networkx Graphs should be splitted.

        Returns
        -------
        network_list: list
            A list of all networkx Graphs for the given interval.
        df_list: list
             A list of all dataframes for the given interval.

        Examples
        --------
        In this example the full dataframe got splitted in dataframes and networks with time windows of 40 seconds
        (2/3 minutes). The output in this case describes the network and the dataframe for the first 40 seconds in the
        original dataframe.
        
        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta = "\\t",
        >>>                meta_attr_list = attr_list)
        >>> test_network_list, test_df_list = hopping_time_networks(test_df, minutes=2/3)
        >>> print(test_network_list[0].edges)
        [(0, 1), (1, 2), (1, 3), (2, 3)]
        >>> print(test_network_list[0].nodes)
        [0, 1, 2, 3]
        >>> for i in test_network_list[0].nodes:
            >>> print(test_network_list[0].nodes[i])
        {'Age': 1.0, 'Sex': 'F'}
        {'Age': 0.0, 'Sex': nan}
        {'Age': nan, 'Sex': 'M'}
        {'Age': 0.0, 'Sex': 'F'}
        >>> print(test_df_list[0])
           Time  i  j  TimeGroup
        0    20  0  1   0.0-40.0
        1    40  1  2   0.0-40.0
        2    40  1  3   0.0-40.0
        3    40  2  3   0.0-40.0

        See Also
        ---------
        face2face.imports.create_network.create_sliding_time_networks
        face2face.imports.create_network.event_time_networks

        """
    interval_seconds = minutes * 60

    time_stamps = Data.interaction["Time"][0]
    end_time_stamp = Data.interaction["Time"].tail(1).item()

    time_stamp_split_list = []

    id_group = 0
    while time_stamps <= end_time_stamp + interval_seconds:
        time_stamp_split_list.append([time_stamps, str(time_stamps-interval_seconds-Data.interaction["Time"][0]) + "-"
                                      + str(time_stamps-Data.interaction["Time"][0])])
        time_stamps += interval_seconds
        id_group += 1

    marker_timestamp_list = []
    unique_timestamp_list = set(Data.interaction["Time"].values)
    for i in range(1, len(time_stamp_split_list)):
        for j in unique_timestamp_list:
            if time_stamp_split_list[i][0] > j >= time_stamp_split_list[i-1][0]:
                marker_timestamp_list.append([j, time_stamp_split_list[i][0], time_stamp_split_list[i][1]])
    timestamp_marker_df = pd.DataFrame(marker_timestamp_list, columns=["Time", "sortby", "TimeGroup"])
    df_marker = Data.interaction.merge(timestamp_marker_df, how="left", on="Time")
    df_marker["sortby"] = df_marker["sortby"] - Data.interaction["Time"][0]
    df_list = [x for _, x in df_marker.groupby("sortby")]
    df_list = [i.drop(columns="sortby") for i in df_list]

    if hasattr(Data, "metadata") is False:
        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])
            network_list.append(G)

        return network_list, df_list

    else:
        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])

            attribute_list = list(Data.metadata.columns.values)
            attr_dict = {}
            for index, row in Data.metadata.iterrows():
                id_dict = {}
                for i in attribute_list[1:]:
                    id_dict[str(i)] = row[str(i)]
                attr_dict[row[attribute_list[0]]] = id_dict

            nx.set_node_attributes(G, attr_dict)
            network_list.append(G)
        return network_list, df_list


def sliding_time_networks(Data, slide=1, interval=1000):
    r"""Create multiple Networkx Graphs and DataFrames

        Creating multiple Networkx Graphs and DataFrames based on the given interval and the sliding time interval.

        Parameters
        ----------
        Data: Data
            Data Object that contains Tij- and Metadata for a data set.
        slide: int
            The time steps in which the intervals should be created.
        interval: int
            The interval time in which the networkx Graphs should be splitted.

        Returns
        -------
        network_list: list
            A list of all networkx Graphs for a given interval.
        df_list: list
            A list of all dataframes for a given interval.

        Examples
        ---------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta = "\t",
        >>>                meta_attr_list=attr_list)
        >>> test_network_list, test_df_list = sliding_time_networks(test_df, slide=1/3, interval=2/3)
        >>> print(test_df_list[0])
           Time  i  j  TimeGroup
        0    20  0  1     0-40.0
        1    40  1  2     0-40.0
        3    40  1  3     0-40.0
        5    40  2  3     0-40.0
        >>> print(test_network_list[0].nodes)
        [0, 1, 2, 3]
        >>> print(test_network_list[0].edges)
        [(0, 1), (1, 2), (1, 3), (2, 3)]
        >>> print(test_df_list[1])
            Time  i  j  TimeGroup
        2     40  1  2  20.0-60.0
        4     40  1  3  20.0-60.0
        6     40  2  3  20.0-60.0
        7     60  4  6  20.0-60.0
        9     60  4  7  20.0-60.0
        11    60  6  7  20.0-60.0
        >>> print(test_network_list[1].nodes)
        [1, 2, 3, 4, 6, 7]
        >>> print(test_network_list[1].edges)
        [(1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (6, 7)]

        See Also
        ---------
        face2face.imports.create_network.hopping_time_networks
        face2face.imports.create_network.event_time_networks
        """
    interval_seconds = interval * 60
    interval_slide = slide * 60

    time_stamps = Data.interaction["Time"][0]
    end_time_stamp = Data.interaction["Time"].tail(1).item()
    time_stamp_split_list = []

    interval = 0
    interval2 = interval_seconds
    id_group = 0
    while time_stamps <= end_time_stamp + interval_seconds:
        time_stamp_split_list.append([time_stamps, time_stamps + interval_seconds, id_group, str(interval) + "-"
                                      + str(interval2)])
        time_stamps += interval_slide
        interval2 += interval_slide
        interval += interval_slide
        id_group += 1

    marker_timestamp_list = []
    unique_timestamp_list = set(Data.interaction["Time"].values)
    for i in time_stamp_split_list:
        for j in unique_timestamp_list:
            if i[1] > j >= i[0]:
                marker_timestamp_list.append([j, i[2], i[3]])

    timestamp_marker_df = pd.DataFrame(marker_timestamp_list, columns=["Time", "id_group","TimeGroup"])
    df_marker = Data.interaction.merge(timestamp_marker_df, how="left", on="Time")

    df_list = [x for _, x in df_marker.groupby("id_group")]
    df_list = [i.drop(columns="id_group") for i in df_list]

    if hasattr(Data, "metadata") is False:
        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])
            network_list.append(G)

        return network_list, df_list

    else:

        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="EdgeWeight")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])

            attribute_list = list(Data.metadata.columns.values)
            attr_dict = {}
            for index, row in Data.metadata.iterrows():
                id_dict = {}
                for i in attribute_list[1:]:
                    id_dict[str(i)] = row[str(i)]
                attr_dict[row[attribute_list[0]]] = id_dict

            nx.set_node_attributes(G, attr_dict)
            network_list.append(G)
        return network_list, df_list


def event_time_networks(Data, events):
    r"""Create multiple Networkx Graphs and DataFrames

        Creating multiple Networkx Graphs and DataFrames based on a given event list.

        Parameters
        ----------
        Data: Data
            Data Object that contains Tij- and Metadata for a data set.
        events: list
            A list of tuples that contains the eventname and the start and the beginning of the event.

        Returns
        -------
        network_list: list
            A list of all networkx Graphs for a given interval.
        df_list: list
            A list of all dataframes for a given interval.

        Examples
        --------
        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>       path_meta="../../data/Test/meta_test.dat", separator_meta = "\t",
        >>>       meta_attr_list=attr_list)

        >>> event_list = [("Event A", 20, 60), ("Event B", 120, 180), ("Event C", 400, 500)]

        >>> test_network_list, test_df_list = event_time_networks(test_df, events=event_list)
        >>> print(test_df_list[0])
             Time i  j TimeGroup
        1    40  1  2   Event A
        2    40  1  3   Event A
        3    40  2  3   Event A
        4    60  4  6   Event A
        5    60  4  7   Event A
        6    60  6  7   Event A
        >>> print(test_network_list[0].nodes)
        [1, 2, 3, 4, 6, 7]
        >>> print(test_network_list[0].edges)
        [(1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (6, 7)]
        >>> print(test_df_list[1])
             Time i  j TimeGroup
        13   140  7  6   Event B
        14   140  4  6   Event B
        15   140  7  4   Event B
        16   160  7  6   Event B
        17   160  4  6   Event B
        18   160  7  4   Event B
        19   180  7  6   Event B
        20   180  4  6   Event B
        21   180  7  4   Event B
        >>> print(test_network_list[1].nodes)
        [4, 6, 7]
        >>> print(test_network_list[1].edges)
        [(4, 6), (4, 7), (6, 7)]
        >>> print(test_df_list[2])
             Time  i   j   TimeGroup
        25   420   4   6   Event C
        26   420   4   7   Event C
        27   420   6   7   Event C
        28   440   4   6   Event C
        29   440   4   7   Event C
        30   440   6   7   Event C
        31   440   1   2   Event C
        32   440   1   3   Event C
        33   440   2   3   Event C
        34   460   1   2   Event C
        35   460   1   3   Event C
        36   460   2   3   Event C
        37   460  10  11   Event C
        38   460  11  12   Event C
        39   460  10  12   Event C
        40   500  10  11   Event C
        41   500  11  12   Event C
        42   500  10  12   Event C
        >>> print(test_network_list[2].nodes)
        [1, 2, 3, 4, 6, 7, 10, 11, 12]
        >>> print(test_network_list[2].edges)
        [(1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (6, 7), (10, 11), (10, 12), (11, 12)]

        See Also
        --------
        face2face.imports.create_network.hopping_time_networks
        face2face.imports.create_network.sliding_time_networks

        """

    marker_timestamp_df = []
    unique_timestamp_list = set(Data.interaction["Time"].values)
    for i in range(len(events)):
        for j in unique_timestamp_list:
            if events[i][2] >= j > events[i][1]:
                marker_timestamp_df.append([j, events[i][0], i])
    marker_timestamp_df = pd.DataFrame(marker_timestamp_df, columns=["Time","Event","TimeGroup"])
    df_marker = Data.interaction.merge(marker_timestamp_df, how="left", on="Time")

    df_list = [x for _, x in df_marker.groupby("TimeGroup")]
    df_list = [i.drop(columns="TimeGroup") for i in df_list]

    if hasattr(Data, "metadata") is False:
        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="AmountOfContactsIJ")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])
            network_list.append(G)

        return network_list, df_list

    else:
        network_list = []
        for i in df_list:
            G = nx.Graph()
            node_list = list(set(i["i"].append(i["j"])))
            G.add_nodes_from(node_list)
            df_edge = i.groupby(["i", "j"]).size().reset_index(name="EdgeWeight")
            for col, row in df_edge.iterrows():
                G.add_edge(row["i"], row["j"])

            attribute_list = list(Data.metadata.columns.values)
            attr_dict = {}
            for index, row in Data.metadata.iterrows():
                id_dict = {}
                for i in attribute_list[1:]:
                    id_dict[str(i)] = row[str(i)]
                attr_dict[row[attribute_list[0]]] = id_dict

            nx.set_node_attributes(G, attr_dict)
            network_list.append(G)
        return network_list, df_list


def replace_str_attr_to_float_2(metadata):

    r"""Replaces string attributes

        If replaced_attr parameter is set true in the `create_network_from_data` function, string attributes will be
        replaced by float numbers.

        Parameters
        ----------
        metadata : DataFrame
            DataFrame object that contains meta data for the persons that have participated in the experiment.

        Returns
        -------
        metadata : DataFrame
            DataFrame object that contains meta data for the persons that have participated in the experiment. Metadata
            string attribute values are changed into float values.
    """
    parameter_list = []
    for col in metadata.columns:
        if col != "ID":
            parameter_list.append(col)

    parameter_specification_list = []
    for i in parameter_list:
        contacts_of_i = list(set(metadata[i]))
        parameter_specification_list.append(contacts_of_i)

    mapping = {}
    for i in parameter_specification_list:
        for j in range(len(i)):
            if isinstance(i[j], str):
                mapping[i[j]] = float(j)
    metadata = metadata.replace(mapping)
    return metadata
