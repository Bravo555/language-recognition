#!/usr/bin/python3

import unittest
from language_recognition import *
from collections import OrderedDict

class TestLanguageRecognition(unittest.TestCase):
	def test_character_frequency(self):
		self.assertEqual(character_frequency('aaabb'), OrderedDict([('a', 3), ('b', 2)]))

if __name__ == '__main__':
	unittest.main()
