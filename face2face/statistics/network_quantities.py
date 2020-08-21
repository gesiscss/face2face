import math

from face2face.imports.load_all_data import Data


def calculating_number_of_edges_nodes(network):
    r"""Calculate number of edges/nodes

        Calculating the amount of edges and nodes for a given network

        Parameters
        ----------
        network: networkx Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported data set.

        Returns
        -------
        number_of_nodes: int
            Contains the number of nodes.
        number_of_edges: int
            Contains the number of edges.

        Examples
        ---------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>               meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> number_of_nodes, number_of_edges = calculating_number_of_edges_nodes(test_network)
        >>> print(number_of_nodes)
        10
        >>> print(number_of_edges)
        10

        """
    number_of_nodes = len(network.nodes)
    number_of_edges = len(network.edges)

    return number_of_nodes, number_of_edges


def mean_degree_network(network):
    r"""Calculate average degree

        Calculating the average degree of a given random network

        .. math::

            \langle k \rangle = \frac{2 * \langle L \rangle}{N}

        Parameters
        ----------
        network: networkx Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported dataset.

        Returns
        -------
        k: float
            Contains the average degree for a network.

        References
        ----------
        .. [1] Barabasi, Albert-Laszlo. (2013). Network science. Philosophical transactions. Series A, Mathematical,
               physical, and engineering sciences. 371. 20120375. 10.1098/rsta.2012.0375.

        Examples
        --------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>               meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> k = mean_degree_network(test_network)
        >>> print(k)
        2

        """
    k = (2 * len(network.edges))/len(network.nodes)

    return k


def variance_std_network(network):
    r"""Calculate variance and standard deviation

        Calculating the variance and the standard deviation of the degrees of a given network

        .. math::

            \sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})

        .. math::

            \sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}

        Parameters
        ----------
        network: networkx Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported data set.

        Returns
        -------
        var: float
            Contains the variance of the network degree
        std: float
            Contains the standard deviation of the network degree

        Examples
        ---------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>                meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> variance, standard_deviation = variance_std_network(test_network)
        >>> print(variance)
        0.2
        >>> print(standard_deviation)
        0.4472135954999579

        """
    var = 0
    k = mean_degree_network(network)
    for i in network.degree:
        var += (i[1] - k)**2
    var = var/len(network.degree)
    std = var**(1/2)

    return var, std


def average_path_length_network(network):
    r"""Calculate the average path length

        Calculating the average path length <d> of a given network

        .. math::

            d_{max} \approx \frac{\ln N}{\ln \langle k \rangle}

        Parameters
        ----------
        network: networkx Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported data set.

        Returns
        -------
        d: float
            Contains the Average Path Length

        References
        ----------
        .. [1] Barabasi, Albert-Laszlo. (2013). Network science. Philosophical transactions. Series A, Mathematical,
               physical, and engineering sciences. 371. 20120375. 10.1098/rsta.2012.0375.

        Examples
        --------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>                meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> d = average_path_length_network(test_network)
        >>> print(d)
        3.3219280948873626

        """

    n_nodes, n_edges = calculating_number_of_edges_nodes(network)
    k = mean_degree_network(network)
    d = math.log(n_nodes)/math.log(k)

    return d


def clustering_coefficient(network):
    r"""Calculate the global Clustering Coefficient

        Calculating the global Clustering Coefficient C for a given network

        .. math::

            \langle L_i \rangle = p \frac{k_i(k_i - 1)}{2}

        .. math::

            C_i = \frac{2 \langle L_i \rangle}{k_i(k_i - 1)} = p = \frac{\langle k \rangle}{N}

        Parameters
        ----------
        network: networkx Graph
            A graph with a specified degree sequence. Nodes are labeled based on the imported data set.

        Returns
        -------
        c: float
            Contains the Clustering Coefficient for the network.

        References
        ----------
         .. [1] Barabasi, Albert-Laszlo. (2013). Network science. Philosophical transactions. Series A, Mathematical,
                physical, and engineering sciences. 371. 20120375. 10.1098/rsta.2012.0375.


        Examples
        --------

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>                path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>                meta_attr_list=attr_list)
        >>> test_network = create_network_from_data(test_df)
        >>> C = clustering_coefficient(test_network)
        >>> print(C)
        0.2

        """
    n_nodes, n_edges = calculating_number_of_edges_nodes(network)
    k = mean_degree_network(network)
    c = k / n_nodes

    return c
