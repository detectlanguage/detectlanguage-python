import detectlanguage

def detect(data):
	result = detectlanguage.client.post('detect', { 'q': data })
	return result['data']['detections']

def simple_detect(data):
	result = detect(data)
	return result[0]['language']

def user_status():
	return detectlanguage.client.get('user/status')

def languages():
	return detectlanguage.client.get('languages')

