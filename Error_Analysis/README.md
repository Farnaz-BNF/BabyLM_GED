
This directory provides notebooks for the `Error Analysis`.

There are `Error_Analysis_Code.ipynb` and `Error_Analysis_Code_P2.ipynb` notebooks that includes all codes for the error analysis.

### Subdirectories  
There are four subdirectories with the following structure:


+ **EA_CSV_files/**  
	Here you find all `.csv` files that `Error_Analysis_Code.ipynb` saves.

+ **outfiles/**  
  Files of models' predictions. It has this format: `text + labels + UID + prediction`.

+ **outfiles_with_prob/**  
  Files of models' predictions and row_outputs. It has this format: `text + labels + UID + prediction + row_outputs`.


+ **EA_ORGANIZED_CSVs/**  
Here all the `.csv` files in folder `EA_CSV_files/` are organized in subdirectories. Each subdirectory is as follows:

	+ **Compare_two_models/**  
This directory includes six `.csv` files the models compared one by one, with following name format: `MODEL1_vs_MODEL2` where `MODEL1` predicts correct and `MODEL2` predicts incorrect.

	+ **Correct_vs_Wrong/**  
Compare all models against each other in six `.csv` files with following name format: `CMODELS_vs_WMODELS.csv` where `CMODELS` is name of one or two model(s) that predict(s) instance correctly and `WMODELS` is name of other model(s) that predict(s) incorrectly.
		+ This directory also includes six subdirectories with same name format as each `.csv` files with an additional  `detailes_` at the beginning. Each subdirectory includes:
			+  12 `.csv` files with `GOLD_WRONG.csv` name format where `GOLD`is true label and `WRONG` label refers to instances that are incorrectly classified. 
			+  Two `.csv` files ,`30_G_PREP_baby_and_BB_vs_O.csv` and `30_PREP_G_baby_and_BB_vs_O.csv` where 30 instances that models misclassified between `PREP` and `G` are randomly selected for error analysis part (if there is less than 30 instances all of them are selected).
			+ Two `.json` files where count  `GOLD_WRONG` label pairs in total and per models. 


	+ **G_DET/**  
All instance where gold label is `G` but models predict it as `DET`. One `.csv` file for each model(s).

	+ **G_PREP/**  
All instance where gold label is `G` but models predict it as `PREP`. One `.csv` file for each model(s).

	+ **G_SVA/**  
All instance where gold label is `G` but models predict it as `SVA`. One `.csv` file for each model(s).

	+ **PREP_G/**  
All instance where gold label is `PREP` but models predict it as `G`. One `.csv` file for each model(s).

	+ **PREP_SVA/**  
All instance where gold label is `PREP` but models predict it as `SVA`. One `.csv` file for each model(s).

	+ **SVA_DET/**  
All instance where gold label is `SVA` but models predict it as `DET`. One `.csv` file for each model(s).

	+ **SVA_G/**  
All instance where gold label is `SVA` but models predict it as `G`. One `.csv` file for each model(s).

	+ **all_correct.csv**  
All instance that all models predict them correctly.

	+ **all_outfiles.csv**  
All predicts of all models together.

	+ **all_wrongs.csv**  
All instance that all models predict them incorrectly.
