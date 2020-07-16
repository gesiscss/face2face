from collections import Counter
import math
from face2face.imports.load_all_data import Data
from face2face.imports.create_network import create_network_from_data
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def avg_degree_attr(df):
    """Calculates the average degree

        Calculates the average degree for every attribute of every group and for the whole group

        Parameters
        ----------
        df: Data
            Data Object that contains Tij- and Metadata for a dataset.

        Returns
        -------
        attr_degree_list : list
            A list that contains the average degree for every attribute and every attribute value.

        Notes
        -----

        References
        ----------

        Examples
        ---------
        The first string in a list for example "Age" tells you which attribute's average degrees are in this list.
        The following first list entrys for example 1.0, 0.0 or 2.0 are the different attribute values and the second
        entry in the list is the average degree for this attribute value. The 'GlobalAvG' list entry tells you the
        average degree for the whole attribute (for example "Age").

        #>>> attr_list = ["ID", "Age", "Sex"]
        #>>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\\t",
        #>>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\\t",
        #>>>               meta_attr_list=attr_list)
        #>>> avg_degree_list = new_avg_degree_attr(test_df)
        #>>> print(avg_degree_list)
        [['Age', [[1.0, 2.5], [0.0, 1.6666666666666667], [2.0, 2.0], ['GlobalAvG', 2.055555555555556]]],
         ['Sex', [['F', 1.8], ['M', 2.0], ['GlobalAvG', 1.9]]]]

        See Also
        ---------
        new_group_list_degree
        global_avg_var_std

        """

    network = create_network_from_data(df)
    df_meta_nan = df.metadata.fillna("NaN")

    parameter_list = []
    for col in df_meta_nan.columns:
        if col != "ID":
            parameter_list.append(col)

    liste1 = []
    for i in parameter_list:
        liste = []
        dataframe = df.metadata.loc[df.metadata[i] != "NaN"]
        for region, df_region in dataframe.groupby(i):
            liste.append([df_region["ID"], region])
        liste1.append([i, liste])

    liste_degree = []
    for i in liste1:
        liste3 = []
        for j in i[1]:
            avg_degree = 0
            for k in j[0]:
                avg_degree += network.degree[k]
            avg_degree = avg_degree / len(j[0])
            liste3.append([j[1], avg_degree])
        liste_degree.append([i[0], liste3])

    for i in liste_degree:
        avg_gesamt = 0
        for j in i[1]:
            avg_gesamt += j[1]
        avg_gesamt = avg_gesamt / len(i[1])
        i[1].append(["GlobalAvG", avg_gesamt])

    return liste_degree


def group_list_degree(df):
    """Creates lists of the degrees

       Creating a list of degrees for every attribute of every group

       Parameters
       ----------
       df: Data
           Contains a dataframe with the tij-data from the dataset

       Returns
       -------
       attr_degree_list: list
           Contains lists for all attributes and all occuring degrees for the different attribute values.

       Notes
       -----

       References
       ----------

       Examples
       ---------
       This functions return a list of lists which contains a list for every attribute value. In this list you have the
       attribute as a string, the attribute value and a list with all degrees for this attribute value.

       #>>> attr_list = ["ID", "Age", "Sex"]
       #>>> test_df = Data(path_tij="../../data/Test/tij_test.dat", separator_tij="\\t",
       #>>>               path_meta="../../data/Test/meta_test.dat", separator_meta="\\t",
       #>>>               meta_attr_list=attr_list)
       #>>> attr_degree_list = new_group_list_degree(test_df)
       [['Age', 1.0, [1, 2, 2]], ['Age', 0.0, [3, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]],
       ['Sex', 'M', [2, 2, 2]]]


       See Also
       ----------
       new_avg_degree_attr
       global_avg_var_std

       """
    df_meta_nan = df.metadata.fillna("NaN")
    network = create_network_from_data(df)

    parameter_list = []
    for col in df_meta_nan.columns:
        if col != "ID":
            parameter_list.append(col)

    liste1 = []
    for i in parameter_list:
        dataframe = df.metadata.loc[df.metadata[i] != "NaN"]
        for region, df_region in dataframe.groupby(i):
            liste1.append([i, region, list(df_region["ID"])])
            #print(list(df_region["ID"]))

    for i in liste1:
        Liste = []
        for j in i[2]:
            #print(network.degree(j))
            #Liste.append(network.degree(i[2][j]))
            Liste.append(network.degree(j))
        i[2] = Liste[:]
    return liste1


#attr_list = ["ID", "Age", "Sex"]
#test_df = Data(path_tij=r"../data2/Test/tij_test.dat", separator_tij="\t",
#               path_meta=r"../data2/Test/meta_test.dat", separator_meta="\t",
#               meta_attr_list=attr_list)
#print(test_df.metadata, test_df.interaction)
#test = group_list_degree(test_df)
#print(test)


def global_avg_var_std(attr_degree_list):
    """Calculating global measures

    Calculate the average, the variance and the standard deviation for the global meta data

    Parameters
    ----------
    attr_degree_list : list
        This list is the output of :mod:`~face2face.statistics.average_degree.avg_degree_attribute`.

    Returns
    -------
    measures : list
        This list contains the Average Degree, the variance and the standard deviation for the degrees of the whole
        dataset

    Notes
    -----

    References
    ----------

    Examples
    --------
    You can use the output of the :meth:`avg_degree_attr` method as input for this function. The return of this function
    is the average degree, the variance of the degree and the standard deviation for the degree of all attributes.

    #>>> attr_degree_list = avg_degree_attr(test_df)
    #>>> print(attr_degree_list)
    [['Age', 1.0, [1, 2, 2]], ['Age', 0.0, [3, 2]], ['Age', 2.0, [2, 2, 2]], ['Sex', 'F', [1, 2, 2, 2, 2]],
    ['Sex', 'M', [2, 2, 2]]]
    #>>> measures = global_avg_var_std(attr_degree_list)
    #>>> print(measures)
    [1.9777777777777779, 0.006049382716049409, 0.07777777777777795]

    See Also
    ---------
    avg_degree_attr
    group_list_degree

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

