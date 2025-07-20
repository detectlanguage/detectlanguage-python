import detectlanguage

def detect(data):
	if isinstance(data, list):
		raise ValueError('use detect_batch instead for multiple texts')

	return detectlanguage.client.post('detect', { 'q': data })

def detect_code(data):
	result = detect(data)
	return result[0]['language']

def detect_batch(data):
	return detectlanguage.client.post('detect-batch', { 'q': data })

def account_status():
	return detectlanguage.client.get('account/status')

def languages():
	return detectlanguage.client.get('languages')
