import solution
import pytest

@pytest.fixture
def _s():
    return solution.Solution()

def test_pivotIndex_case_one_should_return_correct(_s):
    assert _s.pivotIndex([1,7,3,6,5,6]) == 3

def test_pivotIndex_case_two_should_return_correct(_s):
    assert _s.pivotIndex([1,2,3]) == -1

def test_pivotIndex_case_three_should_return_correct(_s):
    assert _s.pivotIndex([2,1,-1]) == 0

@pytest.mark.parametrize("nums", [
    ([3]),
    ([1234]),
    ([-456])
])
def test_pivotIndex_input_len_one_should_return_0(_s, nums):
    assert _s.pivotIndex(nums) == 0

@pytest.mark.parametrize("nums,expected", [
    ([1,1,1,-3,9], 4),
    ([1,2,1,1,-5,8], 5)
])
def test_pivotIndex_should_return_last_index_when_pivot_at_end(_s, nums, expected):
    assert _s.pivotIndex(nums) == expected

@pytest.mark.parametrize("nums,expected", [
    ([1,3,1,-5,5], 1),
    ([1,5,1,-7,7], 1)
])
def test_pivotIndex_should_return_leftmost_when_multiple_pivots(_s, nums, expected):
    assert _s.pivotIndex(nums) == expected
