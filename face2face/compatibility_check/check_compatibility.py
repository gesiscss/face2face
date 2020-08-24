def check_compatibility_of_versions():

    """Check installed packages needed for this library

       Checks if the installed package versions that are needed for this library contain the needed functions.

       Parameters
       ----------
       None

       Returns
       -------
       dictionary: dict
           Contains the packages needed for this library with the probably missing functions of the packages

       See Also
       ---------
       face2face.compatibility_check.check_compatibility.check_which_methods_are_affected
       """

    dictionary = {}

    import pandas
    pandas_requirements = ["merge", "groupby", "size", "reset_index", "iterrows", "columns", "values", "tail",
                           "read_csv", "rename", "index", "fillna", "replace", "loc", "sort_values", "cumsum",
                           "drop_duplicates", "diff","tolist"]
    pandas_functions = dir(pandas.DataFrame) + dir(pandas) + dir(pandas.Series)
    dictionary["pandas"] = []
    for i in pandas_requirements:
        if i not in pandas_functions:
            dictionary["pandas"].append(i)

    import networkx
    networkx_requirements = ["add_nodes_from", "add_edge", "set_node_attributes", "degree", "nodes", "edges",
                             "attribute_mixing_matrix",
                             "assortativity", "configuration_model", "copy", "remove_edges_from"]

    networkx_functions = dir(networkx) + dir(networkx.Graph)
    dictionary["networkx"] = []
    for i in networkx_requirements:
        if i not in networkx_functions:
            dictionary["networkx"].append(i)

    import numpy
    numpy_requirements = ["tolist", "linspace", "array", "append", "histogram", "shuffle", "ravel", "log10"]

    numpy_functions = dir(numpy) + dir(numpy.ndarray) + dir(numpy.random)
    dictionary["numpy"] = []
    for i in numpy_requirements:
        if i not in numpy_functions:
            dictionary["numpy"].append(i)

    import powerlaw

    powerlaw_requirements = ["Fit", "generate_random", "distribution_compare"]

    powerlaw_functions = dir(powerlaw) + dir(powerlaw.Distribution) + dir(powerlaw.Fit)
    dictionary["powerlaw"] = []
    for i in powerlaw_requirements:
        if i not in powerlaw_functions:
            dictionary["powerlaw"].append(i)

    import matplotlib.pyplot as plt
    from matplotlib.text import Annotation
    matplotlib_requirements = ["subplots", "set_title", "set_text", "title", "twiny", "bar", "set_ylabel", "set_xlabel",
                               "set_xlim","tick_params", "axhline", "axhspan", "axvline", "text", "legend", "boxplot",
                               "xticks","ylabel", "xlabel", "show","tight_layout","plot"]

    matplotlib_functions = dir(plt) + dir(plt.Axes) + dir(Annotation)
    dictionary["matplotlib"] = []
    for i in matplotlib_requirements:
        if i not in matplotlib_functions:
            dictionary["matplotlib"].append(i)

    from scipy.stats import norm
    scipy_function = dir(norm)
    if "sf" not in scipy_function:
        dictionary["scipy"] = "sf"

    import random
    random_function = dir(random.Random)
    if "shuffle" not in random_function:
        dictionary["random"] = "shuffle"

    import seaborn
    seaborn_function = dir(seaborn)
    if "heatmap" not in seaborn_function:
        dictionary["seaborn"] = "heatmap"

    import math
    math_requriements = ["log","sqrt"]
    math_function = dir(math)
    dictionary["math"] = []
    for i in math_requriements:
        if i not in math_function:
            dictionary["math"].append(i)

    import collections
    collections_function = dir(collections)
    if "Counter" not in collections_function:
        dictionary["collections"] = "Counter"

    return dictionary


#dictionary2 = check_compatibility_of_versions()
#print(dictionary2)


def check_which_methods_are_affected(dict):

    """Check for affected library functions

       Checks which library functions are directly affected by missing functions of the installed version of the
       packages. Based on that the user can decide if he needs this functions and therefore another version of a
       package.

       Parameters
       ----------
       dict: dict
           Contains the packages needed for this library with the probably missing functions of the packages

       Returns
       -------
       None

       See Also
       ---------
       face2face.compatibility_check.check_compatibility.check_compatibility_of_versions
       """

    import pandas
    liste = []
    df = pandas.read_csv("Functions_for_functions.csv", sep=';', engine='python')
    for column in df:
        for key, value in dict.items():
            for i in value:
                if i in df[column].tolist():
                    liste.append(str(column))

    liste = list(set(liste))

    dictionary3 = {
        "create_network" : ["create_network","hopping","sliding","event","replace_float_2"],
        "load_all_data" : ["Data"],
        "average_degree" : ["new_avg_degree","avg_degree","new_group_degree","group_degree"],
        "calculating_multiple_measurements_for_a_network" : ["number_edges_nodes","mean_degree","average_path"],
        "check_distribution" : ["search_best_fit","get_best_fit","tupels_comb"],
        "distribution" : ["contact_duration","triangle_duration","inter_contact"],
        "null_modell" : ["bonferroni","mapping","other_model","remove_self_loops","to_simple_graph"],
        "plot_average_degree" : ["plot_degree"],
        "plot_contact_matrix_heatmap" : ["plot_heatmap"],
        "plot_histogram_null_model" : ["plot_diff_scales", "plot_null_model"],
        "plot_probability_distribution" : ["plot_contact_duration","plot_triangle_duration","plot_inter_duration"]}

    next_list = []
    for key, value in dictionary3.items():
        for i in liste:
            if i in value:
                next_list.append(key)

    next_list = list(set(next_list))

    print("Affected functions are:")
    for i in liste:
        print(i)

    print("Affected methods are: ")
    for i in next_list:
        print(i)

#check_which_methods_are_affected(dictionary2)