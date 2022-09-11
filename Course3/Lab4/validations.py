

import re

def validate_user(username, minlen):
    if len(username) < minlen:
        return False
    if not re.match('^[a-z0-9._]*$', username):
        return False
    if username[0].isnumeric():
        return False
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    return True

print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be Fals#!/usr/bin/env python3

