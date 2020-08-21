import math

import pandas as pd

from face2face.imports.create_network import create_network_from_data
from face2face.imports.load_all_data import Data

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def avg_degree_attr(df):
    """Calculates the average degree

        Calculates the average degree for every subgroup and for the whole group for every attribute.

        Parameters
        ----------
        df: Data
            Data Object that contains Tij- and Metadata for a data set.

        Returns
        -------
        attr_degree_list : list
            A list that contains the average degree for every subgroup and for the whole group for every attribute.

        Examples
        ---------
        The first string in a list, for example "Age", tells you which attribute's average degrees are in this list.
        The following first list entries for example 0.0, 1.0 or 2.0 are the different attribute values and the second
        entry in the list is the average degree for this attribute value. The 'GlobalAvG' list entry tells you the
        average degree for the whole attribute (for example "Age").

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
        >>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
        >>>               meta_attr_list=attr_list)
        >>> avg_degree_list = avg_degree_attr(test_df)
        >>> print(avg_degree_list)
        [['Age', [[0.0, 1.6666666666666667], [1.0, 2.5], [2.0, 2.0], ['GlobalAvG', 2.055555555555556]]],
         ['Sex', [['F', 1.8], ['M', 2.0], ['GlobalAvG', 1.9]]]]

        See Also
        ---------
        face2face.group_list_degree
        face2face.global_avg_var_std

        """

    network = create_network_from_data(df)
    df_meta_nan = df.metadata.fillna("NaN")

    parameter_list = []
    for col in df_meta_nan.columns:
        if col != "ID":
            parameter_list.append(col)

    complete_parameter_value_list = []
    for i in parameter_list:
        parameter_value_list = []
        nan_filtered_dataframe = df.metadata.loc[df.metadata[i] != "NaN"]
        for parameter_values, grouped_by_dataframes in nan_filtered_dataframe.groupby(i):
            parameter_value_list.append([grouped_by_dataframes["ID"], parameter_values])
        complete_parameter_value_list.append([i, parameter_value_list])

    avg_degree_param_list = []
    for i in complete_parameter_value_list:
        value_avg_degree_pair_list = []
        for j in i[1]:
            avg_degree = 0
            for k in j[0]:
                avg_degree += network.degree[k]
            avg_degree = avg_degree / len(j[0])
            value_avg_degree_pair_list.append([j[1], avg_degree])
        avg_degree_param_list.append([i[0], value_avg_degree_pair_list])

    for i in avg_degree_param_list:
        avg_degree_parameter = 0
        for j in i[1]:
            avg_degree_parameter += j[1]
        avg_degree_parameter = avg_degree_parameter / len(i[1])
        i[1].append(["GlobalAvG", avg_degree_parameter])

    return avg_degree_param_list


def group_list_degree(df):
    """Creates lists of the degrees

       Creating a list of degrees for every attribute value of every group

       Parameters
       ----------
       df: Data
           Contains a dataframe with the tij-data from the data set

       Returns
       -------
       attr_degree_list: list
           Contains lists for all attributes and all occurring degrees for the different attribute values.

       Examples
       ---------
       This functions return a list of lists which contains a list for every attribute value. In this list you have the
       attribute as a string, the attribute value and a list with all degrees for this attribute value.

       >>> attr_list = ["ID", "Age", "Sex"]
       >>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\t",
       >>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\t",
       >>>               meta_attr_list=attr_list)
       >>> attr_degree_list = group_list_degree(test_df)
       [['Age', 1.0, [1, 2, 2]], ['Age', 0.0, [3, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]],
       ['Sex', 'M', [2, 2, 2]]]


       See Also
       ----------
       face2face.avg_degree_attr
       face2face.global_avg_var_std

       """
    df_meta_nan = df.metadata.fillna("NaN")
    network = create_network_from_data(df)

    parameter_list = []
    for col in df_meta_nan.columns:
        if col != "ID":
            parameter_list.append(col)

    complete_parameter_value_list = []
    for i in parameter_list:
        nan_filtered_dataframe = df.metadata.loc[df.metadata[i] != "NaN"]
        for parameter_values, grouped_by_dataframes in nan_filtered_dataframe.groupby(i):
            complete_parameter_value_list.append([i, parameter_values, list(grouped_by_dataframes["ID"])])

    for i in complete_parameter_value_list:
        parameter_value_degree_list = []
        for j in i[2]:
            parameter_value_degree_list.append(network.degree(j))
        i[2] = parameter_value_degree_list[:]
    return complete_parameter_value_list


def global_avg_var_std(attr_degree_list):
    """Calculating global degree measures

    Calculate the average, the variance and the standard deviation for the degrees of the whole data set.

    Parameters
    ----------
    attr_degree_list : list
        This list is the output of :mod:`~face2face.statistics.average_degree.avg_degree_attribute`.

    Returns
    -------
    measures : list
        This list contains the average degree, the variance and the standard deviation for the degrees of the whole
        data set.

    Examples
    --------
    You can use the output of the :meth:`avg_degree_attr` method as input for this function. The return of this function
    is the average degree, the variance of the degree and the standard deviation for the degree of all attributes.

    >>> attr_degree_list = avg_degree_attr(test_df)
    >>> print(attr_degree_list)
    [['Age', 1.0, [1, 2, 2]], ['Age', 0.0, [3, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]],
    ['Sex', 'M', [2, 2, 2]]]
    >>> measures = global_avg_var_std(attr_degree_list)
    >>> print(measures)
    [1.9777777777777779, 0.006049382716049409, 0.07777777777777795]

    See Also
    ---------
    face2face.avg_degree_attr
    face2face.group_list_degree

    """
    total_sum = 0
    for i in attr_degree_list:
        total_sum += i[1][-1][1]
    global_mean = total_sum/len(attr_degree_list)

    variance = 0
    for i in attr_degree_list:
        variance += (i[1][-1][1] - global_mean)**2
    variance = variance/len(attr_degree_list)

    std = math.sqrt(variance)
    measures = [global_mean, variance, std]
    return measures

