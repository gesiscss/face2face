import pytest

from face2face.imports.load_all_data import Data
from face2face.imports.create_network import create_network_from_data, hopping_time_networks, sliding_time_networks, \
                                             event_time_networks


@pytest.fixture
def supply_null_modell_functions():
    attr_list = ["ID", "Age", "Sex"]
    test_df = Data(path_tij=r"face2face/data/Test/tij_test.dat", separator_tij="\t",
                   path_meta=r"face2face/data/Test/meta_test.dat", separator_meta="\t",
                   meta_attr_list=attr_list)

    test_network = create_network_from_data(test_df)

    return [test_df, test_network]


def test_hopping_network(supply_null_modell_functions):

    network_list, df_list = hopping_time_networks(supply_null_modell_functions[0], minutes=2/3)
    last_edges = list(network_list[-1].edges)
    first_nodes = list(network_list[0].nodes)
    assert len(network_list) == 9 and last_edges == [(10, 11), (10, 12), (11, 12)] and first_nodes == [0, 1, 2, 3],\
        "Test failed"


def test_sliding_network(supply_null_modell_functions):

    network_list, df_list = sliding_time_networks(supply_null_modell_functions[0], slide=1/3, interval=2/3)

    last_edges = list(network_list[-1].edges)
    first_nodes = list(network_list[0].nodes)

    assert len(network_list) == 16 and last_edges == [(10, 11), (10, 12), (11, 12)] and first_nodes == [0, 1, 2, 3], \
        "Test failed"


def test_event_network(supply_null_modell_functions):
    event_list = [("Event A", 20, 80), ("Event B", 120, 180), ("Event C", 400, 500)]
    network_list, df_list = event_time_networks(supply_null_modell_functions[0], event_list)
    last_edges = list(network_list[-1].edges)
    first_nodes = list(network_list[0].nodes)
    last_edges_test = [(1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (6, 7), (10, 11), (10, 12), (11, 12)]
    first_nodes_test = [1, 2, 3, 4, 6, 7]

    assert len(network_list) == 3 and last_edges == last_edges_test and first_nodes == first_nodes_test, "Test failed"