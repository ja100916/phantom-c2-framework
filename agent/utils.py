"""
Utility functions for the agent
"""

import hashlib
import random
import string

def generate_agent_id() -> str:
    """Generate a unique agent ID"""
    system_info = f"{platform.node()}{platform.platform()}{os.urandom(16)}"
    return hashlib.sha256(system_info.encode()).hexdigest()[:16]

def jitter_sleep(base_interval: int, jitter: float = 0.3) -> float:
    """Calculate sleep time with jitter"""
    jitter_amount = base_interval * jitter
    return base_interval + random.uniform(-jitter_amount, jitter_amount)

def random_string(length: int = 8) -> str:
    """Generate a random string"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))