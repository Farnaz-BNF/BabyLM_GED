This directory contains notebooks, files, and subdirectories related to fine-tuning the models.


## Notebooks  

+ **Fine_Tune_Data.ipynb**  
	This notebook includes all codes to prepare data for the fine-tuning phase.

+ **Fine_Tune_Epochs_experiment.ipynb**  
	This notebook includes all codes to do the epoch experiment in the fine-tuning phase.

+ **Fine_Tune_Code_Other_Seed.ipynb**  
	This notebook includes all codes to do the seed experiment in the fine-tuning phase.

+ **Fine_Tune_Code.ipynb**  
	This notebook includes all codes to fine-tune the models.


## Files  
+ **epoch_1_evals_half.json**  
  Evaluation results of the first training stage of the selected BabyLM on half of data in the epoch experiment.  

+ **epoch_10_evals_half.json**  
  Evaluation results of the last training stage of the selected BabyLM on half of data in the epoch experiment.
  
+ **epoch_1_evals.json**  
  Evaluation results of the first training stage of the selected BabyLM on all data in the epoch experiment. 

+ **epoch_10_evals.json**  
  Evaluation results of the last training stage of the selected BabyLM on all data in the epoch experiment.

## Subdirectories  
1. **data/**  
  Contains datasets used for fine-tuning and evaluation.    

1. **models/**  
  Stores fine-tuned models. You can find all the fine-tuned models [Here](https://mega.nz/folder/xVhF1JbZ#3e8oeSVzHk9dvE2-kZyYzg). To work with the other models, download and put the `model folder` in this directory.
  
1. **outfiles/**  
  Stores outfiles of the models' predictions.  

## Directory Structure  
Overall, this directory structure should be like:
```  
fine-tune/
|
├── data/
|	├── blimp_filtered/
|	├── all_prepared_data.csv
|	├── dev_data.csv
|	├── dev_test_no_split_data.csv
|	├── errors_class_data.csv
|	├── g_class_data.csv
|	├── test_data.csv
|	└── train_data.csv
|
├── models/
|	├── fine_tuned_v20_l4_e9_model/
|	⋮
|	├── fine_tuned_bb_RoBERTa_model/
|	└── fine_tuned_o_RoBERTa_model/
|
├── outfiles/
|	├── outfile_v20_l4_e1.csv
|	├── outfile_v20_l4_e2.csv
|	├── outfile_v20_l4_e3.csv
|	├── outfile_v20_l4_e4.csv
|	├── outfile_v20_l4_e5.csv
|	├── outfile_v20_l4_e6.csv
|	├── outfile_v20_l4_e7.csv
|	├── outfile_v20_l4_e8.csv
|	├── outfile_v20_l4_e9.csv
|	├── outfile_v20_l4_e10.csv
|	├── outfile_bb_RoBERTa.csv
|	└── outfile_o_RoBERTa.csv
|
├── epoch_1_evals.json
|
├── epoch_10_evals.json
|
├── epoch_1_evals_half.json
|
├── epoch_10_evals_half.json
|
├── Fine_Tune_Data.ipynb
|
├── Fine_Tune_Epochs_experiment.ipynb
|
├── Fine_Tune_Code_Other_Seed.ipynb
|
└── Fine_Tune_Code.ipynb
```  

