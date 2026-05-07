"""Sum operation."""


class Sum:
    """Sum operation class for multiple values."""

    def __init__(self, values: list[int]) -> None:
        """Initialize Sum with a list of values.

        Args:
            values: List of integers to sum.

        """
        self.values = values

    def compute(self) -> int:
        """Compute the sum of all values.

        Returns:
            The arithmetic sum of all values.

        """
        return sum(self.values)
