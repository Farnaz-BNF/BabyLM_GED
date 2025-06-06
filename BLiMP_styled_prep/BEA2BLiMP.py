import re
import os
import json
import argparse

def read_props_from_bea_m2(file_path):
	""" Read preposition errors from BEA M2 file and return sentences with preposition errors.
	Args: 
		file_path (str): Path of the BEA M2 file.
	Returns:
		dict: Sentences with preposition errors.
	"""
	one_sentence = dict()
	sentences = dict()

	with open(file_path, 'r') as inputfile:

		sents_count = 0
		new_sent_line_count = 1
		error_list = []

		patterns = [r"err_\d+_R:PREP", r"err_\d+_M:PREP", r"err_\d+_U:PREP"]
		for line in inputfile:

			if line =="" or line.isspace():
				one_sentence['errors']=error_list
				error_list = []

				if any(re.search(r'err_\d+_UNK', gram_error['err_id']) for gram_error in one_sentence['errors']):
					new_sent_line_count = 1
					one_sentence= dict()
					continue

				if any(re.search(pattern, gram_error['err_id']) for gram_error in one_sentence['errors'] for pattern in patterns):
					sentences[sents_count] = one_sentence
					one_sentence= dict()
					sents_count+=1
					new_sent_line_count = 1
					continue
				else:
					new_sent_line_count = 1
					one_sentence= dict()
					continue

			line = line.strip()
			if line.startswith("S"):
				one_sentence["sentence"]=' '.join(line.split()[1:])
				one_sentence["sentence_tokens"]=line.split()[1:]
			else:
				# 4 6 , R:OTHER , PEOPLE , REQUIRED , -NONE- , 0
				annotate = ''.join(line.split(maxsplit=1))[1:].split('|||')
				if annotate[-1] != "0":
					continue

				annot_info={'err_id':f"err_{new_sent_line_count}_{annotate[1]}",
							'start_offset':int(annotate[0].split()[0]),
							'end_offset':int(annotate[0].split()[1]),
							'error_type':annotate[1],
							'correction':annotate[2]}

				error_list.append(annot_info)
				new_sent_line_count +=1

	print(f"there is {sents_count} sentences with preposition error in <{file_path}> file.")

	return sentences

def fix_sentence_spaces(txt):
	""" Fix spaces in the sentence.
	Args:
		txt (str): Sentence text.
	Returns:
		str: Sentence with fixed spaces.
	"""
	txt = txt.replace(" 's", "'s")
	txt = txt.replace(" n'", "n'")
	txt = txt.replace(" ( ", " (")
	txt = txt.replace(" ) ", ") ")
	txt = txt.replace(" [ ", " [")
	txt = txt.replace(" ] ", "] ")
	txt = txt.replace(" { ", " {")
	txt = txt.replace(" } ", "} ")
	txt = txt.replace(" 'm", "'m")
	txt = txt.replace(" 've", "'ve")
	txt = txt.replace(" 're", "'re")
	txt = txt.replace(" 'd", "'d")
	txt = txt.replace(" 'll", "'ll")
	txt2 = re.sub(r"""\s([.,`'"!?])""", r"\1", txt)
	return txt2

def duplicate_prep_sentence(sentence:dict):
	""" Duplicate sentence for each preposition error.
	Args:
		sentence (dict): Sentence with preposition error.
	Returns:
		list: List of sentences with preposition errors.
	"""
	prep_sents = []
	for error in sentence['errors']:
		prep_sents.append({'error':error,'sentence':sentence})
	return prep_sents

def keep_only_one_prep(sentences_dict:dict):
	""" Keep only one preposition error in each sentence.
	Args:
		sentences_dict (dict): Sentences with preposition errors.
	Returns:
		list: List of sentences with only one preposition error
"""

	prep_list = []
	for sent_id, sent in sentences_dict.items():
		prep_list = prep_list + duplicate_prep_sentence(sent)

	blimp_list_R = []
	blimp_list_M = []
	blimp_list_U = []

	for sent in prep_list:
		blimp_styles = convert_to_blimp_format(sent['error'],sent['sentence'])
		if re.search(r"err_\d+_R:PREP", sent['error']['err_id']):
			blimp_list_R.append(blimp_styles)
		if re.search(r"err_\d+_M:PREP", sent['error']['err_id']):
			blimp_list_M.append(blimp_styles)
		if re.search(r"err_\d+_U:PREP", sent['error']['err_id']):
			blimp_list_U.append(blimp_styles)

	return blimp_list_R, blimp_list_M, blimp_list_U

def convert_to_blimp_format(error:dict, error_sentence_dict:dict):
	""" Convert preposition error to BLiMP format.
	Args:
		error (dict): Preposition error.
		error_sentence_dict (dict): Sentence with preposition error.
	Returns:
		dict: Preposition error in BLiMP format.
	"""
	blimp_formated_data = {}
	error_idx = 0
	sentence_dict = error_sentence_dict.copy()
	corrected_sentence = sentence_dict['sentence_tokens'].copy()
	
	errors_copy = [err.copy() for err in sentence_dict['errors']]

	for other_error_idx, other_error in enumerate(errors_copy):
		if other_error['err_id'] == error['err_id']:
			error_idx = other_error_idx
			continue

		other_error_start_offset = other_error['start_offset']
		other_error_end_offset = other_error['end_offset']
		other_error_correction = other_error['correction'].split()
		len_shift = len(other_error_correction) - (other_error_end_offset - other_error_start_offset)

		for errs in errors_copy[other_error_idx+1:]:
			errs['start_offset'] += len_shift
			errs['end_offset'] += len_shift

		corrected_sentence = corrected_sentence[:other_error_start_offset] + other_error_correction + corrected_sentence[other_error_end_offset:]

	error = errors_copy[error_idx]

	start_offset = error['start_offset']
	end_offset = error['end_offset']
	correction = error['correction'].split()

	blimp_formated_data = {"sentence_good": fix_sentence_spaces(' '.join(corrected_sentence[:start_offset] + correction + corrected_sentence[end_offset:])),
							"sentence_bad": fix_sentence_spaces(' '.join(corrected_sentence)),
							"one_prefix_prefix": fix_sentence_spaces(' '.join(corrected_sentence[:start_offset])),
							"one_prefix_word_good": ' '.join(correction), 
							"one_prefix_word_bad": ' '.join(corrected_sentence[start_offset:end_offset]),
							"field": "syntax-semantics", 
							"linguistics_term": "Preposition", 
							"UID": "Preposition", 
							"simple_LM_method": True,
							"one_prefix_method": True, 
							"two_prefix_method": False, 
							"lexically_identical": False}
	return blimp_formated_data

def correct_other_errors(one_sentence_dict:dict):
	""" Correct other errors in the sentence.
	Args:
		one_sentence_dict (dict): Sentence with preposition error
	Returns:
		dict: Sentence with corrected other errors.
	"""
	corrected_sentence = one_sentence_dict['sentence_tokens'].copy()
	fixed_errors_idx = []

	for error_number, gram_error in enumerate(one_sentence_dict['errors']):
		if gram_error['error_type'] in ("R:PREP","M:PREP","U:PREP"): # skip preposition errors
			continue
		start_offset = gram_error['start_offset']
		end_offset = gram_error['end_offset']
		correction = gram_error['correction'].split()
		len_shift = len(correction) - (end_offset-start_offset)

		for other_error in one_sentence_dict['errors'][error_number+1:]:
			other_error['start_offset'] += len_shift
			other_error['end_offset'] += len_shift

		corrected_sentence = corrected_sentence[:start_offset] + correction + corrected_sentence[end_offset:]

		fixed_errors_idx.append(error_number)
	one_sentence_dict['sentence_tokens'] = corrected_sentence
	one_sentence_dict['sentence'] = ' '.join(corrected_sentence)

	fixed_errors_idx.reverse()
	for idx in fixed_errors_idx:
		del one_sentence_dict['errors'][idx]
		
def preprocess_data(sentences_dict:dict):
	""" Preprocess data.
	Args:
		sentences_dict (dict): Sentences with preposition errors.
	Returns:
		dict: Sentences with corrected other errors.
	"""
	for sent_id, sent in sentences_dict.items():
		correct_other_errors(sent)
	return sentences_dict

def write_output_file(blimp_list, output_file):
	""" Write BLiMP-styled data to a file.
	Args:
		blimp_list (list): BLiMP-styled data.
		output_file (str): Path of the output file.
	"""
	with open (output_file, 'w') as outfile:
		for item in blimp_list:
			outfile.write(str(item)+'\n')
			
def write_json(data, filename):
	""" Write data to a JSON file.
	Args:
		data (dict): Data to be written.
		filename (str): Path of the output JSON file.
	"""
	with open(filename,'w') as outfile:
		json.dump(data, outfile, indent=4) 

def process_bea_m2_file(file_path):
	""" Process BEA M2 file.
	Args:
		file_path (str): Path of the BEA M2 file.
	Returns:
		list: BLiMP-styled data.
	"""
	sents = read_props_from_bea_m2(file_path) # read file
	sents = preprocess_data(sents) # correct other errors
	blimp_list_r, blimp_list_m, blimp_list_u = keep_only_one_prep(sents) # keep only one preposition error and convert to BLiMP format
	return blimp_list_r, blimp_list_m, blimp_list_u # return BLiMP-styled data

def reset_pairID(blimp_list):
	""" Reset pairID.
	Args:
		blimp_list (list): BLiMP-styled data.
	Returns:
		list: BLiMP-styled data with reset pairID.
	"""
	for idx, blimp_sent in enumerate(blimp_list):
		blimp_sent['pairID']= idx
	return blimp_list

def main(args):
	""" Main function.
	Args:
		args (argparse.ArgumentParser): Command line arguments.
	"""
	
	data_dir_path = args.data_dir_path
	
	train_file_name = "fce.train.gold.bea19.m2"
	dev_file_name = "fce.dev.gold.bea19.m2"
	test_file_name = "fce.test.gold.bea19.m2"

	train_path = os.path.join(data_dir_path, train_file_name)
	dev_path = os.path.join(data_dir_path , dev_file_name)
	test_path = os.path.join(data_dir_path , test_file_name)
	
	blimp_list_train_r, blimp_list_train_m, blimp_list_train_u = process_bea_m2_file(train_path)
	blimp_list_dev_r, blimp_list_dev_m, blimp_list_dev_u = process_bea_m2_file(dev_path)
	blimp_list_test_r, blimp_list_test_m, blimp_list_test_u = process_bea_m2_file(test_path)

	blimp_list_R = blimp_list_train_r + blimp_list_dev_r + blimp_list_test_r
	blimp_list_M = blimp_list_train_m + blimp_list_dev_m + blimp_list_test_m
	blimp_list_U = blimp_list_train_u + blimp_list_dev_u + blimp_list_test_u

	print (f"R_PREP: {len(blimp_list_R)}\nM_PREP: {len(blimp_list_M)}\nU_PREP: {len(blimp_list_U)}")

	blimp_list_R = reset_pairID(blimp_list_R)
	blimp_list_M = reset_pairID(blimp_list_M)
	blimp_list_U = reset_pairID(blimp_list_U)

	write_output_file(blimp_list_R, os.path.join(args.data_dir_path,"blimp_prep_r.txt"))
	write_output_file(blimp_list_M, os.path.join(args.data_dir_path,"blimp_prep_m.txt"))
	write_output_file(blimp_list_U, os.path.join(args.data_dir_path,"blimp_prep_u.txt"))

	write_json(blimp_list_R, os.path.join(args.data_dir_path,"blimp_prep_r.json"))
	write_json(blimp_list_M, os.path.join(args.data_dir_path,"blimp_prep_m.json"))
	write_json(blimp_list_U, os.path.join(args.data_dir_path,"blimp_prep_u.json"))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='BEA2BLiMP')
	parser.add_argument('--data_dir_path', type=str, help='Path of the data dir')
	args = parser.parse_args()
	main(args)

###### Run following command to generate Preposition BLiMP-styled data: 
##			 python BEA2BLiMP.py --data_dir_path .\data
