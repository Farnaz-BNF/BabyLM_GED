This directory provides notebook, script, and data to create a BLiMP-style datset for prepositions.

The `BEA2BLiMP.py` script is used to extract any sentence in [BEA-2019 shared task dataset](https://www.cl.cam.ac.uk/research/nl/bea2019st/) that has at least one preposition error.

You can run it like:

`BEA2BLiMP.py --data_dir_path .\data`

The `prep_filter_code.ipynb` includes all codes that are used to create a filtered BLiMP-style dataset for prepositions.

The final filtered BLiMP-style dataset for prepositions is stored in `preposition.json`.

There are two subfolders with the following structure:

	/data
		Here you find BEA-2019 dataset used to create the BLiMP-style dataset for prepositions.

---

	/prep_data
		Any output of script and notebook is saved in this directory.

