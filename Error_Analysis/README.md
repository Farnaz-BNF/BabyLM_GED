This directory provides notebooks for the `Error Analysis`.

There is a `Save_model_outfiles_with_prob.ipynb` notebook to save model predictions and probibalites. It has this format: `text + labels + UID + prediction + Probabilities`. 

There is a `Error_Analysis_Code.ipynb` notebook that includes all codes for the error analysis.

There are three subfolders with the following structure:

	/EA_CSV_files
		Here you find all `.csv` files that `Error_Analysis_Code.ipynb` saves.
---
	/outfiles
		Files of models' predictions. It has this format: `text + labels + UID + prediction`.
---
	/outfiles_with_prob
		Files of models' predictions and probibalites.It has this format: `text + labels + UID + prediction + Probabilities`.
