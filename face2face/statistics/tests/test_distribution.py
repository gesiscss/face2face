import pytest
from face2face import Data
from face2face.statistics.distribution import *


@pytest.fixture
def supply_example_probability():

    attr_list = ["ID", "Age", "Sex"]
    test_df = Data(path_tij=r"face2face/data/Test/tij_test.dat", separator_tij="\t",
                   path_meta=r"face2face/data/Test/meta_test.dat", separator_meta="\t",
                   meta_attr_list=attr_list)

    contact_duration_test = [[0.022727272727272728, 0.013636363636363636, 0.013636363636363636],[20, 40, 60]]
    triangle_duration_test = [[0.02142857142857143, 0.014285714285714287, 0.014285714285714287],[20, 40, 60]]
    inter_contact_duration_test = [[0.0, 0.049999999999999996, 0.0], [20, 40, 60]]

    return [test_df, contact_duration_test, triangle_duration_test, inter_contact_duration_test]


def test_contact_duration(supply_example_probability):
    bins = [20, 40, 60, 80]
    y_x_list_1, delta_t_list = calculate_contact_duration(supply_example_probability[0], bins=bins)

    assert y_x_list_1 == supply_example_probability[1], "Test failed"


def test_triangle_duration(supply_example_probability):
    bins = [20, 40, 60, 80]
    y_x_list_2, delta_t_list = calculate_triangle_duration(supply_example_probability[0], bins=bins)

    assert y_x_list_2 == supply_example_probability[2], "Test failed"


def test_inter_contact_duration(supply_example_probability):
    bins = [20, 40, 60, 80]
    y_x_list_3, delta_t_list = calculate_inter_contact_duration(supply_example_probability[0], bins=bins)
    a = y_x_list_3[0]
    b = y_x_list_3[1]
    y_x_list_4 = [b, a]
    assert y_x_list_3 == supply_example_probability[3], "Test failed"

