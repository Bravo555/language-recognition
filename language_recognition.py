#!/usr/bin/python3

import string 
from collections import OrderedDict

def character_frequency(input_text):
	# Initialize dictionary with all letters
	return_dict = OrderedDict()
	for char in string.ascii_lowercase:
		return_dict[char] = 0
	
	for char in input_text:
		return_dict[char] += 1
	
	# Remove unnecessary keys
	for char in list(return_dict.keys()):
		if return_dict[char] == 0:
			return_dict.pop(char)

	return return_dict

