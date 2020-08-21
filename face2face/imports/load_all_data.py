import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


class Data:

    def __init__(self, data_set_name=None, path_tij=None, separator_tij=None, path_meta=None, separator_meta=None,
                 meta_attr_list=None, header=None, meta_df=None, tij_df=None):

        """Initialize an object that contains Tij- and Metadata for imported or given data sets.

            Creating multiple Networkx Graphs and DataFrames based on a given event list.

            Parameters
            ----------
            data_set_name: optional: str, default: None
                If you want to use predefined data sets you can use this parameter to create a Data object. For example
                you can import the "Synthetic" data set.
            path_tij: optional: str, default: None
                Must be used to import tij data sets manually.
            separator_tij: optional: str, default: None
                Must be used if you import tij data sets manually.
            path_meta: optional: str, default: None
                Must be used to import meta data sets manually.
            separator_meta: optional: str, default: None
                 Must be used if you import meta data sets manually.
            meta_attr_list: optional: list, default: None
                Must be used if you want to import metadata manually that has no header.
            header: optional: str, default: None
                Must be used if tij and/or metadata already contain a header. Possible parameters are 'tij', 'meta' or
                'all'.
            meta_df: optional: dataframe, default: None
                Must be used if you want to create a Data Class Object based on a dataframe
            tij_df: optional: dataframe, default: None
                Must be used if you want to create a Data Class Object based on a dataframe, for example with a
                dataframe of the dataframe list from the create_network functions

            Examples
            ---------
            Importing predefined data sets by their string name

            >>> df = Data("Synthetic")

            Importing own data sets or predefined data sets manually (without header)

            >>> attr_list = ["ID", "Age", "Sex"]
            >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\\t",
            >>>       path_meta="../../data/Test/meta_test.dat", separator_meta = "\\t",
            >>>       meta_attr_list=attr_list)

            Importing own data sets or predefined data sets manually (with headers for tij- and metadata)

            >>> test_df = Data(path_tij="../../data/Synthetic_Data/synthetic_tij.dat", separator_tij=",",
            >>>       path_meta="../../data/Synthetic_Data/synthetic_metadata.dat", separator_meta = ",", header= "all")

            """
        script_path = __file__
        script_path = script_path.replace("\\", "/")
        path = str(script_path.replace("imports/load_all_data.py", ""))

        data_set = {"test": {"tij": [str(path + "data/Test/tij_test.dat"), "\t"],
                             "meta": [str(path + "data/Test/meta_test.dat"), "\t"],
                             "attr": {0: "ID", 1: "Age", 2: "Gender"}},
                    "Synthetic": {"tij": [str(path + "data/Synthetic_Data/synthetic_tij.dat"), ","],
                                  "meta": [str(path + "data/Synthetic_Data/synthetic_metadata.dat"), ","],
                                  "attr": {0: "ID", 1: "type"}},
                    }

        if data_set_name is not None:
            if len(data_set[data_set_name]) == 3:
                self.interaction = pd.read_csv(data_set[data_set_name]["tij"][0], sep=data_set[data_set_name]["tij"][1],
                                               header=None, engine='python', index_col=False)
                self.metadata = pd.read_csv(data_set[data_set_name]["meta"][0], sep=data_set[data_set_name]["meta"][1],
                                            header=None, engine='python', index_col=False)

                self.interaction = self.interaction.rename(columns={0: "Time", 1: "i", 2: "j"})
                self.interaction.index.name = 'Index'
                self.metadata = self.metadata.rename(columns=data_set[data_set_name]["attr"])
                self.metadata.index.name = 'Index'
            elif len(data_set[data_set_name]) == 1:
                self.interaction = pd.read_csv(data_set[data_set_name]["tij"][0], sep=data_set[data_set_name]["tij"][1],
                                               header=None, engine='python', index_col=False)

                self.interaction = self.interaction.rename(columns={0: "Time", 1: "i", 2: "j"})
                self.interaction.index.name = 'Index'

        elif data_set_name is None and header is None:
            if meta_attr_list is not None:
                self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=None, engine='python',
                                               index_col=False)
                self.metadata = pd.read_csv(path_meta, sep=separator_meta, header=None, engine='python',
                                            index_col=False)

                self.interaction = self.interaction.rename(columns={0: "Time", 1: "i", 2: "j"})
                self.interaction.index.name = 'Index'
                columns = {}
                for i in range(len(meta_attr_list)):
                    columns[i] = meta_attr_list[i]
                self.metadata = self.metadata.rename(columns=columns)
                self.metadata.index.name = 'Index'
            elif meta_attr_list is None and path_tij is not None:

                self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=None, engine='python',
                                               index_col=False)
                self.interaction = self.interaction.rename(columns={0: "Time", 1: "i", 2: "j"})
                self.interaction.index.name = 'Index'

        elif data_set_name is None and header is not None:
            if header == "meta":

                self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=None, engine='python',
                                               index_col=False)
                self.metadata = pd.read_csv(path_meta, sep=separator_meta, header=0, engine='python',
                                            index_col=False)
                self.interaction = self.interaction.rename(columns={0: "Time", 1: "i", 2: "j"})
                self.interaction.index.name = 'Index'
                self.metadata.index.name = 'Index'

            elif header == "tij":
                if meta_attr_list is None and path_meta is None:

                    self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=0, engine='python',
                                                   index_col=False)
                    self.interaction.index.name = 'Index'
                else:
                    if path_tij and path_meta and meta_attr_list is not None:

                        self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=0, engine='python',
                                                       index_col=False)
                        self.metadata = pd.read_csv(path_meta, sep=separator_meta, header=None, engine='python',
                                                    index_col=False)

                        self.interaction.index.name = 'Index'
                        columns = {}
                        for i in range(len(meta_attr_list)):
                            columns[i] = meta_attr_list[i]
                        self.metadata = self.metadata.rename(columns=columns)
                        self.metadata.index.name = 'Index'

            elif header == "all":
                if path_tij and path_meta is not None:

                    self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=0, engine='python',
                                                   index_col=False)
                    self.metadata = pd.read_csv(path_meta, sep=separator_meta, header=0, engine='python',
                                                index_col=False)

                    self.interaction.index.name = 'Index'
                    self.metadata.index.name = 'Index'
                else:
                    self.interaction = pd.read_csv(path_tij, sep=separator_tij, header=0, engine='python',
                                                   index_col=False)
                    self.interaction.index.name = 'Index'

        if meta_df is not None and tij_df is not None:
            self.interaction = tij_df
            self.metadata = meta_df
            self.interaction.index.name = 'Index'
            self.metadata.index.name = 'Index'
        elif meta_df is None and tij_df is not None:
            self.interaction = tij_df
            self.interaction.index.name = 'Index'

    def replace_str_attr_to_float(self):

        """Replace string attribute values

        Replaces string attributes into float attributes for the null model functions.

        Parameters
        ----------
        self : Data
            Data Object that contains Tij- and Metadata for a data set.

        Returns
        --------
        self : Data
            Data Object that contains Tij- and Metadata for a data set. Metadata string attribute values are changed
            into float values.

        Examples
        ---------
        As you can see in this example every non-numerical or NaN value gets replaced into a float value. In this case
        "F" turns into 0.0 and "M" turns into 1.0.

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>                meta_attr_list=attr_list)
        >>> print(test_df.metadata)
                ID     Age  Sex
        Index
        0       0 1.00000    F
        1       1 0.00000  NaN
        2       2     nan    M
        3       3 0.00000    F
        4       4     nan    M
        5       6 1.00000    F
        6       7 1.00000  NaN
        7      10 2.00000    F
        8      11 2.00000    M
        9      12 2.00000    F
        >>> test_df.replace_str_attr_to_float()
        >>> print(test_df.metadata)
                ID     Age    Sex
        Index
        0       0 1.00000 0.00000
        1       1 0.00000     NaN
        2       2     NaN 1.00000
        3       3 0.00000 0.00000
        4       4     NaN 1.00000
        5       6 1.00000 0.00000
        6       7 1.00000     NaN
        7      10 2.00000 0.00000
        8      11 2.00000 1.00000
        9      12 2.00000 0.00000

        """

        self.metadata = self.metadata.fillna("NaN")

        parameter_list = []
        for col in self.metadata.columns:
            if col != "ID":
                parameter_list.append(col)

        parameter_specification_list = []
        for i in parameter_list:
            contacts_of_i = list(set(self.metadata[i]))
            parameter_specification_list.append(contacts_of_i)

        mapping = {}
        for i in parameter_specification_list:
            for j in range(len(i)):
                if isinstance(i[j], str) and i[j] != "NaN":
                    mapping[i[j]] = float(j)
        self.metadata = self.metadata.replace(mapping)
        return self




