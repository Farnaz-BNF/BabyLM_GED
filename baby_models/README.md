This directory include all training stages of the selected BabyLM (`BabyLM_V20_L4`) and also zero-shot results for the selected BabyLM, BB-RoBERTa and O-RoBERTa.

If you want to work with another pretrained model just put it here.
Other BabyLMs that this thesis trained and BB-RoBERTa are avilable [Here](https://mega.nz/folder/FAIkxJQA#hYsbYO_ngCe8d4SLacl-dQ).
Or, you can find [O-RoBERTa](https://huggingface.co/FacebookAI/roberta-base) and [BB-RoBERTa](https://huggingface.co/babylm/roberta-base-strict-small-2023) in huggingface.

Two other files in this directory:

1. dev_V20.pkl
2. train_V20.pkl

These two files are prepared data to train any model with vocab-size = `20K`.
Also, `Tokenizer` for model with `20K` vocab-size is stored in "`tokenizer_V20_folder`" directory. 

For the vocab-size of `40K` and `50K`, you can find prepared data and tokenizer [Here](https://mega.nz/folder/kNZWVDbC#QeWyPSzi0EIrdIw4ew9TxQ).

Overall, this directory structure should be like:

		/baby_models
		|
		├── /roberta-base
		|
		├── /roberta-base-strict-small-2023
		|
		├── /V20L4
		|	├── /model_e1_v20_l4
		|	⋮
		|	└── /model_e10_v20_l4
		|
		├── /V20L6
		|	├── /model_e1_v20_l6
		|	⋮
		|	└── /model_e10_v20_l6
		|
		├── /V40L4
		|	├── /model_e1_v40_l4
		|	⋮
		|	└── /model_e10_v40_l4
		|
		├── /V40L6
		|	├── /model_e1_v40_l6
		|	⋮
		|	└── /model_e10_40_l6
		|
		├── /V50L4
		|	├── /model_e1_v50_l4
		|	⋮
		|	└── /model_e10_v50_l4
		|
		├── /V50L6
		|	├── /model_e1_v50_l6
		|	⋮
		|	└── /model_e10_v50_l6
		|
		├── /tokenizer_V20_folder
		|
		├── /tokenizer_V40_folder
		|
		├── /tokenizer_V50_folder
		|
		├── dev_V20.pkl
		|
		├── dev_V40.pkl
		|
		├── dev_V50.pkl
		|
		├── train_V20.pkl
		|
		├── train_V40.pkl
		|
		└── train_V50.pkl
		
