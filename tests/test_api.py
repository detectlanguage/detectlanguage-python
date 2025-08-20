# -*- coding: utf-8 -*-

import pytest
import detectlanguage
import os

class TestApi:
	def setup_method(self):
		detectlanguage.configuration.api_key = os.environ['DETECTLANGUAGE_API_KEY']

	def test_detect_code(self):
		result = detectlanguage.detect_code("Hello world")
		assert result == 'en'

	def test_detect(self):
		result = detectlanguage.detect("Hello world")
		assert result[0]['language'] == 'en'

	def test_detect_with_array(self):
		with pytest.warns(DeprecationWarning, match="use detect_batch"):
			detectlanguage.detect(["Hello world", "Ėjo ežiukas"])

	def test_detect_unicode(self):
		result = detectlanguage.detect("Ėjo ežiukas")
		assert result[0]['language'] == 'lt'

	def test_detect_batch(self):
		result = detectlanguage.detect_batch(["Hello world", "Ėjo ežiukas"])
		assert result[0][0]['language'] == 'en'
		assert result[1][0]['language'] == 'lt'

	def test_account_status(self):
		result = detectlanguage.account_status()
		assert result['status'] == 'ACTIVE'

	def test_languages(self):
		result = detectlanguage.languages()
		assert { 'code': 'en', 'name': 'English' } in result

	def test_simple_detect(self):
		with pytest.warns(DeprecationWarning, match="simple_detect.*deprecated"):
			result = detectlanguage.simple_detect("Hello world")
			assert result == 'en'

	def test_user_status(self):
		with pytest.warns(DeprecationWarning, match="user_status.*deprecated"):
			result = detectlanguage.user_status()
			assert result['status'] == 'ACTIVE'

class TestApiErrors:
	def test_invalid_key(self):
		detectlanguage.configuration.api_key = 'invalid'
		with pytest.raises(detectlanguage.DetectLanguageError):
			detectlanguage.detect("Hello world")
