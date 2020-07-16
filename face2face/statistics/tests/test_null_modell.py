import pytest
import numpy as np
from face2face import Data, create_network_from_data
from face2face.statistics.null_modell import *


@pytest.fixture
def supply_null_modell_functions():
    test_label_1 = "Age"
    test_label_2 = "Sex"

    attr_list = ["ID", "Age", "Sex"]
    test_df = Data(path_tij=r"face2face/data/Test/tij_test.dat", separator_tij="\t",
                   path_meta=r"face2face/data/Test/meta_test.dat", separator_meta="\t",
                   meta_attr_list=attr_list)
    test_network = create_network_from_data(test_df)

    return [test_df, test_network, test_label_1, test_label_2]


def test_mapping_function(supply_null_modell_functions):
    mapping_label_1 = mapping_function(supply_null_modell_functions[0], label=supply_null_modell_functions[2])

    mapping_label_2 = mapping_function(supply_null_modell_functions[0], label=supply_null_modell_functions[3])

    assert mapping_label_1 == {0: 0, 1: 1, 2: 2} and mapping_label_2 == {0: 0, 1: 1}, "Test failed"


def test_configuration_model_2_seeds(supply_null_modell_functions):
    seed_mat = [12, 123, 1234, 12345, 123456]
    seed_label = [12, 123, 1234, 12345, 123456]

    cm_seeded_config_mat_label, mat, mixing_mat, mat2 = configuration_model_label_z_score_mixing_matrix(
        supply_null_modell_functions[0], runs=5,
        label=supply_null_modell_functions[2], shuffle_label=True, force_simple_graph=True,
        seed_config_mat=seed_mat, seed_label=seed_label)
    cm_seeded_config_mat_label = [list(cm_seeded_config_mat_label[0]), list(cm_seeded_config_mat_label[1]),
                                  list(cm_seeded_config_mat_label[2])]

    cm_test_seeded_config_mat_label = [[2.0, -1.3568010505999366, -2.6475854543081474],
                                       [-1.3568010505999366, 2.0, -2.1405749388195425],
                                       [-2.6475854543081474, -2.1405749388195425, 5.30722777603022]]

    assert cm_seeded_config_mat_label == cm_test_seeded_config_mat_label, "Test failed"


def test_configuration_model_seed_config_model(supply_null_modell_functions):
    seed_mat = [1, 12, 123, 1234, 12345]
    cm_seeded_config_mat, mat, mixing_mat, mat2 = configuration_model_label_z_score_mixing_matrix(
        supply_null_modell_functions[0], runs=5,
        label=supply_null_modell_functions[2], shuffle_label=False, force_simple_graph=True,
        seed_config_mat=seed_mat)
    cm_seeded_config_mat = [list(cm_seeded_config_mat[0]), list(cm_seeded_config_mat[1]), list(cm_seeded_config_mat[2])]

    cm_test_seeded_config_mat = [[float("inf"), 0.26726124191242423, -1.7251638983558857],
                                [0.26726124191242423, 0.884537962671703, -1.779513042005218],
                                [-1.7251638983558857, -1.779513042005218, 2.4567293553997884]]
    assert cm_seeded_config_mat == cm_test_seeded_config_mat, "Test failed"


def test_null_model_shuffle_identities_seeded(supply_null_modell_functions):
    seed_label = [12, 123, 1234, 12345, 123456]

    cm_seeded_label, mat2 = shuffle_label_z_score_mixing_matrix(supply_null_modell_functions[0], runs=5,
                                                          label=supply_null_modell_functions[2], seed_label=seed_label)
    cm_seeded_label = [list(cm_seeded_label[0]), list(cm_seeded_label[1]), list(cm_seeded_label[2])]

    cm_test = [[float("inf"), -1.1180339887498951, -2.857738033247041],
                [-1.1180339887498951, 0.4999999999999999, -0.9128709291752767],
                [-2.857738033247041, -0.9128709291752767, 5.500000000000001]]

    assert cm_seeded_label == cm_test, "Test failed"


def test_remove_self_loops(supply_null_modell_functions):

    degree_sequence_1 = [v[1] for v in supply_null_modell_functions[1].degree]
    null_model_1 = nx.configuration_model(degree_sequence_1, seed=1)
    remove_self_loops(null_model_1)
    test_edges = [(0, 1, 0), (2, 6, 0), (2, 3, 0), (3, 4, 0), (4, 8, 0), (6, 9, 0), (7, 8, 0), (7, 9, 0)]

    assert list(null_model_1.edges) == test_edges, "Test failed"


def test_bonferroni_correction():
    cm = np.array([[1, 1, 3.4], [1, 1, 1], [3.4, 1, 1]])
    annotated_cm = check_bonferroni_correction(cm)
    annotated_cm = [list(annotated_cm[0]), list(annotated_cm[1]), list(annotated_cm[2])]
    test_annotated_cm = [['1.0', '1.0', '3.4*'], ['1.0', '1.0', '1.0'], ['3.4*', '1.0', '1.0']]

    assert annotated_cm == test_annotated_cm, "Test failed"