import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_typical_case():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6   # Standard LeetCode example
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15                   # All positive, entire array is best
    assert max_subarray_sum([-1, 2, 3, -1, 4]) == 8                  # Subarray in the middle

def test_single_element():
    assert max_subarray_sum([5]) == 5                                 # Single positive number
    assert max_subarray_sum([-5]) == -5                               # Single negative number
    assert max_subarray_sum([0]) == 0                                 # Single zero

def test_all_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1                       # Least negative is the answer
    assert max_subarray_sum([-10, -5, -20]) == -5                     # Least negative in middle
    assert max_subarray_sum([-1, -1, -1]) == -1                       # All equal negatives

def test_mixed_with_zeros():
    assert max_subarray_sum([0, 0, 0]) == 0                           # All zeros
    assert max_subarray_sum([-2, 0, -3]) == 0                         # Zero is the best subarray
    assert max_subarray_sum([0, -1, 2, 0]) == 2                       # Positive surrounded by zeros

def test_empty_list():
    assert max_subarray_sum([]) == 0                                  # Edge case: empty list

def test_large_values():
    assert max_subarray_sum([100000, -1, 100000]) == 199999           # Large numbers
    assert max_subarray_sum([-100000, 100000]) == 100000              # Large negative and positive

if __name__ == "__main__":
    pytest.main()