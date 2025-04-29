from typing import Optional

def is_balanced(input_string: Optional[str]) -> bool:
    """
    Check whether a string has properly balanced grouping symbols:
      - parentheses:      ( )
      - square brackets: [ ]
      - curly braces:     { }
    and ignores any symbols that appear inside C-style comments: /* ... */.

    Rules:
      - Opening tokens must be matched by the corresponding closing token in the correct order.
      - Comments start with '/*' and end at the next '*/'. Comment markers do NOT nest.
      - Any grouping symbols inside a comment are ignored completely.
      - An unclosed comment (i.e. a '/*' without a following '*/') makes the string unbalanced.
      - A '*/' outside of an open comment is treated as ordinary text (and thus ignored).
      - Null (None) or empty strings are considered balanced.

    Parameters:
    -----------
    input_string : Optional[str]
        The input string to check. If None or "", returns True.

    Returns:
    --------
    bool
        True if all symbols are properly balanced (and comments properly closed), False otherwise.

    Raises:
    -------
    TypeError
        If `input_string` is not a string or None.
    """
    if input_string is None or input_string == "":
        return True

    if not isinstance(input_string, str):
        raise TypeError(f"Expected string or None, got {type(input_string).__name__!r}")

   
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    in_comment = False
    i = 0
    n = len(input_string)

    while i < n:
        # start comment
        if not in_comment and input_string[i] == '/' and i+1 < n and input_string[i+1] == '*':
            in_comment = True
            i += 2
            continue

        # end comment
        if in_comment and input_string[i] == '*' and i+1 < n and input_string[i+1] == '/':
            in_comment = False
            i += 2
            continue

        if in_comment:
            i += 1
            continue

        # outside comment: check for grouping symbols
        ch = input_string[i]
        if ch in pairs.values():            # opening symbol
            stack.append(ch)
        elif ch in pairs:                   # closing symbol
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        # else: ignore all other characters
        i += 1

    # at end, must not be inside a comment and stack must be empty
    return (not in_comment) and (not stack)
