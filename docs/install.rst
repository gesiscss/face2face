Install
=======

face2face requires a Python Version >= 3.6.1 for the used librarys inside this one. If you have no python environment on your computer yet you can check the following instruction guide for the installation. `scientific Python stack <https://scipy.org/install.html>`_.


.. note::
   If you are on Windows and want to install optional packages (e.g., `scipy`),
   then you will need to install a Python distribution such as
   `Anaconda <https://www.anaconda.com/download/>`_,
   `Enthought Canopy <https://www.enthought.com/product/canopy>`_,
   `Python(x,y) <http://python-xy.github.io/>`_,
   `WinPython <https://winpython.github.io/>`_, or
   `Pyzo <http://www.pyzo.org/>`_.
   If you use one of these Python distribution, please refer to their online
   documentation.
   
Below we assume you have the default Python environment already configured on
your computer and you intend to install ``face2face`` inside of it.  If you want
to create and work with Python virtual environments, please follow instructions
on `venv <https://docs.python.org/3/library/venv.html>`_ and `virtual
environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

First, make sure you have the latest version of ``pip`` (the Python package manager)
installed. If you do not, refer to the `Pip documentation
<https://pip.pypa.io/en/stable/installing/>`_ and install ``pip`` first.


Install the released version
------------------------------

Install the current release of ``face2face`` with ``pip``::

    $ pip install face2face
	
You can also install ``face2face`` with ``conda``::

	$ conda install face2face

Install the development version
------------------------------------

Optional packages
------------------

The following optional packages provide additional functionality.

- `NumPy <http://www.numpy.org/>`_ (>= 1.15.4) provides matrix representation of
  graphs and is used in some graph algorithms for high-performance matrix
  computations.
- `pandas <http://pandas.pydata.org/>`_ (>= 0.23.3) provides a DataFrame, which
  is a tabular data structure with labeled axes.
- `Matplotlib <http://matplotlib.org/>`_ (>= 3.0.2) provides flexible drawing of
  graphs.
- `networkX <https://networkx.github.io/documentation/stable/>`_ (>= >) provides creating and analysing of network graphs.
- `SciPy <https://docs.scipy.org/doc/scipy/reference/index.html>`_ (>= >) provides a collection of mathematical algorithms and convenience functions.
- `seaborn <https://seaborn.pydata.org/>`_ (>=) provides functions to create statistical graphics in python.
- `powerlaw` <https://pythonhosted.org/powerlaw/>`_ () provides functions to find the best fitting distribution for a data set.
- `random` <https://docs.python.org/3/library/random.html>`_ () provides functions to generate pseudo-random numbers.
- `math` <https://docs.python.org/3/library/math.html>`_ () provides mathematical functions.
- `collections` <https://docs.python.org/3/library/collections.html>`_ provides specialized container datatypes as an alternative to Python's built-in containers.


To install ``face2face`` and all optional packages, do::

    $ pip install face2face[all]

To explicitly install all optional packages, do::

    $ pip install numpy pandas matplotlib networkx scipy seaborn powerlaw random math collections

Or, install any optional package (e.g., ``numpy``) individually::

    $ pip install numpy

If you want to use multiple librarys for your project, which use similar librarys like ``pandas`` or ``numpy``, but they require different versions you can use the functions from the ``check_compatiblity`` method to find out if the 
versions of the required packages contain already or still contain the functions, that are needed in the ``face2face`` library. To get the maximum backwards and forward compatibility there are no specific versions required for the packages that are used for this library,
but instead you can use this tool as an assistant to find out which parts of this library won't work with the currently installed package versions. So you can decide if you need the affected functions and if the function tells you which functions in the installed package versions are missing you have
a good hint to find the version you need to make this functions work. 

Testing
---------

face2face uses the Python ``pytest`` testing package.  You can learn more
about pytest on their `homepage <https://pytest.org>`_.

Test a source distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test an installed package
^^^^^^^^^^^^^^^^^^^^^^^^^^