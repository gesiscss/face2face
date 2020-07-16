import matplotlib.pyplot as plt


def plot_avg_degree_group(attr_degree_list, measures):
    r"""Plot boxplot for the average degrees

        Plots the average degree for every attribute in a boxplot. It also shows the average over all degrees and the
        standard deviation.

        Parameters
        ----------
        attr_degree_list : list
            Contains lists with all degrees for all attribute values. You can get this list with the "group_list_degree"
            function.
        measures : list
            Contains the global average degree, the variance and the standard deviation over all attributes.
            You can get this values by using the "global_avg_var_std"- function.

        Returns
        -------
        None

        Notes
        -----

        References
        ------------
        [1] Génois, Mathieu & Zens, Maria & Lechner, Clemens & Rammstedt, Beatrice & Strohmaier, Markus. (2019). Building connections: How scientists meet each other during a conference.

        See Also
        ----------
        face2face.statistics.average_degree.group_list_degree
        face2face.statistics.average_degree.global_avg_var_std

    """

    x_list = []
    label_list = []
    for i in attr_degree_list:
        x_list.append(i[2])
        label_list.append(str(i[0]) + " " + str(str(i[1])))

    fig, ax = plt.subplots()
    ax.set_title('Average degree for the attributes of the different groups')
    plt.axhline(measures[0], color='black', linestyle='solid', label='AvgMean', linewidth=1)
    plt.axhspan(measures[0], measures[0] - measures[1] * (1 / 3), color="lightcoral")
    plt.axhspan(measures[0] - measures[1] * (1 / 3), measures[0] - measures[1] * (2 / 3), color="indianred")
    plt.axhspan(measures[0] - measures[1] * (2 / 3), measures[0] - measures[1], color="brown")

    plt.axhspan(measures[0], measures[0] + measures[1] * (1 / 3), color="lightcoral")
    plt.axhspan(measures[0] + measures[1] * (1 / 3), measures[0] + measures[1] * (2 / 3), color="indianred")
    plt.axhspan(measures[0] + measures[1] * (2 / 3), measures[0] + measures[1], color="brown")
    ax.boxplot(x_list, vert=True, labels=label_list, showfliers=False, notch=False)
    plt.xticks(rotation=90)
    plt.ylabel("Average Degree")
    plt.xlabel("Attributes from the different groups")
    plt.show()

    return None
