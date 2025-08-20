import detectlanguage

class Configuration:
	api_key = None
	api_version = 'v3'
	host = 'ws.detectlanguage.com'
	user_agent = 'Detect Language API Python Client ' + detectlanguage.__version__
	timeout = 5
	proxies = None  # e.g., {'https': 'https://proxy.example.com:8080'}
