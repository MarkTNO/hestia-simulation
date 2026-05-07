import pytest

from hestia_simulation import Add, Sum


def test_add_returns_sum() -> None:
    """Verify that Add.compute returns the arithmetic sum for integer inputs.

    :returns: None. Passes when the computed sum equals the expected value.
    """
    add_op = Add(2, 5)
    assert add_op.compute() == 7


def test_add_with_negative_numbers() -> None:
    """Verify that Add.compute works correctly with negative numbers.

    :returns: None. Passes when the computed sum is correct.
    """
    add_op = Add(-2, 5)
    assert add_op.compute() == 3


def test_sum_returns_sum_of_list() -> None:
    """Verify that Sum.compute returns the sum of a list of integers.

    :returns: None. Passes when the computed sum equals the expected value.
    """
    sum_op = Sum([1, 2, 3, 4, 5])
    assert sum_op.compute() == 15


def test_sum_with_empty_list() -> None:
    """Verify that Sum.compute returns 0 for an empty list.

    :returns: None. Passes when the computed sum is 0.
    """
    sum_op = Sum([])
    assert sum_op.compute() == 0


def test_add_raises_type_error_with_invalid_types() -> None:
    """Verify that Add.compute raises TypeError for invalid operand types.

    :raises TypeError: Raised when attempting to add incompatible types.
    :returns: None. Passes when TypeError is raised.
    """
    add_op = Add(2, "3")  # type: ignore
    with pytest.raises(TypeError):
        add_op.compute()
