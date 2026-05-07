"""Addition operation."""


class Add:
    """Addition operation class."""

    def __init__(self, left: int, right: int) -> None:
        """Initialize Add with two operands.

        :param left: First operand.
        :param right: Second operand.
        """
        self.left = left
        self.right = right

    def compute(self) -> int:
        """Compute the sum of the operands.

        :returns: The arithmetic sum of left and right.
        """
        return self.left + self.right
