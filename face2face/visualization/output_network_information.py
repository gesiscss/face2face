from face2face.statistics.network_quantities import calculating_number_of_edges_nodes, \
    mean_degree_network, variance_std_network, average_path_length_network, clustering_coefficient


def print_network_measures(network):
    r"""Prints information about the network

        Prints multiple measures as a text output about the given network.

        Parameters
        ----------
        network: networkx Graph
                A graph with a specified degree sequence. Nodes are labeled based on the imported dataset.

        Returns
        -------
        None


        """
    n_nodes, n_edges = calculating_number_of_edges_nodes(network)
    k = mean_degree_network(network)
    var, std = variance_std_network(network)
    d = average_path_length_network(network)
    c = clustering_coefficient(network)

    print("Number of nodes" + " = " + str(n_nodes) + " , " + "Number of edges" + " = " + str(n_edges))
    print("Average Network degree <k>" + " = " + str(k))
    print("Standard deviation of the Network degree" + " = " + str(std))
    print("Average Path Length <d>" + " = " + str(d))
    print("Clustering Coefficient C" + " = " + str(c))

    return None
