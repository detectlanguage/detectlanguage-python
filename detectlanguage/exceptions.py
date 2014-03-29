class DetectLanguageError(BaseException):
	def __init__(self, *args, **kwargs):
		super(DetectLanguageError, self).__init__(*args, **kwargs)
