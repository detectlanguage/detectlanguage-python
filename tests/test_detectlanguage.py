from . import utils
from nose.tools import eq_
import detectlanguage

class TestDetectlanguage(utils.TestCase):
	def testDefaults(self):
		eq_('0.2', detectlanguage.configuration.api_version)
		eq_('ws.detectlanguage.com', detectlanguage.configuration.host)
		eq_(False, detectlanguage.configuration.secure)

	def testConfiguration(self):
		detectlanguage.configuration.api_key = 'TEST'
		eq_('TEST', detectlanguage.client.configuration.api_key)
