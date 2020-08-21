import matplotlib.pyplot as plt

plt.rcParams.update(plt.rcParamsDefault)


def plot_contact_duration(list_x_y, color_list, marker_list, label_list):
    r"""Plots the probability distribution of the contact duration

        Plots the values of the probability on the y-axis and the values of the contact duration Delta T on the x-axis.

        Parameters
        ----------
        list_x_y : list
            Contains the output of the "calculate_contact_duration"-function, which is a list of the y-values
            (probabilities) and the x-values (contact durations). You can add multiple lists of the
            "calculate_contact_duration"-function in the list_x_y to compare them in the graph.

        color_list: list
            Should contain a color for every list in list_x_y to define the color of the markers for the visualisation.

        marker_list: list
            Should contain a marker for every list in list_x_y to define the shape of the data points.

        label_list: list
            Should contain a string label for every list in list_x_y to create a comprehensible legend.

        Returns
        -------
        None

        References
        ----------
        [1] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics of Person-to-Person
        Interactions from Distributed RFID Sensor Networks. PLOS ONE 5(7): e11596.
        https://doi.org/10.1371/journal.pone.0011596

        See Also
        ---------
        face2face.statistics.distribution.calculate_contact_duration
        """
    for i in range(len(list_x_y)):
        plt.plot(list_x_y[i][1], list_x_y[i][0], marker_list[i], color=color_list[i], label=label_list[i])
        plt.ylabel("Probability ($\Delta$t)")
        plt.xlabel("Contact duration $\Delta$t (seconds)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Probability Distribution of duration of contacts")
        x_vertical_lines = [[60, 70,"1 minute"], [1800,2000,"30 minutes"]]
        for xc in x_vertical_lines:
            plt.axvline(x=xc[0],  color='k', linestyle='--')
            plt.text(x=xc[1], y=min(list_x_y[0][0]) + 0.0005, s=xc[2], rotation=90)
        plt.legend(loc="upper right")
    plt.show()

    return None


def plot_triangle_duration(list_x_y, color_list, marker_list, label_list):
    r"""Plots the probability distribution of the triangle duration

        Plots the values of the probability on the y-axis and the values of the triangle duration Delta T on the x-axis.

        Parameters
        ----------
        list_x_y : list
            Contains the output of the "calculate_triangle_duration"-function, which is a list of the y-values
            (probabilities) and the x-values (triangle durations). You can add multiple lists of the
            "calculate_triangle_duration"-function in the list_x_y to compare them in the graph.

        color_list: list
            Should contain a color for every list in list_x_y to define the color of the markers for the visualization.

        marker_list: list
            Should contain a marker for every list in list_x_y to define the shape of the data points.
        label_list: list
            Should contain a string label for every list in list_x_y to create a comprehensible legend.

        Returns
        -------
        None

        References
        ----------
        [2] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics of Person-to-Person
        Interactions from Distributed RFID Sensor Networks. PLOS ONE 5(7): e11596.
        https://doi.org/10.1371/journal.pone.0011596

        See Also
        ---------
        face2face.statistics.distribution.calculate_triangle_duration

        """

    for i in range(len(list_x_y)):
        plt.plot(list_x_y[i][1], list_x_y[i][0], marker_list[i], color=color_list[i], label=label_list[i])
        plt.ylabel("Probability($\Delta$t)")
        plt.xlabel("Triangle duration $\Delta$t (seconds)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Probability Distribution of the duration of triangles")
        x_vertical_lines = [[60, 70, "1 minute"], [1800, 2000, "30 minutes"]]
        for xc in x_vertical_lines:
            plt.axvline(x=xc[0], color='k', linestyle='--')
            plt.text(x=xc[1], y=min(list_x_y[0][0]) + 0.0005, s=xc[2], rotation=90)
        plt.legend(loc="upper right")
    plt.show()

    return None


def plot_inter_contact_duration(list_x_y, color_list, marker_list, label_list):
    r"""Plots the probability distribution for the inter-contact duration

        Plots the values of the probability on the y-axis and the values of the inter-contact duration Delta T
        on the x-axis.

        Parameters
        ----------
        list_x_y : list
            Contains the output of the "calculate_inter_contact_duration"-function, which is a list of the y-values
            (probabilities) and the x-values (inter-contact durations). You can add multiple lists of the
            "calculate_inter_contact_duration"-function in the list_x_y to compare them in the graph.

        color_list: list
            Should contain a color for every list in list_x_y to define the color of the markers for the visualisation.

        marker_list: list
            Should contain a marker for every list in list_x_y to define the shape of the data points.
        label_list: list
            Should contain a string label for every list in list_x_y to create a comprehensible legend.

        Returns
        -------
        None

        References
        ----------
        [2] Cattuto C, Van den Broeck W, Barrat A, Colizza V, Pinton JF, et al. (2010) Dynamics of Person-to-Person
        Interactions from Distributed RFID Sensor Networks. PLOS ONE 5(7): e11596.
        https://doi.org/10.1371/journal.pone.0011596

        See Also
        ---------
        face2face.statistics.distribution.calculate_inter_contact_duration

        """

    for i in range(len(list_x_y)):
        plt.plot(list_x_y[i][1], list_x_y[i][0],marker_list[i], color=color_list[i], label=label_list[i])
        plt.ylabel("Probability ($\Delta$t)")
        plt.xlabel("Inter-contact duration tAC-tAB (seconds)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Probability Distribution of the time intervals between consecutive contacts")
        x_vertical_lines = [[60, 70, "1 minute"], [1800, 2000, "30 minutes"]]
        for xc in x_vertical_lines:
            plt.axvline(x=xc[0], color='k', linestyle='--')
            plt.text(x=xc[1], y=min(list_x_y[0][0]) + 0.0005, s=xc[2], rotation=90)
        plt.legend(loc="upper right")
    plt.show()

    return None
