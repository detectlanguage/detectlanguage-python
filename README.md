Detect Language API Python Client
========

[![PyPI version](https://badge.fury.io/py/detectlanguage.svg)](https://badge.fury.io/py/detectlanguage)
[![Build Status](https://github.com/detectlanguage/detectlanguage-python/actions/workflows/main.yml/badge.svg)](https://github.com/detectlanguage/detectlanguage-python/actions)

Detects language of given text. Returns detected language codes and scores.

Before using Detect Language API client you have to setup your personal API key.
You can get it by signing up at https://detectlanguage.com

## Installation

```
pip install detectlanguage
```

### Upgrading

When upgrading please check [changelog](CHANGELOG.md) for breaking changes.

### Configuration

```python
import detectlanguage

detectlanguage.configuration.api_key = "YOUR API KEY"

# You can use proxy if needed
# detectlanguage.configuration.proxies = {'https': 'https://user:pass@proxy:8080'}
```

## Usage

### Detect language

```python
detectlanguage.detect("Dolce far niente")
```

#### Result

```python
[{'language': 'it', 'score': 0.5074}]
```

### Detect single code

If you need just a language code you can use `detect_code`.

```python
detectlanguage.detect_code("Dolce far niente")
```

#### Result

```python
'it'
```

### Batch detection

It is possible to detect language of several texts with one request.
This method is faster than doing one request per text.

```python
detectlanguage.detect_batch(["Dolce far niente", "Hello world"])
```

#### Result

Result is array of detections in the same order as the texts were passed.

```python
[[{'language': 'it', 'score': 0.5074}], [{'language': 'en', 'score': 0.9098}]]
```

### Get your account status

```python
detectlanguage.account_status()
```

#### Result

```python
{ 'status': 'ACTIVE', 'daily_requests_limit': 5000, 'daily_bytes_limit': 1048576,
  'bytes': 3151, 'plan': 'FREE', 'date': '2014-03-29', 'requests': 263,
  'plan_expires': None }
```

### Get list of supported languages

```python
detectlanguage.languages()
```

#### Result

```python
[{'code': 'aa', 'name': 'Afar'}, {'code': 'ab', 'name': 'Abkhazian'}, ...]
```

## License

Detect Language API Python Client is free software, and may be redistributed under the terms specified in the MIT-LICENSE file.
