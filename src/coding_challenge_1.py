from typing import Any, List, Dict, Union

def concatenate(items: List[Any]) -> Union[int, float, str, List[Any], Dict[Any, Any]]:
    """
    Concatenate a list of elements depending of their type:
      - int / float  → sum
      - str         → string joined by '|'
      - bool        → '1' for True, '0' for False, concatenated string
      - list        → concatenated list with the sublists merged
      - dict        → merged dictionary (the last value of the same key overrides the previous one.)
    Raise:
      - ValueError if the list is empty
      - TypeError if there are mixed types or unsupported types.
    """
    if not items:
        raise ValueError("The list is empty, impossible to concatenate.")

    # 1) bool first (bool is a subclass of int)
    if all(isinstance(x, bool) for x in items):
        return ''.join('1' if x else '0' for x in items)

    # 2) numeric (int or float, but not bool)
    if all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in items):
        return sum(items)  # float if at least one float

    # 3) strings
    if all(isinstance(x, str) for x in items):
        return '|'.join(items)

    # 4) lists
    if all(isinstance(x, list) for x in items):
        result: List[Any] = []
        for lst in items:
            result.extend(lst)
        return result

    # 5) dictionaries
    if all(isinstance(x, dict) for x in items):
        result: Dict[Any, Any] = {}
        for d in items:
            result.update(d)
        return result

    # otherwise mixed types / unsupported types
    raise TypeError("All elements must be of the same type and supported (int/float, str, bool, list or dict).")
