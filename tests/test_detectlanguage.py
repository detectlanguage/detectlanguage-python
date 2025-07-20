import pytest
import detectlanguage

class TestDetectlanguage:
	def testDefaults(self):
		assert detectlanguage.configuration.api_version == '0.2'
		assert detectlanguage.configuration.host == 'ws.detectlanguage.com'
		assert detectlanguage.configuration.secure == False

	def testConfiguration(self):
		detectlanguage.configuration.api_key = 'TEST'
		assert detectlanguage.client.configuration.api_key == 'TEST'
