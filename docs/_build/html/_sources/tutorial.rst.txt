Tutorial
========

.. currentmodule:: face2face

This guide should help you to get started with this package.


Import Tij- and Metadata as Data Object
----------------------------------------

Import predefined datasets as Data Object. The Data Class gives you multiple import options. You can import already predefined data sets included in this toolbox, you can import your own data sets or you can import dataframes which you have created. To learn more about the input parameter of this Class check out the Online documentation or the tutorial "import_data_set". For this example we import the predefined "WS16" data set as described below.

.. code-block:: python

	>>> import face2face as f2f
	>>> df = f2f.Data("WS16")
	
A :class:`Data` object is a collection of one or two pandas dataframes. It always contains a tij-dataframe, but it can also contain a metadata dataframe. You can use the whole Data-Object as Parameter for all functions where you use tij-dataframes or metadata-dataframes.
If you want to access one of the two dataframes of the Data-Object, you can access it like this.

.. code-block:: python

	>>> df_tij = Data.interaction
	>>> df_meta = Data.metadata


Create different Networks
--------------------------

With the :class:`Data` you can create different kind of networks.

.. code-block:: python
	
	>>> full_network = f2f.create_network_from_data(Data)
	>>> hopping_network = f2f.hopping_time_networks(Data, minute= )
	>>> sliding_network = f2f.sliding_time_networks(Data, slide= ,interval= )
	>>> event_time_network = f2f.event_time_networks(Data, events)


Notebook Tutorials in Git
--------------------------

To get an overview of the functions that are included in this toolbox you can work through the following tutorials to get an idea how to use these functions. 

If you are already experienced in using python and especially librarys like pandas, numpy and networkX you can skip the beginner tutorials "01_tutorial_exploring_the_data" and "02_tutorial_first_functions".

If you are new to Python or this librarys or you want to refresh your knowledge you can start with the beginner tutorials.


Beginner Tutorials
^^^^^^^^^^^^^^^^^^^^

01_tutorial_exploring_the_data
"""""""""""""""""""""""""""""""

This tutorial includes small tasks with functions of pandas that are also used for the functions in this toolbox. The tasks should give you an idea on the functions that are used for this toolbox like "groupby", "merge" etc. 

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/01_tutorial_exploring_the_data.ipynb>`_

02_tutorial_first_functions
"""""""""""""""""""""""""""""

This tutorial explains the basics about the functions that are implemented in the distribution and the average_degree methods. It allows you to get an idea on how to use the pandas and python tools that you saw in the previous tutorial. In this tutorial, the functions for the calculations of the probabilities for the three different interaction durations that are part of this library are explained.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/02_tutorial_first_functions.ipynb>`_

03_tutorial_first_functions
"""""""""""""""""""""""""""""

This tutorial explains the basics about the functions that are implemented in the distribution and the average_degree methods. It allows you to get an idea on how to use the pandas and python tools that you saw in the previous tutorial. In this tutorial, the functions for the calculations of the average degree for the different groups and subgroups of a data set are explained.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/03_tutorial_first_functions.ipynb>`_

face2face Tutorials
^^^^^^^^^^^^^^^^^^^^^^^^

import_data_set   
""""""""""""""""

The tutorial "import_data_set" tells you about every way that you can import predefined or your own datasets to make them useable in this toolbox. 

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/import_data_set.ipynb>`_


avg_degree
""""""""""

This tutorial shows how to use the packages about the measurement and the visualization of the (average) degree from a given dataset.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/avg_degree.ipynb>`_


dynamic_network_analyses
""""""""""""""""""""""""""

This tutorial shows you the functions to create different kinds of networks with this toolbox. It also shows you the implemented functions for measurements of the network for a first decisive loook on a given network.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/dynamic_network_analyses.ipynb>`_

homophily
""""""""""""

This tutorial shows you how to analyse the data sets in terms of the homophily. The homophily describes the tendency of individuals to be more attracted to get in contact with other people witch share related (socio-demographic) attributes. 

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/homophily.ipynb>`_


probability_distribution_contact_duration
""""""""""""""""""""""""""""""""""""""""""

This tutorial shows you how to analyze the different kinds of contact durations in a dataset and also how to plot it.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/probability_distribution_contact_duration.ipynb>`_

Statistical characterization
"""""""""""""""""""""""""""""""

This tutorial should give you basic instructions on how to use the powerlaw package to analyze the distribution of the contact duration functions from this toolbox.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/Statistical_characterization.ipynb>`_


How_to_use_statistical_characterization
""""""""""""""""""""""""""""""""""""""""""

This tutorial requires the knowledge from the previous Tutorial. This tutorial should teach you how to use the packages powerlaw and face2face, to determine reasonable parameters, find the best fitting distribution for the data set and how to visualize it.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/How_to_use_statistical_characterization.ipynb>`_

Paper
"""""""

This tutorial shortly describes how the plots for the paper "The statistical characteristics of face-to-face interaction" were made so that they are more comprenhensible for people how read the paper and are interested.

To get to the tutorial click `here <https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit/blob/development/tutorial/Paper.ipynb>`_