"""
Tests for cryptographic utilities
"""

import unittest
from server.crypto_utils import CryptoUtils

class TestCryptoUtils(unittest.TestCase):
    def setUp(self):
        self.crypto = CryptoUtils()
    
    def test_encrypt_decrypt_string(self):
        test_data = "Hello, Phantom C2!"
        encrypted = self.crypto.encrypt(test_data)
        decrypted = self.crypto.decrypt(encrypted)
        self.assertEqual(test_data, decrypted)
    
    def test_encrypt_decrypt_dict(self):
        test_data = {"agent_id": "test123", "command": "system_info"}
        encrypted = self.crypto.encrypt(test_data)
        decrypted = self.crypto.decrypt(encrypted)
        self.assertEqual(test_data, eval(decrypted))

if __name__ == '__main__':
    unittest.main()