import requests

from .exceptions import *
from requests.exceptions import HTTPError

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

class Client:
	def __init__(self, configuration):
		self.configuration = configuration

	def get(self, path, payload = {}):
		r = requests.get(self.url(path), params=payload, headers = self.headers(), timeout = self.configuration.timeout)
		return self.handle_response(r)

	def post(self, path, payload):
		r = requests.post(self.url(path), json=payload, headers = self.headers(), timeout = self.configuration.timeout)
		return self.handle_response(r)

	def handle_response(self, r):
		try:
			r.raise_for_status()

			return r.json()
		except HTTPError as err:
			self.handle_http_error(r, err)
		except JSONDecodeError:
			raise DetectLanguageError("Error decoding response JSON")

	def handle_http_error(self, r, err):
		try:
			json = r.json()

			if not 'error' in json:
				raise DetectLanguageError(err)

			raise DetectLanguageError(json['error']['message'])
		except JSONDecodeError:
			raise DetectLanguageError(err)

	def url(self, path):
		return "%s://%s/%s/%s" % (self.protocol(), self.configuration.host, self.configuration.api_version, path)

	def protocol(self):
		return 'https' if self.configuration.secure else 'http'

	def headers(self):
		return {
			'User-Agent': self.configuration.user_agent,
			'Authorization': 'Bearer ' + self.configuration.api_key,
		}
