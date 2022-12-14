import solution
import pytest

@pytest.fixture
def s():
    return solution.Solution()

def test_case_one_returns_correct(s):
    result = s.runningSum([1,2,3,4])
    assert result == [1,3,6,10]

def test_case_two_returns_correct(s):
    result = s.runningSum([1,1,1,1,1])
    assert result == [1,2,3,4,5]

def test_case_three_returns_correct(s):
    result = s.runningSum([3,1,2,10,1])
    assert result == [3,4,6,16,17]


