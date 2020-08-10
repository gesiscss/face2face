import pytest

from face2face.statistics.average_degree import *


@pytest.fixture
def supply_average_degree_functions():
    attr_list = ["ID", "Age", "Sex"]
    test_df = Data(path_tij=r"face2face/data/Test/tij_test.dat", separator_tij="\t",
                   path_meta=r"face2face/data/Test/meta_test.dat", separator_meta="\t",
                   meta_attr_list=attr_list)

    attr_degree_list_fix = [['Age', [[0.0, 2.5], [1.0, 1.6666666666666667], [2.0, 2.0], ['GlobalAvG', 2.055555555555556]]], ['Sex', [['F', 1.8], ['M', 2.0], ['GlobalAvG', 1.9]]]]
    #group_list_degree_fix = [['Age', 1.0, [1, 2, 2]], ['Age', 0.0, [3, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]], ['Sex', 'M', [2, 2, 2]]]
    group_list_degree_fix = [['Age', 0.0, [3, 2]], ['Age', 1.0, [1, 2, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]], ['Sex', 'M', [2, 2, 2]]]
    measures_fix = [1.9777777777777779, 0.006049382716049409, 0.07777777777777795]
    return [test_df, attr_degree_list_fix, group_list_degree_fix, measures_fix]


def test_average_degree(supply_average_degree_functions):
    attr_degree_list = avg_degree_attr(supply_average_degree_functions[0])

    assert attr_degree_list == supply_average_degree_functions[1], "Test failed"


def test_group_list_degree(supply_average_degree_functions):
    group_degree_list = group_list_degree(supply_average_degree_functions[0])

    assert group_degree_list == supply_average_degree_functions[2], "Test failed"


def test_global_avg_var_std(supply_average_degree_functions):
    measures = global_avg_var_std(supply_average_degree_functions[1])

    assert measures == supply_average_degree_functions[3], "Test failed"
