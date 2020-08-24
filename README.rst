.. image:: https://notebooks.gesis.org/binder/badge.svg
   :target: https://notebooks.gesis.org/binder/v2/gh/gesiscss/face-to-face-interaction-analysis-toolkit/development?urlpath=lab/tree/tutorial/import_data_set.ipynb

******************************************
Face-to-face interaction analysis toolkit
******************************************

Face2face is a toolbox that contains multiple methods for the basic analysis of sociopatterns data sets and networks.

- **Homepage**: https://gesiscss.github.io/face2face/ 
- **Website of Gesis**: https://www.gesis.org/home

Installation
-------------

You have multiple options for the installation on your local machine.

If you want to become a contributor in this toolbox and you want to apply changes or add new functions to the toolbox you can take a look on the development guide from the website.

If you just want to install the toolbox on your system to work with it, you can do so with:
    
        $ pip install face2face
        
        
Tutorials
----------

If you are new to this library and you want to learn about how to use the included methods or you want to learn how they work you can use the tutorials. For a short description of the different tutorials you can find more information in the tutorial README [Tutorial README](/tutorial/README.md). If you want to test the tutorials right now you can click on the binder badge on top of this README.md to open the tutorials in the Gesis Notebooks. 

`Here <https://github.com/gesiscss/face2face/tree/master/tutorial>`_ you get to the tutorial folder.

Short summary
--------------

With the methods from the import module you can import your own tij- and metadata data sets or you can use predefined data sets which are included in the installed library. With the Data Object you created with your or the predefined data sets you can directly start with the analysis of the probability for different contact durations and visualize them. You can also use the Object to create a network and analyze this network in terms of basic key figures about the underlying network. Furthermore you can use this library to analyze and visualize the homophily of the given data set. 

Current State
--------------

The face2face toolbox at its current state is an alpha version. If you find any bugs or you have suggestions about how to extend the toolbox with useful new functionalities please let us know by creating a new issue thread on our `GitHub Page <https://github.com/gesiscss/face2face/issues>`_ or contribute a fix or additional methods by yourself as described in the developer guide in the online documentation.