Install
=======

face2face is Python 3 based toolbox so you need to install a Python 3 IDE if you want to use the toolbox. Below you can see possible sources where you can download a fitting python distribution for Windows.

- `Anaconda <https://www.anaconda.com/download/>`_,
- `Enthought Canopy <https://www.enthought.com/product/canopy>`_,
- `Python(x,y) <http://python-xy.github.io/>`_,
- `WinPython <https://winpython.github.io/>`_, or
- `Pyzo <http://www.pyzo.org/>`_.

When you have set up the python environment you can also think about using an IDE like `PyCharm <https://www.jetbrains.com/de-de/pycharm/download/#section=windows/>`_ to work with.

After you successfully have set up a python 3 environment on your computer you have to make sure that you have the latest ``pip`` version installed. For more information you can check the `Documentation of pip <https://pip.pypa.io/en/stable/installing/>`_.

If you installed the latest ``pip`` version you are able to easily install the ``face2face`` toolbox inside the command prompt.

Install the latest version
------------------------------

Install the latest release of ``face2face`` with ``pip``::

    $ pip install face2face
	
You can also install ``face2face`` with ``conda``::

	$ conda install face2face

Additional packages
----------------------

The ``face2face`` toolbox is based on a few additional librarys, that are required for the usage of the functions. Below you can see the librarys that you have to install.

- `NumPy <http://www.numpy.org/>`_ 
- `pandas <http://pandas.pydata.org/>`_ 
- `Matplotlib <http://matplotlib.org/>`_ 
- `networkX <https://networkx.github.io/documentation/stable/>`_ 
- `SciPy <https://docs.scipy.org/doc/scipy/reference/index.html>`_
- `seaborn <https://seaborn.pydata.org/>`_ 
- `powerlaw <https://pythonhosted.org/powerlaw/>`_



To install ``face2face`` and all additional packages, do::

    $ pip install face2face

To explicitly install all additional packages, do::

    $ pip install numpy pandas matplotlib networkx scipy seaborn powerlaw

Or, install any additional package (e.g., ``numpy``) individually::

    $ pip install numpy

If you want to use multiple librarys on your environment, which use similar librarys like ``pandas`` or ``numpy``, but they require different versions you can use the functions from the ``check_compatiblity`` method to find out if the 
versions of the required librarys already contain or still contain the functions, that are needed in the ``face2face`` toolbox. To get the maximum backward and forward compatibility there are no specific versions required for the packages that are used for this toolbox,
but instead you can use this tool as an assistant to find out which parts of this toolbox won't work with the currently installed package versions. So you can decide if you need the affected functions and if the function tells you which functions in the installed package versions are missing you have
a good hint to find the version you need to make this functions work. 


