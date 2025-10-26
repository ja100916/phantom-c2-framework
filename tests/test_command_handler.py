"""
Tests for command handler
"""

import unittest
from server.command_handler import CommandHandler
from server.database import DatabaseManager

class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(":memory:")  # In-memory DB for testing
        self.handler = CommandHandler(self.db)
    
    def test_unknown_command(self):
        result = self.handler.process_command("test123", "unknown_cmd", {})
        self.assertEqual(result["status"], "error")
    
    def test_valid_command(self):
        result = self.handler.process_command("test123", "system_info", {})
        self.assertEqual(result["status"], "success")

if __name__ == '__main__':
    unittest.main()