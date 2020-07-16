import pytest
from face2face import Data
from face2face.statistics.calculating_multiple_measurements_for_a_network import *
from face2face.imports.create_network import create_network_from_data


@pytest.fixture
def supply_network_measurements():
    attr_list = ["ID", "Age", "Sex"]
    test_df = Data(path_tij=r"face2face/data/Test/tij_test.dat", separator_tij="\t",
                   path_meta=r"face2face/data/Test/meta_test.dat", separator_meta="\t",
                   meta_attr_list=attr_list)
    test_network = create_network_from_data(test_df)

    return [test_network]


def test_number_edges_nodes(supply_network_measurements):

    number_of_nodes, number_of_edges = calculating_number_of_edges_nodes(supply_network_measurements[0])

    assert number_of_nodes and number_of_edges == 10, "Test failed"


def test_mean_degree_network(supply_network_measurements):

    k = mean_degree_network(supply_network_measurements[0])

    assert k == 2, "Test failed"


def test_var_std(supply_network_measurements):

    var, std = variance_std_network(supply_network_measurements[0])

    assert var == 0.2 and std == 0.4472135954999579, "Test failed"


def test_average_path_length(supply_network_measurements):

    d = average_path_length_network(supply_network_measurements[0])

    assert d == 3.3219280948873626, "Test failed"


def test_clustering_coefficient(supply_network_measurements):

    c = clustering_coefficient(supply_network_measurements[0])

    assert c == 0.2, "Test failed"