import math

import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import pandas as pd

from face2face.imports.load_all_data import Data
from face2face.statistics.null_modell import configuration_model_label_z_score_mixing_matrix
from face2face.statistics.null_modell import shuffle_label_z_score_mixing_matrix


def plot_diff_scales(ax1, x_value, y_value, x2_value, y2_value, title):

    """Creates the subplots

       Creates the subplots for every attribute combination and defines the parameters for their visualization

       Parameters
       ----------
       ax1: axes
           Basic axes parameter for the figure without any layout information yet
       x_value: list
           List with the amount of edges between the two attribute-values for every iteration of the null model
           functions.
       y_value:
           Frequency of the occurrence of the amount of edges for every iteration
       x2_value: float
           Average z-score for this attribute-value combination
       y2_value: float
           Maximum value of y_value list for a better representation of the z-score
       title: list
           Contains the two attribute-values that gets compared in this iteration

       Returns
       -------
       ax1: axes
           Parameter for the visualization of the edge-frequency between the two attribute-values
       ax2: axes
           Parameter for the visualization of the z-score for the two attribute-values
       """

    ax1.title.set_text(str(title))
    ax2 = ax1.twiny()
    ax1.bar(x2_value, y2_value, color="#0B6C11", width=0.08, align="center")
    ax1.set_ylabel('Frequency', color="k")
    ax1.set_xlim(-5, 5)
    ax1.tick_params(axis='x', labelcolor="k")
    ax2.bar(x_value, y_value, color="#23D42F", align="center")
    ax2.set_ylabel('Frequency')
    ax1.set_xlabel('z-score')

    return ax1, ax2


def plot_null_model_subplots(Data, runs, label="type", shuffle_label=False, force_simple_graph=False,
                             model="configuration_model"):

    """Creates a figure for all attribute-value combinations

       Creates and plots a figure with subplots for every attribute-value combination. Every subplot shows the frequency
       of the amount of edges for the given attribute-value combination and the average z-score.

       Parameters
       ----------
       Data: Data
           Data Object that contains Tij- and Metadata for a data set.
       runs: int
           The amount of times the function should be executed. It's a heuristic approach, so the more the runs the
           better might be the result
       label: str
           A string that tells the function for which attribute the contact matrix should be made.
       shuffle_label: bool
           Gives the option to extend the null model by randomizing the node attributes.
       force_simple_graph: bool
           Deletes parallel- and selfedges that can occur by using the networkx "configuration_model"-function if True.
       model: str
           Defines which null model should be used. Possible Values: "configuration_model", "random_identities"

       Returns
       -------
       None

       See Also
       ---------
       face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix
       face2face.statistics.null_modell.shuffle_label_z_score_mixing_matrix
       face2face.visualization.plot_contact_matrix_heatmap.plot_cm_heatmap
       """

    if model == "configuration_model":
        contact_matrix, matrices, data_mixing_matrix, matrices2 = configuration_model_label_z_score_mixing_matrix(
            Data, runs=runs, label=label, shuffle_label=shuffle_label, force_simple_graph=force_simple_graph)

    elif model == "random_identities":
        contact_matrix, matrices2 = shuffle_label_z_score_mixing_matrix(Data, runs=runs, label=label)

    contact_matrix_list = contact_matrix.ravel().tolist()

    abs_edges_lists = []
    for i in matrices2:
        abs_edges_lists.append(i.ravel().tolist())

    abs_edges_df = pd.DataFrame(abs_edges_lists)

    frequency_df_list = []
    for column in abs_edges_df:
        frequency_df = abs_edges_df.groupby(column).size().reset_index(name="Frequency")
        frequency_df_list.append(frequency_df)

    dimension = int(math.sqrt(len(contact_matrix_list)))
    list_plot_title = []
    for i in range(dimension):
        for j in range(dimension):
            list_plot_title.append([i, j])

    i = 0
    fig, axs = plt.subplots(dimension, dimension, figsize=(5, 4))

    for row in axs:
        for ax in row:
            ax1, ax2 = plot_diff_scales(ax, frequency_df_list[i][i], frequency_df_list[i]["Frequency"],
                                        contact_matrix_list[i], max(frequency_df_list[i]["Frequency"]),
                                        list_plot_title[i])
            i += 1

    plt.tight_layout()
    plt.show()

