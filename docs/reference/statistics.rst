Statistics
==========

.. currentmodule:: face2face

Distribution
------------

.. automodule:: face2face.statistics.distribution


.. autosummary::
	:toctree: generated/
	
	calculate_contact_duration
	calculate_triangle_duration
	calculate_inter_contact_duration

	
Null Model
----------

.. automodule:: face2face.statistics.null_modell

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

.. automodule:: face2face.statistics.average_degree

.. autosummary::
	:toctree: generated/
	
	avg_degree_attr
	group_list_degree
	global_avg_var_std
	
Network Measurements
---------------------

.. automodule:: face2face.statistics.network_quantities

.. autosummary::
	:toctree: generated/
	
	calculating_number_of_edges_nodes
	mean_degree_network
	variance_std_network
	average_path_length_network
	clustering_coefficient

Check distribution
-------------------

.. automodule:: face2face.statistics.check_distribution

.. autosummary::
	:toctree: generated/
	
	search_best_fit_distribution
	get_best_fit_distribution
	distribution_tupel_combinations
	