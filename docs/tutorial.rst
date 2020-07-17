Tutorial
========

.. currentmodule:: sociopatterns

This guide should help you to get started with this package.


Import Tij- and Metadata as Data Object
----------------------------------------

Import predefined datasets as Data Object.

.. code-block:: python

	>>> import sociopatterns as sp
	>>> df = sp.Data()
	
A :class:`Data` is a collection of one or two pandas dataframes. It always contains a tij-dataframe, but it can also contain a metadata dataframe. You can use the whole Data-Object as Parameter for all functions where you use tij-dataframes or metadata-dataframes.
If you want to access one of the two dataframes of the Data-Object, you can access it like this.

.. code-block:: python

	>>> df_tij = Data.interaction
	>>> df_meta = Data.metadata


Create different Networks
--------------------------

With the :class:`Data` you can create different kind of networks.

.. code-block:: python
	
	>>> full_network = create_network_from_data(Data)
	>>> hopping_network = hopping_time_networks(Data, minute= )
	>>> sliding_network = sliding_time_networks(Data, slide= ,interval= )
	>>> event_time_network = event_time_networks(Data, events)


Notebook Tutorials in Git
--------------------------

To get an overview of the functions that are included in this library you can work through the following tutorials to get an idea how to use these functions. 

If you are already experienced in using python and especially librarys like pandas, numpy and networkX you can skip the beginner tutorials "01_tutorial_exploring_the_data" and "02_tutorial_first_functions".

If you are new to Python or this librarys or you want to refresh your knowledge you can start with the beginner tutorials.


Beginner Tutorials
^^^^^^^^^^^^^^^^^^^^

01_tutorial_exploring_the_data
"""""""""""""""""""""""""""""""

This tutorial includes small tasks with functions of pandas that are also used for the functions in this library. The tasks should give you an idea on the functions that are used for this library like "groupyby", "merge" etc. 

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/01_tutorial_exploring_the_data.ipynb>`_

02_tutorial_first_functions
"""""""""""""""""""""""""""""

This tutorial explains the basics about the functions that are implemented in the distribution and the average_degree methods. It allows you to get an idea on how to use the pandas and python tools that you saw in the previous tutorial.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/02_tutorial_first_functions.ipynb>`_


Sociopatterns Tutorials
^^^^^^^^^^^^^^^^^^^^^^^^

import_data_set
""""""""""""""""

The tutorial "import_data_set" tells you about every way that you can import predefined or your own datasets to make them useable in this library. 

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/import_data_set.ipynb>`_


avg_degree
""""""""""

This tutorial shows how to use the packages about the measurement and the visualization of the (average) degree from a given dataset.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/avg_degree.ipynb>`_


dynamic_network_analyses
""""""""""""""""""""""""""

This tutorial shows you the functions to create different kinds of networks with this library. It also shows you the implemented functions for measurements of the network for a first decisive loook on a given network.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/dynamic_network_analyses.ipynb>`_

homophily
""""""""""""

This tutorial shows you how to apply two kinds of null models on a dataset to get a contact matrix that tells you the deviation from the mean for every pair of attribute values for a given attribute. It also shows you how apply the bonferroni correction and how to plot this contact matrix as a heatmap.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/homophily.ipynb>`_


probability_distribution_contact_duration
""""""""""""""""""""""""""""""""""""""""""

This tutorial shows you how to analyze the different kinds of contact durations in a dataset and also how to plot it.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/probability_distribution_contact_duration.ipynb>`_

Statistical characterization
"""""""""""""""""""""""""""""""

This tutorial should give you basic instructions on how to use the powerlaw package to analyze the distribution of the contact duration functions from this library.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/Statistical_characterization.ipynb>`_


How_to_use_statistical_characterization
""""""""""""""""""""""""""""""""""""""""""

This tutorial requires the knowledge from the previous Tutorial. This tutorial should teach you how to use the packages powerlaw and sociopatterns, to determine reasonable parameters, find the best fitting distribution for the data set and how to visualize it.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/How_to_use_statistical_characterization.ipynb>`_