Detect Language API Python Client
========

[![PyPI version](https://badge.fury.io/py/detectlanguage.svg)](https://badge.fury.io/py/detectlanguage)
[![Build Status](https://api.travis-ci.org/detectlanguage/detectlanguage-python.svg)](http://travis-ci.org/detectlanguage/detectlanguage-python)

Detects language of given text. Returns detected language codes and scores.

Before using Detect Language API client you have to setup your personal API key.
You can get it by signing up at https://detectlanguage.com

## Installation

```
pip install detectlanguage
```

### Configuration

```python
import detectlanguage

detectlanguage.configuration.api_key = "YOUR API KEY"

# Enable secure mode (SSL) if you are passing sensitive data
# detectlanguage.configuration.secure = True
```

## Usage

### Language detection

```python
detectlanguage.detect("Buenos dias señor")
```

#### Result

```python
[{'isReliable': True, 'confidence': 12.04, 'language': 'es'}]
```

### Simple language detection

If you need just a language code you can use `simple_detect`. It returns just the language code.

```python
detectlanguage.simple_detect("Buenos dias señor")
```

#### Result

```python
'es'
```

### Batch detection

It is possible to detect language of several texts with one request.
This method is faster than doing one request per text.
To use batch detection just pass array of texts to `detect` method.

```python
detectlanguage.detect(["Buenos dias señor", "Labas rytas"])
```

#### Result

Result is array of detections in the same order as the texts were passed.

```python
[ [ {'isReliable': True, 'confidence': 12.04, 'language': 'es'} ],
  [ {'isReliable': True, 'confidence': 9.38, 'language': 'lt'} ] ]
```

### Getting your account status

```python
detectlanguage.user_status()
```

#### Result

```python
{ 'status': 'ACTIVE', 'daily_requests_limit': 5000, 'daily_bytes_limit': 1048576,
  'bytes': 3151, 'plan': 'FREE', 'date': '2014-03-29', 'requests': 263,
  'plan_expires': None }
```

### Getting list detectable languages

```python
detectlanguage.languages()
```

#### Result

Array of language codes and names.

## Contribution

You are welcome to patch and send GitHub pull requests.

### Testing

    pip install -r requirements.txt
    pip install -r test-requirements.txt
    nosetests

## License

Detect Language API Python Client is free software, and may be redistributed under the terms specified in the MIT-LICENSE file.
