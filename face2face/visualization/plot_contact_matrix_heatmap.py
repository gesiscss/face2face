import seaborn as sns
import matplotlib.pylab as plt
from face2face.statistics.null_modell import check_bonferroni_correction


def plot_cm_heatmap(contact_matrix):

    """Plots a heatmap for a given contact matrix

       Plots the contact matrix for a choosen attribute. The heatmap ncludes a bonferroni correction which is shown by
       a white * if a value is an outlier.

        Parameters
        ----------
        contact_matrix : list
            A matrixlike List of lists that contains the z-scores for a given attribute.

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
        face2face.statistics.null_modell.configuration_model_label_z_score_mixing_matrix
        face2face.statistics.null_modell.shuffle_label_z_score_mixing_matrix
        face2face.visualization.plot_histogram_null_model.plot_null_model_subplots

    """
    annotation_list = check_bonferroni_correction(contact_matrix)
    ax = sns.heatmap(contact_matrix, annot=annotation_list, fmt='', cmap="bwr", linewidth=0.5)
    plt.show()

    return None