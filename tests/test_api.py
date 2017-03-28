# -*- coding: utf-8 -*-

from . import utils
from nose.tools import *
import detectlanguage
import os

class TestApi(utils.TestCase):
	def setUp(self):
		detectlanguage.configuration.api_key = os.environ['DETECTLANGUAGE_API_KEY']
		
	def test_simple_detect(self):
		result = detectlanguage.simple_detect("Hello world")
		eq_('en', result)

	def test_detect(self):
		result = detectlanguage.detect("Hello world")
		eq_('en', result[0]['language'])

	def test_detect_unicode(self):
		result = detectlanguage.detect("Ėjo ežiukas")
		eq_('lt', result[0]['language'])

	def test_detect_array(self):
		result = detectlanguage.detect(["Hello world", "Ėjo ežiukas"])
		eq_('en', result[0][0]['language'])
		eq_('lt', result[1][0]['language'])

	def test_user_status(self):
		result = detectlanguage.user_status()
		eq_('ACTIVE', result['status'])

	def test_languages(self):
		result = detectlanguage.languages()
		assert { 'code': 'en', 'name': 'ENGLISH' } in result

	def test_secure(self):
		detectlanguage.configuration.secure = True
		result = detectlanguage.detect("Hello world")
		eq_('en', result[0]['language'])
		detectlanguage.configuration.secure = False

class TestApiErrors(utils.TestCase):
	@raises(detectlanguage.DetectLanguageError)
	def test_invalid_key(self):
		detectlanguage.configuration.api_key = 'invalid'
		detectlanguage.detect("Hello world")
		