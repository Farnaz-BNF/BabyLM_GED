The training code for BabyLMs from [Rozema's thesis](https://github.com/CRozema22/BabyLM-SLA) was used as the basis for the BabyLM training setup, but it was modified to fit the goals and experiments of this thesis.

This directory includes all notebooks for training six BabyLMs.
Each notebook trains one BabyLM.

After training, the models are saved in `../baby_models` directory.

### Notebooks
Notebooks names are in this format: `BabyLM_VX_LY.ipynb` where `X` is vocab-size and `Y` is number of hidden layers of a BabyLM.

+ **BabyLM_V20_L4.ipynb**
  This notebook trains a BabyLM with vocab-size of `20K` and `4` hidden layers.  

+ **BabyLM_V20_L6.ipynb**
  This notebook trains a BabyLM with vocab-size of `20K` and `6` hidden layers.
  
+ **BabyLM_V40_L4.ipynb**
  This notebook trains a BabyLM with vocab-size of `40K` and `4` hidden layers.
  
+ **BabyLM_V40_L6.ipynb**
  This notebook trains a BabyLM with vocab-size of `40K` and `6` hidden layers.
  
+ **BabyLM_V50_L4.ipynb**
  This notebook trains a BabyLM with vocab-size of `50K` and `4` hidden layers.

+ **BabyLM_V50_L6.ipynb**
  This notebook trains a BabyLM with vocab-size of `50K` and `6` hidden layers.
