Developer Guide
================

If you want to be part in the development here is a guide on how to setup your local repository.

1. 

	* Get the development repository from `https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit<https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit>`_ and create your own fork by clicking on the fork button.

	* Clone the repository to your local computer by using:: 
		
		git clone git@github.com:your-username/face-to-face-interaction-analysis-toolkit.git

	* After that you have to add the upstream repository. Navigate to the face-to-face-interaction-analysis-toolkit folder and do the following ::
	
		git remote add upstream git@github.com:face-to-face-interaction-analysis-toolkit/face-to-face-interaction-analysis-toolkit.git
		
	* You should have two remote repositories now:
		
		- ``upstream``, this repository refers to the original ``face-to-face-interaction-analysis-toolkit`` repository
		- ``origin``, this is the repository of you personal fork
		
2. 

	* Pull the latest changes from upstream::
		
		git checkout master
		git pull upstream master
		
	* Commit your progress locally with (``git add`` and ``git commit``)
	
	* Create a branch for your new feature or for the bugfix that you want to add to the library. Use a meaningful name as a branch name like 'Feature_XYZ'::
	
		git checkout -b Feature_XYZ

3.
	
	* Push your changes back to your fork on GitHub::
	
		git push origin	Feature_XYZ
		
	* Use the green Pull Request button, that shows up in the new branch
	
	
Version Control for face-to-face-interaction-analysis-toolkit project
------------------------------------------------------------------------

Please make sure that you have installed ``pre-commit`` and ``pytest`` on your computer

If you cloned the Repository and pulled the latest changes install pre-commit by::

Using pip::

	pip install pre-commit

Using homebrew::

	brew install pre-commit
	
Using Conda::
	
	conda install -c conda-forge pre-commit

After that you have to install the hooks.
	
pre-commit install --install-hooks --overwrite 


When you want to commit any changes on your repository the hook will run every pytest to check if your code does not break anything.
If the test passes you can push it to your repository.






