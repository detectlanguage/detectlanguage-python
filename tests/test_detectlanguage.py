import pytest
import detectlanguage

class TestDetectlanguage:
	def testDefaults(self):
		assert detectlanguage.configuration.api_version == 'v3'
		assert detectlanguage.configuration.host == 'ws.detectlanguage.com'

	def testConfiguration(self):
		detectlanguage.configuration.api_key = 'TEST'
		assert detectlanguage.client.configuration.api_key == 'TEST'
