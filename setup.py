from setuptools import setup, Extension
with open("README.rst", "r") as fh:
    long_description = fh.read()
DEPENDENCIES = ['numpy', 'pandas', 'matplotlib', 'networkx', 'scipy',
                'seaborn', 'powerlaw']
packages = ["face2face",
            "face2face.imports",
            "face2face.statistics",
            "face2face.visualization",
	    "face2face.compatibility_check"
            ]
setup(name="face2face",
      version="0.2.1 Alpha",
      packages=packages,
      description="Library with basic social science functions",
      url="https://gesiscss.github.io/face2face/",
      license="GPLv3",
      #python_requires=">=3.6.1",
      long_description=long_description,
      install_requires=DEPENDENCIES,
      package_data = {"face2face": ["data/*/*.dat"]}
      )