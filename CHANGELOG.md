# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## v2.0.0

### Added
- `detect_batch` method for batch detections
- Proxy support

### Changed
- Switched to v3 API which uses updated language detection model
- ⚠️ `detect` method result fields are `language` and `score`

### Deprecated
- Calling `detect()` with list argument. Use `detect_batch` instead.
- `simple_detect()` - Use `detect_code()` instead. Will be removed in a future version.
- `user_status()` - Use `account_status()` instead. Will be removed in a future version.

### Removed
- Secure mode configuration. HTTPS is used by default.
