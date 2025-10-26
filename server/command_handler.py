"""
Command handling and task management
"""

import logging
from database import DatabaseManager

class CommandHandler:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available_commands = {
            'system_info': self._get_system_info,
            'execute_command': self._execute_command,
            'file_list': self._list_files,
            'download_file': self._download_file
        }
    
    def process_command(self, agent_id: str, command: str, args: dict) -> dict:
        """Process incoming commands from operators"""
        if command not in self.available_commands:
            return {"status": "error", "message": f"Unknown command: {command}"}
        
        try:
            result = self.available_commands[command](agent_id, args)
            return {"status": "success", "result": result}
        except Exception as e:
            logging.error(f"Command execution error: {e}")
            return {"status": "error", "message": str(e)}
    
    def _get_system_info(self, agent_id: str, args: dict) -> dict:
        """Get system information from agent"""
        return {"command": "system_info", "pending": True}
    
    def _execute_command(self, agent_id: str, args: dict) -> dict:
        """Execute system command on agent"""
        cmd = args.get('command', '')
        return {"command": "execute", "cmd": cmd, "pending": True}
    
    def _list_files(self, agent_id: str, args: dict) -> dict:
        """List files in directory"""
        path = args.get('path', '.')
        return {"command": "file_list", "path": path, "pending": True}
    
    def _download_file(self, agent_id: str, args: dict) -> dict:
        """Download file from agent"""
        file_path = args.get('file_path', '')
        return {"command": "download_file", "file_path": file_path, "pending": True}