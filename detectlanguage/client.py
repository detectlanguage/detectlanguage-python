import requests

from .exceptions import *

class Client:
	def __init__(self, configuration):
		self.configuration = configuration

	def get(self, path, payload = {}):
		r = requests.get(self.url(path), params=self.data(payload), headers = self.headers())
		return self.handle_response(r)

	def post(self, path, payload):
		r = requests.post(self.url(path), json=self.data(payload), headers = self.headers())
		return self.handle_response(r)

	def handle_response(self, r):
		json = r.json()

		if 'error' in json:
			raise DetectLanguageError(json['error']['message'])

		r.raise_for_status()

		return json

	def url(self, path):
		return "%s://%s/%s/%s" % (self.protocol(), self.configuration.host, self.configuration.api_version, path)

	def protocol(self):
		return 'https' if self.configuration.secure else 'http'

	def data(self, payload):
		payload.update({ 'key': self.configuration.api_key })
		return payload

	def headers(self):
		return { 'User-Agent': self.configuration.user_agent }
