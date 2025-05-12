# src/utils.py

import uuid
import re
from datetime import datetime

def is_valid_date_format_yyyy_mm_dd(date_string):
    """Check if the date is in YYYY-MM-DD format."""
    try:
        if not isinstance(date_string, str):
            return False
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
            return False
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def generate_unique_visit_id(existing_ids):
    """Generate a unique 8-character visit ID that isn't already used."""
    existing_ids = set(str(x).strip() for x in existing_ids)
    for _ in range(100):
        new_id = uuid.uuid4().hex[:8].upper()
        if new_id not in existing_ids:
            return new_id
    raise RuntimeError("Unable to generate a unique Visit ID after 100 tries.")
