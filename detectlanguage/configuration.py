import detectlanguage

class Configuration:
	api_key = None
	api_version = '0.2'
	host = 'ws.detectlanguage.com'
	user_agent = 'Detect Language API Python Client ' + detectlanguage.__version__
	secure = False
