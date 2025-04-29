import pytest
from src.coding_challenge_2 import is_balanced

def test_none_and_empty_are_balanced():
    assert is_balanced(None) is True
    assert is_balanced("") is True

def test_single_pairs():
    assert is_balanced("()") is True
    assert is_balanced("[]") is True
    assert is_balanced("{}") is True

def test_nested_balanced():
    s = "( { [ () [] ] } )"
    assert is_balanced(s) is True

def test_simple_unbalanced():
    assert is_balanced("(]") is False
    assert is_balanced("([)]") is False
    assert is_balanced("(()") is False

def test_symbols_outside_comment_ignored():
    # '*/' outside comment is just text
    assert is_balanced("*/") is True

def test_comment_only():
    assert is_balanced("/* this is a comment */") is True

def test_unclosed_comment_is_unbalanced():
    assert is_balanced("/* not closed") is False
    assert is_balanced("prefix /* abc") is False

def test_ignore_symbols_inside_comment():
    # brackets inside comment are ignored
    string1 = "/* ([{ < > }]) */"
    assert is_balanced(string1) is True
    # comment ends, then an unmatched closing bracket
    string2 = "/* ([{ })) */]"
    assert is_balanced(string2) is False

def test_comment_markers_do_not_nest():
    # the first '*/' closes the comment, the trailing '*/' is ignored as plain text
    s = "/* abcd /* efgh */ ijkl */"
    assert is_balanced(s) is True

def test_mixed_content():
    s = "{ foo(/* [ ] */), bar }"
    assert is_balanced(s) is True

def test_mismatch_after_comment():
    # comment hides matching, but then we close wrong one
    s = "/* ( [ */ )"
    # the '(' and '[' are in comment; ')' outside is unmatched
    assert is_balanced(s) is False

def test_non_string_type_error():
    with pytest.raises(TypeError):
        is_balanced(123)   # not a str or None
    with pytest.raises(TypeError):
        is_balanced(["]"]) # not a str or None
