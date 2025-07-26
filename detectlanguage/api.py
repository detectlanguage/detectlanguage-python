import detectlanguage
import warnings

def detect(data):
	if isinstance(data, list):
		_warn_deprecated('use detect_batch instead for multiple texts')
		return detect_batch(data)

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


### DEPRECATED

def simple_detect(data):
    """
    DEPRECATED: This function is deprecated and will be removed in a future version.
    Use detect_code() instead.

    Args:
        data: Text to detect language for

    Returns:
        str: Language code of the detected language
    """
    _warn_deprecated(
        "simple_detect() is deprecated and will be removed in a future version. "
        "Use detect_code() instead."
    )
    return detect_code(data)

def user_status():
    """
    DEPRECATED: This function is deprecated and will be removed in a future version.
    Use account_status() instead.

    Returns:
        dict: Account status information
    """
    _warn_deprecated(
        "user_status() is deprecated and will be removed in a future version. "
        "Use account_status() instead."
    )
    return account_status()

def _warn_deprecated(message):
    """Internal utility function to emit deprecation warnings."""
    warnings.warn(
        message,
        DeprecationWarning,
        stacklevel=2
    )
