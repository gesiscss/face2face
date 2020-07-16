import powerlaw
from face2face.imports.load_all_data import Data
from face2face.statistics.distribution import calculate_contact_duration


def search_best_fit_distribution(data, xmin=None, xmax=None, extend_data=None, discret=False, approximation_method=None,
                                 distance_measurement_method="D", sigma_threshold=None, parameter_range=None):

    """Searches the best fitting distribution

        Creates a fit object and compares every distribution for the given data set to find the best fitting one.

        Parameters
        ----------
        data: list
            A list of multiple values
        xmin: float, default: None
            Set xmin to localize the part of the data set that you want to analyze.
        xmax: float, default: None
            Set xmax to localize the port of the data set that you you want to analyze.
        extend_data: int, default: None
            Can be used to extend the data set with random generated data points.
        discret: bool, default: False
            Must be set if data set is discret, because discrete versions of probability distributions are calculated
            differently.
        approximation_method: str, int
            Different approximation methods for discret data sets. Possible values: "round", "xmax" or an integer.
        distance_measurement_method: str, default: "D".
            Changes the measurement method to calculated the minimized distance between the empirical data and the
            distribution. Possible Values: "D","V","Asquare".
        sigma_threshold: float, default: None
            Can be set to add a constraint for the maximum sigma.
        parameter_range: dict, default: None
            Can be set to limit multiple parameters for the distributions.

        Returns
        -------
        Fit: Fit Object
            Contains the created Fit Object to use it for plotting as PDF, CDF or CCDF.
        tupel_list: list
            Contains tupels with the comparison of every distribution that is included in the package.


        See Also
        ---------
        face2face.statistics.distribution.calculate_contact_duration
        face2face.statistics.distribution.calculate_triangle_duration
        face2face.statistics.distribution.calculate_inter_contact_duration

        """

    fit = powerlaw.Fit(data, xmin=xmin, xmax=xmax, discret=discret, discrete_approximation=approximation_method,
                       sigma_threshold=sigma_threshold, parameter_range=parameter_range
                       , xmin_distance=distance_measurement_method)
    if extend_data is not None:
        fit = fit.power_law.generate_random(extend_data)

    if sigma_threshold is not None:
        if fit.noise_flag:
            print("Sigma Treshold was too small to get a result")
        else:
            print("Sigma Treshold was applied successfully")

    distribution_list = ["power_law", "lognormal", "exponential", "truncated_power_law", "stretched_exponential",
                         "lognormal_positive"]

    best_fit = get_best_fit_distribution(distribution_list, fit)
    print("The best fitting distribution is " + best_fit[0])

    tupel_list = distribution_tupel_combinations(distribution_list, fit)

    return fit, tupel_list, best_fit


def get_best_fit_distribution(distribution_list, fit):

    """Searches the best fitting distribution

        Tests the included distributions recursivwly against each other to get the best fit object.

        Parameters
        ----------
        distribution_list: list
            Contains a list of strings with every distribution included in this package.
        fit: Fit object
            Fit objected for the given data set.

        Returns
        -------
        distribution_list: list
            Contains the best fit distribution as a string.

        See Also
        ---------
        face2face.statistics.check_distribution.search_best_fit_distribution
        """

    if len(distribution_list) == 1:
        return distribution_list

    else:
        distribution_list2 = []
        for i in range(1, len(distribution_list)):
            r, p = fit.distribution_compare(distribution_list[i], distribution_list[i - 1], normalized_ratio=True)
            if r > 0:
                if distribution_list[i] not in distribution_list2:
                    distribution_list2.append(distribution_list[i])
            elif r < 0:
                if distribution_list[i - 1] not in distribution_list2:
                    distribution_list2.append(distribution_list[i - 1])
            else:
                if distribution_list[i] not in distribution_list2:
                    distribution_list2.append(distribution_list[i])
                if distribution_list[i - 1] not in distribution_list2:
                    distribution_list2.append(distribution_list[i - 1])
        return get_best_fit_distribution(distribution_list2, fit)


def distribution_tupel_combinations(distribution_list, fit):
    """Searches the best fitting distribution

        Compares every distribution included in this package against each other and returns every combination as a list
        of tupels. The normalized loglikelihood is also included in the tupel.

        Parameters
        ----------
        distribution_list: list
            Contains a list of strings with every distribution included in this package.
        fit: Fit object
            Fit objected for the given data set.

        Returns
        -------
        list_for_distribution_tupels: list
            Contains tupels with the comparison of every distribution that is included in the package.

        See Also
        ---------
        face2face.statistics.check_distribution.search_best_fit_distribution
        """
    list_for_distribution_tupels = []
    for i in range(len(distribution_list)):
        for j in range(len(distribution_list)):
            if i != j:
                r, p = fit.distribution_compare(distribution_list[i], distribution_list[j], normalized_ratio=True)
                if r > 0:
                    if (r, distribution_list[i], distribution_list[j]) or \
                            (r, distribution_list[j], distribution_list[i]) not in list_for_distribution_tupels:
                        distribution_tupel = (r, distribution_list[i], distribution_list[j])
                        list_for_distribution_tupels.append(distribution_tupel)

    return list_for_distribution_tupels


