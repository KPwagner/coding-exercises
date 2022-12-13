import pytest
import solution

def test_base_case_one_should_return_true():
    assert solution.isSubsequence("abc", "ahbgdc") == True

def test_base_case_two_should_return_false():
    assert solution.isSubsequence("axc", "ahbgdc") == False

def test_empty_string_s_returns_true():
    assert solution.isSubsequence("", "abcdcb") == True

def test_empty_string_t_returns_true():
    assert solution.isSubsequence("abcdcb", "") == False

@pytest.mark.parametrize("s,t,expected", [
    ("aabbcc", "abababababcabc", True),
    ("aabbcc", "abaabbbcabc", True),
    ("aabbcc", "abaabcabc", False),
])
def test_repeating_s_chars_should_return_correctly(s ,t ,expected):
    assert solution.isSubsequence(s, t) == expected

@pytest.mark.parametrize("s,t,expected", [
    ("aabbcc", "abababababcabc", True),
    ("aabbcc", "abaabbbcabc", True),
    ("aabbcc", "abaabcabc", False),
    ("xyzz", "zzyxzyxz", False),
])
def test_repeating_s_chars_should_return_correctly(s ,t ,expected):
    assert solution.isSubsequence(s, t) == expected