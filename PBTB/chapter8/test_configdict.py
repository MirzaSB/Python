"""
Test the following:
1) A new instance is a ConfigDict. [DONE]
2) A new instance is also a dict. [DONE]
3) The filename passed to init is stored in the _filename attribute. [DONE]
4) A pre-existing file still exists after constructing a new instance.
5) A new, not-yet-existing file exists after constructing a new instance.
6) Bad file path to constructor raises an IOError.
7) Instance dict has correct key/value pairs.
8) Value with '=' in it has correct value (i.e. '='.split(value)) doesn't split into >2 pieces.
9) Good key read from instance returns correct value.
10) Bad key read from instance raises ConfigKeyError.
11) Key/value added to the instance updates file properly.
"""

import pytest
import os
import shutil
from assignment4 import ConfigDict, ConfigKeyError

class TestConfigDict:
	existing_filename = "config_filename.txt"
	existing_filename_template = "config_filename_template.txt"
	filename_that_does_not_exist = "new_config_filename.txt"
	unknown_filename = '/path/that/does/not/exist/filename.txt'

	def setup_class(self):
		shutil.copy(TestConfigDict.existing_filename_template, TestConfigDict.existing_filename)

	def test_obj(self):
		cd = ConfigDict(TestConfigDict.existing_filename)
		#1
		assert isinstance(cd, ConfigDict)
		#2
		assert isinstance(cd, dict)

	def test_filename(self):
		cd = ConfigDict(TestConfigDict.existing_filename)
		#3
		assert cd._filename == TestConfigDict.existing_filename
	
	def test_pre_existing_file(self):
		#4
		assert os.path.isfile(TestConfigDict.existing_filename_template)
		assert os.path.isfile(TestConfigDict.existing_filename)
		#5
		assert not os.path.isfile(TestConfigDict.filename_that_does_not_exist)
	
	def test_io_error(self):
		#6
		with pytest.raises(IOError):
			cd = ConfigDict(TestConfigDict.unknown_filename)
	
	def test_read_key(self):
		cd = ConfigDict(TestConfigDict.existing_filename)
		#7 & #9
		assert cd['a'] == '1'
		assert cd['b'] == '2'
		assert cd['c'] == '3'
		#8
		assert cd['value_with_equal_sign'] == 'test=equal'

	def test_config_dict_error(self):
		cd = ConfigDict(TestConfigDict.existing_filename)
		#10
		with pytest.raises(ConfigKeyError):
			print cd['unknown']

	def test_write_key(self):
		cd = ConfigDict(TestConfigDict.existing_filename)
		#11
		cd['new_key'] = 'new_value'
		assert cd['new_key'] == 'new_value'