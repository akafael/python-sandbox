"""
    Check if brackets ein a given string are balanced
    @author Akafael
"""

# !/usr/bin/env python


def brackets_match(line):
    """Return True if brackets in a given string are balanced
    :type line: basestring

    Examples:
    >>> brackets_match("f(e(d))")
    True
    >>> brackets_match("((b)")
    False
    >>> brackets_match("(]")
    False
    >>> brackets_match(")(")
    False
    >>> brackets_match("")
    False
    """

    # Trivial Case: Empty String
    if not line:
        return False

    # Count occurrences and find location
    count = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
    position = {'(': [], ')': [], '{': [], '}': [], '[': [], ']': []}
    i = 0
    for letter in line:
        if letter == '(':
            count['('] += 1
            position['('] = i
        elif letter == ')':
            count[')'] += 1
            position[')'] = i
        elif letter == '{':
            count['{'] += 1
            position['{'] = i
        elif letter == '}':
            count['}'] += 1
            position['}'] = i
        elif letter == '[':
            count['['] += 1
            position['['] = i
        elif letter == ']':
            count[']'] += 1
            position[']'] = i

        i += 1
    # Standard Case: Count Same Number of Occurrences of both sides
    is_matching_amount = (count['('] == count[')']) and (count['{'] == count['}']) and (count['['] == count[']'])
    if not is_matching_amount:
        return False

    # Trick Case: Count Same Number of Occurrences of both sides
    if count['('] == count[')']:
        for j in range(count['(']):
            if position['('][j] > position['('][j]:
                return False
    if count['['] == count[']']:
        for j in range(count['[']):
            if position['['][j] > position['('][j]:
                return False
    if count['{'] == count['}']:
        for j in range(count['{']):
            if position['{'][j] > position['}'][j]:
                return False

    return is_matching_amount


if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()
