import random

import networkx as nx
import numpy as np
import scipy


from face2face.imports.load_all_data import Data
from face2face.imports.create_network import create_network_from_data

np.set_printoptions(precision=16)


def check_bonferroni_correction(contact_matrix):

    r"""Apply the bonferroni correction on the contact matrix

        Calculates the p_values of the contact matrix and applies the bonferroni correction on the contact matrix

        Parameters
        ----------
        contact_matrix: list
            A matrixlike List of lists that contains the z-scores for a given attribute.

        Returns
        -------
        annotation_list: list
            A matrixlike list of lists that contains the annotated z-scores for a given attribute. They are annotated
            with a * if they are too small in terms of the bonferroni correction.

        Notes
        -----
        The annotation_list contains the z-scores of the contact matrix and adds a * at every z-score that is an outlier

        References
        ----------


        Examples
        ---------
        >>> cm = np.array([[1, 1, 3.4], [1, 1, 1], [3.4, 1, 1]])
        >>> annotated_cm = check_bonferroni_correction(cm)
        >>> print(annotated_cm)
        [['1.0', '1.0', '3.4*'], ['1.0', '1.0', '1.0'], ['3.4*', '1.0', '1.0']]

        See Also
        ---------
        face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix
        face2face.statistics.null_modell.shuffle_label_z_score_mixing_matrix

        """
    alpha = 0.01
    p_values = scipy.stats.norm.sf(abs(contact_matrix))
    k = len(contact_matrix) - 1
    p_value = 1-(1-alpha)**(1/k)
    annotation_list = []
    for i in range(len(p_values)):
        annot_list = []
        for j in range(len(p_values[i])):
            if p_values[i][j] < p_value:
                annot_z_score = str(round(contact_matrix[i][j], 2)) + '*'
                annot_list.append(annot_z_score)
            else:
                annot_z_score = round(contact_matrix[i][j], 2)
                annot_list.append(annot_z_score)
        annotation_list.append(annot_list)
    annotation_list = np.array(annotation_list)

    return annotation_list


def mapping_function(Data, label="type"):

    r"""Creates a mapping

        Creates a mapping dict to create the attribute mixing matrix dynamic independent of the amount of attributes

        Parameters
        ----------
        Data: Data
            Data Object that contains Tij- and Metadata for a dataset.
        label: str
            A string that tells the function which attribute should be mapped.

        Returns
        -------
        mapping: dict
            A dictionary that contains the dimensions of the given attribute.

        Examples
        ---------
        Based on the amount of attribute values the used attribute has, you have to create a mapping for the
        null model functions.
        >>> mapping = mapping_function(test_df, label="Age")
        >>> print(mapping)
        {0: 0, 1: 1, 2: 2}
        >>> mapping = mapping_function(test_df, label="Sex")
        >>> print(mapping)
        {0: 0, 1: 1}

        See Also
        ---------
        face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix
        face2face.statistics.null_modell.shuffle_label_z_score_mixing_matrix

        """
    df_meta_nan = Data.metadata.fillna("NaN")
    attr_list = set(df_meta_nan[label])
    if "NaN" in attr_list:
        attr_list.remove("NaN")
    mapping = {}
    for i in range(len(attr_list)):
        mapping[i] = i

    return mapping


def configuration_model_label_z_score_mixing_matrix(Data, runs=1000, label="type", shuffle_label=False,
                                                    force_simple_graph=False, seed_config_mat=None, seed_label=None):

    r"""Creates a contact matrix based on the configuration model

        Creates a contact matrix with z-scores based on the choosen attribute. You can assume randomized attributes and/
        or randomized degrees in the null model.

        Parameters
        ----------
        Data: Data
            Data Object that contains Tij- and Metadata for a dataset.
        runs: int
            The amount of times the function should be executed. It's a heuristic approach, so the more the runs the
            better might be the result
        label: str
            A string that tells the function for which attribute the contact matrix should be made.
        shuffle_label: bool
            Gives the option to extend the null model by randomizing the node attributes.
        force_simple_graph: bool
            Deletes parallel- and selfedges that can occur by using the networkx "configuration_model"-function if True.
        seed_config_mat : List, default None
            Allows to create reproducable configuration models for a reproducable output. This parameters is basically
            just for applying tests.
        seed_label : list, default None
            Allows to create reproducable "randomized" labels for a reproducable output. This parameters is basically
            just for applying tests.

        Returns
        -------
        contact_matrix : list
             A matrixlike List of lists that contains the z-scores for a given attribute

        Notes
        -----

        References
        ----------
        .. [1] Génois, Mathieu & Zens, Maria & Lechner, Clemens & Rammstedt, Beatrice & Strohmaier, Markus. (2019). Building
        connections: How scientists meet each other during a conference.

        Examples
        ---------
        >>> contact_matrix = configuration_model_label_z_score_mixing_matrix(test_network, test_df, runs=1000,
        >>>                                                                  label="Age", shuffle_label=True,
        >>>                                                                  force_simple_graph=True)
        >>> print(contact_matrix)
        [[1.0320936930842797, -0.7717976357301974, -0.5],
        [-0.7717976357301974, -0.0667601413575786, -1.2927763604862383],
        [-0.5, -1.2927763604862383, 2.632147318581194]]

        See Also
        ---------
        face2face.statistics.null_modell.shuffle_label_z_score_mixing_matrix
        """

    network = create_network_from_data(Data, replace_attr=True, label=label)
    mapping = mapping_function(Data, label)
    data_mixing_matrix = nx.assortativity.attribute_mixing_matrix(network, label, mapping=mapping)
    degree_sequence = [v[1] for v in network.degree]
    type_sequence = [network.nodes[n][label] for n in network.nodes]
    matrices = []
    matrices_abs = []
    for _ in range(runs):
        if seed_config_mat is None:
            null_model = nx.configuration_model(degree_sequence)
        else:
            null_model = nx.configuration_model(degree_sequence, seed=seed_config_mat[_])
        if force_simple_graph:
            null_model = to_simple_graph(null_model)
        if shuffle_label:
            if seed_label is None:
                np.random.shuffle(type_sequence)
            else:
                random.Random(seed_label[_]).shuffle(type_sequence)
        for n, t in zip(null_model.nodes, type_sequence):
            null_model.nodes[n][label] = t
        matrices.append(nx.assortativity.attribute_mixing_matrix(null_model, label, mapping=mapping))
        matrices_abs.append(nx.assortativity.attribute_mixing_matrix(null_model, label, mapping=mapping, normalized=False))

    return (data_mixing_matrix - np.array(matrices).mean(axis=0))/np.array(matrices).std(axis=0), matrices, \
        data_mixing_matrix, matrices_abs


def shuffle_label_z_score_mixing_matrix(Data, runs=1000, label="type", seed_label=None):

    r"""Creates a contact matrix based on a null model with randomized identities.

        Creates a contact matrix with z-scores based on the choosen attribute. You can assume randomized identities.

        Parameters
        ----------
        network : networkX Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported dataset.
        Data: Data
            Data Object that contains Tij- and Metadata for a dataset.
        runs: int
            The amount of times the function should be executed. It's a heuristic approach, so the more the runs the
            better might be the result
        label: str
            A string that tells the function for which attribute the contact matrix should be made.
        seed_label : list, default None
            Allows to create reproducable "randomized" labels for a reproducable output. This parameters is basically
            just for applying tests.

        Returns
        -------
        contact_matrix : list
             A matrixlike List of lists that contains the z-scores for a given attribute and randomized identities.

        Notes
        -----

        References
        ----------
        .. [2] Génois, Mathieu & Zens, Maria & Lechner, Clemens & Rammstedt, Beatrice & Strohmaier, Markus. (2019). Building connections: How scientists meet each other during a conference.

        Examples
        ---------
        >>> contact_matrix = shuffle_label_z_score_mixing_matrix(test_network, test_df, runs=1000, label="Age"):
        >>> print(contact_matrix)
        [[1.2247448713915892, -0.44846105565116173, -1.5452456409610384],
        [-0.44846105565116173, 2.0, -3.143958736099446],
        [-1.5452456409610384, -3.143958736099446, 5.719237485832778]]

        See Also
        ---------
        face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix

        """

    df = Data

    network = create_network_from_data(df, replace_attr=True, label=label)
    network = network.copy()
    mapping = mapping_function(df, label)
    data_mixing_matrix = nx.assortativity.attribute_mixing_matrix(network, label, mapping=mapping)

    def shuffle_labels(graph):
        if seed_label is None:
            data_group_nodes = [graph.nodes[n][label] for n in graph.nodes]
            np.random.shuffle(data_group_nodes)
        else:
            data_group_nodes = [graph.nodes[n][label] for n in graph.nodes]
            random.Random(seed_label[_]).shuffle(data_group_nodes)
        for n, new_label in zip(graph.nodes, data_group_nodes):
            graph.nodes[n][label] = new_label
        return graph
    matrices = []
    matrices2 = []
    for _ in range(runs):
        shuffle_labels(network)
        matrices.append(nx.assortativity.attribute_mixing_matrix(network, label, mapping=mapping))
        matrices2.append(nx.assortativity.attribute_mixing_matrix(network, label, mapping=mapping, normalized=False))

    return (data_mixing_matrix - np.array(matrices).mean(axis=0))/np.array(matrices).std(axis=0), matrices2


def remove_self_loops(graph):

    r"""Removes self-loops that occur by using the "configuration_model"-function

        Removes self-loops that occur by using the "configuration_model"-function

        Parameters
        ----------
        graph : networkX Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported dataset. Graph might
            contain self loops

        Returns
        ---------
        graph : networkX Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported dataset. Graph contains
            no selfloops anymore.

        Notes
        -----

        References
        ----------

        Examples
        ---------
        The :func:`networkx.configuration_model` function which is being used for the configuration model can lead to
        self- and parellel edges. As you can see here the function :func:`remove_self_loops` filters self loops out of
        the network.

        >>> degree_sequence_1 = [v[1] for v in test_network.degree]
        >>> test_model = nx.configuration_model(degree_sequence_1)
        >>> print(test_model.edges)
        [(0, 1, 0), (1, 1, 0), (2, 6, 0), (2, 3, 0), (3, 4, 0), (4, 8, 0), (5, 5, 0), (6, 9, 0), (7, 8, 0), (7, 9, 0)]
        >>> remove_self_loops(test_model)
        >>> print(test_model.edges)
        [(0, 1, 0), (2, 6, 0), (2, 3, 0), (3, 4, 0), (4, 8, 0), (6, 9, 0), (7, 8, 0), (7, 9, 0)]

         See Also
         ---------
         face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix

         """
    self_loops = []
    for e in graph.edges:
        if e[0] == e[1]:
            self_loops.append(e)
    graph.remove_edges_from(self_loops)
    return graph


def to_simple_graph(graph):
    graph = nx.Graph(graph)
    graph = remove_self_loops(graph)
    return graph


