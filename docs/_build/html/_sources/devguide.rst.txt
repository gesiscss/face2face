Developer Guide
================

If you want to be part in the development here is a guide on how to setup your local repository.

1. 

	* Get the development repository from https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit<https://github.com/gesiscss/face-to-face-interaction-analysis-toolkit> and create your own fork by clicking on the fork button.

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
		
	* Commit your progress locally
	
	* Create a branch for your new feature or for the bugfix that you want to add to the toolbox. Use a meaningful name as a branch name like 'Feature_XYZ'::
	
		git checkout -b Feature_XYZ

3.
	
	* Push your local changes to the fork on GitHub::
	
		git push origin	Feature_XYZ
		
	* Use the green Pull Request button, that shows up in the new branch
	
	
Version Control for face-to-face-interaction-analysis-toolkit project
------------------------------------------------------------------------

When you want to commit any changes on your repository the git hook will run every pytest to check if your code does not break anything.
If the test passes you can push it to the repository. 






