import numpy as np


def calculate_contact_duration(Data, bins=None):
    """Calculates the probabilitys for the contact duration

    Calculates the probabilities for having a face-to-face contact for the different times delta T

    Parameters
    ----------
    Data: Data
        Contains a dataframe with the tij-data from the data set. Might also contain metadata.
    bins: optional: int, default: None
        Amount of bins that are used to calculate the probabilities based on a histogram.

    Returns
    -------
    x_y_list: List
        A list with two lists. The first list contains the probabilities for the y-axis and the second list contains
        the contact duration delta T
    delta_t_list: list
        Contains all the calculated $\delta t$ values for the contact duration of the used data set.

    References
    ----------
    .. [1] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics
           of Person-to-Person Interactions from Distributed RFID Sensor Networks. PLOS ONE

    Examples
    ----------

    >>> attr_list = ["ID", "Age", "Sex"]
    >>> test_df = Data(path_tij="face2face/data/Test/tij_test.dat", separator_tij="\t",
    >>>               path_meta="face2face/data/Test/meta_test.dat", separator_meta="\t",
    >>>               meta_attr_list=attr_list)
    >>> y_x_list, delta_t_list = calculate_contact_duration(test_df)
    >>> print(y_x_List[0])
    [0.45454545454545453, 0.2727272727272727, 0.13636363636363635, 0.13636363636363635]
    >>> print(y_x_list[1])
    [20, 40, 60, 80]

    See Also
    ---------
    face2face.statistics.distribution.calculate_triangle_duration
    face2face.statistics.distribution.calculate_inter_contact_duration

    """

    tij_data_sorted = Data.interaction.sort_values(by=["i", "j"])

    tij_data_sorted["diff"] = tij_data_sorted.groupby(["i", "j"])["Time"].diff()

    marker_list = []
    for key, value in tij_data_sorted.iterrows():
        if value["diff"] > 20:
            marker_list.append(1)
        else:
            marker_list.append(0)

    tij_data_sorted["Marker"] = marker_list
    tij_data_sorted["Ind"] = tij_data_sorted["Marker"].cumsum()

    tij_data_sorted = tij_data_sorted.groupby(["Ind", "i", "j"]).size().reset_index(name="Number")

    delta_t_list = []
    for key, value in tij_data_sorted.iterrows():
        delta_t = value["Number"] * 20
        delta_t_list.append(delta_t)

    if bins is None:
        bins = 10**np.linspace(np.log10(min(delta_t_list)), np.log10(max(delta_t_list)), 50)
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)
    else:
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)

    y_probability = y_probability[:-1]
    x_y_list = [list(x_delta_t), list(y_probability)]

    return x_y_list, delta_t_list


def calculate_triangle_duration(Data, bins=None):
    r"""Calculates the probabilities for the contact duration between triangle constellations

        Calculates the probability how long a triangle constellation lasts.

        Parameters
        ----------
        Data.interaction: Data
            Contains a dataframe with the tij-data from the dataset

        Returns
        -------
        x_y_list: List
            A list with two lists. The first list contains the probabilitys for the y-axis and the second list contains
            the triangle duration delta T
        delta_t_list: list
            Contains all the calculated $\delta t$ values for the contact duration of the used data set.

        References
        ----------
        .. [1] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics of Person-to-Person
               Interactions from Distributed RFID Sensor Networks. PLOS ONE

        Examples
        ----------
        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="face2face/data/Test/tij_test.dat", separator_tij="\\t",
        >>>               path_meta="face2face/data/Test/meta_test.dat", separator_meta="\\t",
        >>>               meta_attr_list=attr_list)
        >>> y_x_list, delta_t_list = calculate_triangle_duration(test_df)
        >>> print(y_x_list[0])
        [0.42857142857142855, 0.2857142857142857, 0.14285714285714285, 0.14285714285714285]
        >>> print(y_x_list[1])
        [20, 40, 60, 80]

        See Also
        ---------
        face2face.statistics.distribution.calculate_contact_duration
        face2face.statistics.distribution.calculate_inter_contact_duration

        """
    df_merge_1 = Data.interaction.merge(Data.interaction, left_on=["Time", "i"], right_on=["Time", "j"])
    df_merge_2 = df_merge_1.merge(Data.interaction, left_on=["Time"], right_on=["Time"])

    df_filter_triangle = df_merge_2[(df_merge_2["i_x"] == df_merge_2["j_y"])
                                    & (df_merge_2["j_x"] == df_merge_2["j"])
                                    & (df_merge_2["i_y"] == df_merge_2["i"])]

    df_no_duplicates = df_filter_triangle.drop_duplicates(keep="first")

    df_no_duplicates["Diff"] = df_no_duplicates.groupby(["i_x", "j_x", "i_y"])["Time"].diff()

    marker_list = []
    for key, value in df_no_duplicates.iterrows():
        if value["Diff"] == 20:
            marker_list.append(0)
        elif value["Diff"] > 20:
            marker_list.append(1)
        else:
            marker_list.append(0)
    df_no_duplicates["Marker"] = marker_list
    df_no_duplicates["Ind"] = df_no_duplicates["Marker"].cumsum()

    df_merge_dd_gb = df_no_duplicates.groupby(["Ind", "i_x", "j_x", "i_y"]) \
        .size().reset_index(name="Number")

    delta_t_list = []
    for key, value in df_merge_dd_gb.iterrows():
        if value["Number"] == 1:
            delta_t = 20
            delta_t_list.append(delta_t)
        elif value["Number"] > 1:
            delta_t = value["Number"] * 20
            delta_t_list.append(delta_t)

    if bins is None:
        bins = 10**np.linspace(np.log10(min(delta_t_list)), np.log10(max(delta_t_list)), 50)
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)
    else:
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)

    y_probability = y_probability[:-1]
    x_y_list = [list(x_delta_t), list(y_probability)]

    return x_y_list, delta_t_list


def calculate_inter_contact_duration(Data, bins=None):
    r"""Calculates the probabilities for the inter-contact duration

        Calculates the probability for the inter-contact duration delta T of three distinct persons.

        Parameters
        ----------
        Data.interaction: Data
            Contains a dataframe with the tij-data from the data set

        Returns
        -------
        x_y_list: List
            A list with two lists. The first list contains the probabilities for the y-axis and the second list contains
            the inter-contact duration tAC-tAB
        delta_t_list: list
            Contains all the calculated $\delta t$ values for the contact duration of the used data set.

        References
        ----------

        .. [1] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics of Person-to-Person
               Interactions from Distributed RFID Sensor Networks. PLOS ONE


        Examples
        ---------
        For this small example data set we fixed the bins for this function. This is not necessary for the normal usage.

        >>> attr_list = ["ID", "Age", "Sex"]
        >>> test_df = Data(path_tij="face2face/data/Test/tij_test.dat", separator_tij="\t",
        >>>               path_meta="face2face/data/Test/meta_test.dat", separator_meta="\t",
        >>>               meta_attr_list=attr_list)
        >>> bins = [20, 40, 60, 80]
        >>> x_y_list, delta_t_list = calculate_inter_contact_duration(test_df, bins=bins)
        >>> print(x_y_list[0])
        [0.0, 0.049999999999999996, 0.0]
        >>> print(x_y_list[1])
        [20, 40, 60]

        See Also
        ---------
        face2face.statistics.distribution.calculate_contact_duration
        face2face.statistics.distribution.calculate_triangle_duration

        """

    individuals = list(set(list(Data.interaction.i) + list(Data.interaction.j)))
    delta_t_list = np.array([])
    for ind in individuals:
        time_stamp = Data.interaction[(Data.interaction.i == ind) | (Data.interaction.j == ind)].Time.values
        diff = time_stamp[1:] - time_stamp[:-1]
        delta_t_list = np.append(delta_t_list, diff[diff > 20])

    if bins is None:
        bins = 10**np.linspace(np.log10(min(delta_t_list)), np.log10(max(delta_t_list)), 50)
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)
    else:
        x_delta_t, y_probability = np.histogram(delta_t_list, bins=bins, density=True)

    y_probability = y_probability[:-1]
    x_y_list = [list(x_delta_t), list(y_probability)]
    return x_y_list, delta_t_list
