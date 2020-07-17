Statistics
==========

.. currentmodule:: sociopatterns

Distribution
------------

.. automodule:: sociopatterns.statistics.distribution


.. autosummary::
	:toctree: generated/
	
	calculate_contact_duration
	calculate_triangle_duration
	calculate_inter_contact_duration

	
Null Model
----------

.. automodule:: sociopatterns.statistics.null_modell

.. autosummary::
	:toctree: generated/
	
	check_bonferroni_correction
	mapping_function
	configuration_model_label_z_score_mixing_matrix
	shuffle_label_z_score_mixing_matrix
	remove_self_loops
	to_simple_graph
	   
Average Degree
----------------

.. automodule:: sociopatterns.statistics.average_degree

.. autosummary::
	:toctree: generated/
	
	new_avg_degree_attr
	avg_degree_attr
	new_group_list_degree
	group_list_degree
	global_avg_var_std
	
Network Measurements
---------------------

.. automodule:: sociopatterns.statistics.calculating_multiple_measurements_for_a_network

.. autosummary::
	:toctree: generated/
	
	calculating_number_of_edges_nodes
	mean_degree_network
	variance_std_network
	average_path_length_network
	clustering_coefficient

Check distribution
-------------------

.. automodule:: sociopatterns.statistics.check_distribution

.. autosummary::
	:toctree: generated/
	
	search_best_fit_distribution
	get_best_fit_distribution
	distribution_tupel_combinations
	