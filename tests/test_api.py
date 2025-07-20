# -*- coding: utf-8 -*-

import pytest
import detectlanguage
import os

class TestApi:
	def setup_method(self):
		detectlanguage.configuration.api_key = os.environ['DETECTLANGUAGE_API_KEY']
		
	def test_simple_detect(self):
		result = detectlanguage.simple_detect("Hello world")
		assert result == 'en'

	def test_detect(self):
		result = detectlanguage.detect("Hello world")
		assert result[0]['language'] == 'en'

	def test_detect_unicode(self):
		result = detectlanguage.detect("Ėjo ežiukas")
		assert result[0]['language'] == 'lt'

	def test_detect_array(self):
		result = detectlanguage.detect(["Hello world", "Ėjo ežiukas"])
		assert result[0][0]['language'] == 'en'
		assert result[1][0]['language'] == 'lt'

	def test_user_status(self):
		result = detectlanguage.user_status()
		assert result['status'] == 'ACTIVE'

	def test_languages(self):
		result = detectlanguage.languages()
		assert { 'code': 'en', 'name': 'ENGLISH' } in result

	def test_secure(self):
		detectlanguage.configuration.secure = True
		result = detectlanguage.detect("Hello world")
		assert result[0]['language'] == 'en'
		detectlanguage.configuration.secure = False

class TestApiErrors:
	def test_invalid_key(self):
		detectlanguage.configuration.api_key = 'invalid'
		with pytest.raises(detectlanguage.DetectLanguageError):
			detectlanguage.detect("Hello world")
		