import unittest
from unittest.mock import patch, MagicMock
import detectlanguage


class TestProxyConfiguration(unittest.TestCase):
    def setUp(self):
        detectlanguage.configuration.proxies = None

    def test_proxy_configuration(self):
        """Test proxy configuration"""
        detectlanguage.configuration.proxies = {'https': 'https://proxy.example.com:8080'}
        self.assertEqual(detectlanguage.configuration.proxies, {'https': 'https://proxy.example.com:8080'})

    @patch('requests.get')
    def test_client_uses_proxy(self, mock_get):
        """Test that client uses configured proxy"""
        detectlanguage.configuration.proxies = {'https': 'https://proxy.example.com:8080'}
        
        mock_response = MagicMock()
        mock_response.json.return_value = {'test': 'data'}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        detectlanguage.account_status()
        
        mock_get.assert_called_once()
        self.assertEqual(mock_get.call_args[1]['proxies'], {'https': 'https://proxy.example.com:8080'})

    @patch('requests.get')
    def test_client_no_proxy_when_disabled(self, mock_get):
        """Test that client doesn't use proxy when disabled"""
        detectlanguage.configuration.proxies = None
        
        mock_response = MagicMock()
        mock_response.json.return_value = {'test': 'data'}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        detectlanguage.account_status()
        
        mock_get.assert_called_once()
        self.assertIsNone(mock_get.call_args[1]['proxies'])


if __name__ == '__main__':
    unittest.main() 