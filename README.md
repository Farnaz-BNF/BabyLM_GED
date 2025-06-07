# Grammaticality and LLMs: Evaluating the Potential of BabyLMs for Grammatical Error Detection in NLP

This repository contains the code for the thesis submitted for the ReMA Humanities (Human Language Technology) at VU University Amsterdam. The files are Jupyter Notebooks and python scripts using `Python 3.11.12` and have been run using `Colab Pro`.


Author: Farnaz Banifatemi

Date: June 2025


## Run the Codes
To run the codes of this thesis **without any modification**, follow next steps:  

1. In the google drive, create a folder with `VU Thesis` name. 
2. In `VU Thesis` folder, create a folder with `Code` name.
3. Clone this repository. To clone the repository, run the following command:
   ```bash
   git clone https://github.com/Farnaz-BNF/BabyLM_GED.git
   ```
4. Put the cloned repository in `VU Thesis/Code` folder in google drive.
5. Then, install the requirements and run the codes.

Note:  
If you want to run the codes in a local machine, change the paths in the notebooks.  


## Requirements
All Requirements are stored in `requirements.txt`. To install requirements, run the following command.

```bash
pip install -r requirements.txt
```


## Structure

Each directory has its own `README` file. 

The structure of this repository is as follows:  


```
/
|
├─── .gitattributes
├─── .gitignore
├─── LICENSE
├─── README.md
├─── requirements.txt
│    
├─── baby_models
|    |
│    ├─── dev_V20.pkl
│    ├─── README.md
│    ├─── train_V20.pkl
│    │    
│    ├─── roberta-base
│    │    └─── zeroshot_with_prep
│    │                
│    ├─── roberta-base-strict-small-2023
│    │    └─── zeroshot_with_prep
│    │                
│    ├─── tokenizer_V20_folder
│    │    ├─── merges.txt
│    │    └─── vocab.json
│    │        
│    └─── V20L4
│         ├─── model_e10_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e1_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e2_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e3_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e4_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e5_v20_l4
│         │    └─── zeroshot_with_prep
|         |
│         ├─── model_e6_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e7_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         ├─── model_e8_v20_l4
│         │    └─── zeroshot_with_prep
│         │                
│         └─── model_e9_v20_l4
│             └─── zeroshot_with_prep
│                        
├─── BliMP_eval_code
|    |
│    ├─── evaluation-pipeline/              
│    ├─── lm_eval/
│    ├─── BabyLM_BLiMP_Evaluation.ipynb
│    └─── README.md
│                
├─── BLiMP_styled_prep
|    |
│    ├─── BEA2BLiMP.py
│    ├─── preposition.json
│    ├─── prep_filter_code.ipynb
│    ├─── README.md
│    ├─── data
|    |	  |
│    │    ├─── fce.dev.gold.bea19.m2
│    │    ├─── fce.test.gold.bea19.m2
│    │    └─── fce.train.gold.bea19.m2
│    │        
│    └─── prep_data
|         |
│         ├─── blimp_prep_m.json
│         ├─── blimp_prep_r.json
│         ├─── blimp_prep_u.json
│         ├─── filtered_preposition.json
│         └─── txt files
|              |
│              ├─── blimp_prep_m.txt
│              ├─── blimp_prep_r.txt
│              └─── blimp_prep_u.txt
│                
├─── Data
|    |
│    ├─── README.md
│    │    
│    ├─── babylm_10M
|    |	  |
│    │    ├─── aochildes.train
│    │    ├─── bnc_spoken.train
│    │    ├─── cbt.train
│    │    ├─── children_stories.train
│    │    ├─── gutenberg.train
│    │    ├─── open_subtitles.train
│    │    ├─── qed.train
│    │    ├─── simple_wikipedia.train
│    │    ├─── switchboard.train
│    │    └─── wikipedia.train
│    │        
│    ├─── babylm_dev
|    |	  |
│    │    ├─── aochildes.dev
│    │    ├─── bnc_spoken.dev
│    │    ├─── cbt.dev
│    │    ├─── children_stories.dev
│    │    ├─── gutenberg.dev
│    │    ├─── open_subtitles.dev
│    │    ├─── qed.dev
│    │    ├─── simple_wikipedia.dev
│    │    ├─── switchboard.dev
│    │    └─── wikipedia.dev
│    │        
│    └─── babylm_test
|         |
│         ├─── aochildes.test
│         ├─── bnc_spoken.test
│         ├─── cbt.test
│         ├─── children_stories.test
│         ├─── gutenberg.test
│         ├─── open_subtitles.test
│         ├─── qed.test
│         ├─── simple_wikipedia.test
│         ├─── switchboard.test
│         └─── wikipedia.test
│            
├─── Error_Analysis
|    |
│    ├─── Error_Analysis_Code.ipynb
│    ├─── README.md
│    ├─── Save_model_outfiles_with_prob.ipynb
│    ├─── EA_CSV_files
|    |	  |
│    │    ├─── all_correct.csv
│    │    ├─── all_outfiles.csv
│    │    ├─── all_wrongs.csv
│    │    ├─── baby_and_BB_vs_O.csv
│    │    ├─── baby_and_O_vs_BB.csv
│    │    ├─── baby_G_DET.csv
│    │    ├─── baby_G_PREP.csv
│    │    ├─── baby_G_SVA.csv
│    │    ├─── baby_PREP_G.csv
│    │    ├─── baby_PREP_SVA.csv
│    │    ├─── baby_SVA_DET.csv
│    │    ├─── baby_SVA_G.csv
│    │    ├─── baby_vs_bb_roberta.csv
│    │    ├─── baby_vs_O_and_BB.csv
│    │    ├─── baby_vs_o_roberta.csv
│    │    ├─── BB_G_DET.csv
│    │    ├─── BB_G_PREP.csv
│    │    ├─── BB_G_SVA.csv
│    │    ├─── BB_PREP_G.csv
│    │    ├─── BB_PREP_SVA.csv
│    │    ├─── bb_roberta_vs_baby.csv
│    │    ├─── bb_roberta_vs_o_roberta.csv
│    │    ├─── BB_SVA_G.csv
│    │    ├─── BB_vs_baby_and_O.csv
│    │    ├─── O_and_BB_vs_baby.csv
│    │    ├─── O_G_DET.csv
│    │    ├─── O_G_PREP.csv
│    │    ├─── O_G_SVA.csv
│    │    ├─── O_PREP_G.csv
│    │    ├─── O_PREP_SVA.csv
│    │    ├─── o_roberta_vs_baby.csv
│    │    ├─── o_roberta_vs_bb_roberta.csv
│    │    ├─── O_SVA_G.csv
│    │    └─── O_vs_baby_and_BB.csv
│    │        
│    ├─── outfiles
|    |	  |
│    │    ├─── outfile_bb_RoBERTa.csv
│    │    ├─── outfile_o_RoBERTa.csv
│    │    └─── outfile_v20_l4_e9.csv
│    │        
│    └─── outfiles_with_prob
|         |
│         ├─── outfile_prob_bb_RoBERTa.csv
│         ├─── outfile_prob_o_RoBERTa.csv
│         └─── outfile_prob_v20_l4_e9.csv
|
├─── fine_tune
|    |
│    ├─── epoch_10_evals.json
│    ├─── epoch_10_evals_half.json
│    ├─── epoch_1_evals.json
│    ├─── epoch_1_evals_half.json
│    ├─── Fine_Tune_Code.ipynb
│    ├─── Fine_Tune_Code_Other_Seed.ipynb
│    ├─── Fine_Tune_Data.ipynb
│    ├─── Fine_Tune_Epochs_experiment.ipynb
│    ├─── README.md
│    ├─── data
|    |	  |
│    │    ├─── all_prepared_data.csv
│    │    ├─── dev_data.csv
│    │    ├─── dev_test_no_split_data.csv
│    │    ├─── errors_class_data.csv
│    │    ├─── g_class_data.csv
│    │    ├─── test_data.csv
│    │    ├─── train_data.csv
│    │    └─── blimp_filtered
|    |         |
│    │         ├─── anaphor_agreement.json
│    │         ├─── argument_structure.json
│    │         ├─── binding.json
│    │         ├─── control_raising.json
│    │         ├─── determiner_noun_agreement.json
│    │         ├─── ellipsis.json
│    │         ├─── filler_gap.json
│    │         ├─── irregular_forms.json
│    │         ├─── island_effects.json
│    │         ├─── npi_licensing.json
│    │         ├─── preposition.json
│    │         ├─── quantifiers.json
│    │         └─── subject_verb_agreement.json
│    │            
│    ├─── models
|    |	  |
│    │    └─── fine_tuned_v20_l4_e9_model
|    |         |
│    │         ├─── config.json
│    │         ├─── merges.txt
│    │         ├─── model.safetensors
│    │         ├─── model_args.json
│    │         ├─── special_tokens_map.json
│    │         ├─── tokenizer.json
│    │         ├─── tokenizer_config.json
│    │         ├─── training_args.bin
│    │         └─── vocab.json
│    │            
│    └─── outfiles
|         |
│         ├─── outfile_bb_RoBERTa.csv
│         ├─── outfile_o_RoBERTa.csv
│         ├─── outfile_v20_l4_e1.csv
│         ├─── outfile_v20_l4_e10.csv
│         ├─── outfile_v20_l4_e2.csv
│         ├─── outfile_v20_l4_e3.csv
│         ├─── outfile_v20_l4_e4.csv
│         ├─── outfile_v20_l4_e5.csv
│         ├─── outfile_v20_l4_e6.csv
│         ├─── outfile_v20_l4_e7.csv
│         ├─── outfile_v20_l4_e8.csv
│         └─── outfile_v20_l4_e9.csv
│            
├─── seeds_experiment
│    │    
│    ├─── V40L4
|    |	  |
│    |    ├─── S1278_BabyLM_V40_L4.ipynb
│    |    ├─── S162_BabyLM_V40_L4.ipynb
│    |    ├─── S354_BabyLM_V40_L4.ipynb
│    |    ├─── S56_BabyLM_V40_L4.ipynb
│    |    └─── S670_BabyLM_V40_L4.ipynb
│    │    
│    ├─── V20L4
|    |	  |
│    │    ├─── S1278_BabyLM_V20_L4.ipynb
│    │    ├─── S162_BabyLM_V20_L4.ipynb
│    │    ├─── S354_BabyLM_V20_L4.ipynb
│    │    ├─── S56_BabyLM_V20_L4.ipynb
│    │    └─── S670_BabyLM_V20_L4.ipynb
│    │        
│    └─── README.md
│            
├─── Training_BabyLMs
|    |
│    ├─── BabyLM_V20_L4.ipynb
│    ├─── BabyLM_V20_L6.ipynb
│    ├─── BabyLM_V40_L4.ipynb
│    ├─── BabyLM_V40_L6.ipynb
│    ├─── BabyLM_V50_L4.ipynb
│    ├─── BabyLM_V50_L6.ipynb
│    └─── README.md
│        
└─── zero_shot_evaluation
     |
     ├─── README.md
     ├─── zero_shot_chart.ipynb
     └─── Zero_shot_Code.ipynb
```


