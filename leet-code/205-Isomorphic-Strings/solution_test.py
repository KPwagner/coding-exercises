import solution
import pytest

@pytest.mark.parametrize("s,t,expected", [
    ('egg', 'add', True),
    ('foo', 'bar', False),
    ('paper', 'title', True),
])
def test_isIsometric_should_return_correctly_for_base_cases(s,t,expected):
    result = solution.isIsomorphic(s,t)
    assert result == expected

@pytest.mark.parametrize("s,t", [
    ('a', 'ac'),
    ('aab', 'abbc')
])
def test_isIsometric_should_return_false_when_sets_not_equal_length(s,t):
    result = solution.isIsomorphic(s,t)
    assert result == False

@pytest.mark.parametrize("s,t,expected", [
    ('baba', 'abab', True),
    ('abcabc', 'bcabca', True)
])
def test_isIsometric_should_handle_duplicate_replacing(s,t,expected):
    result = solution.isIsomorphic(s,t)
    assert result == expected

@pytest.mark.parametrize("s,t,expected", [
    ('baba', 'abcd', False),
    ('toratora', 'torabora', False)
])
def test_isIsometric_should_not_allow_multiple_mapping_s_to_t(s,t,expected):
    result = solution.isIsomorphic(s,t)
    assert result == expected

@pytest.mark.parametrize("s,t,expected", [
    ('abcd', 'baba', False),
    ('torabora', 'toratora', False)
])
def test_isIsometric_should_not_allow_multiple_mapping_t_to_s(s,t,expected):
    result = solution.isIsomorphic(s,t)
    assert result == expected