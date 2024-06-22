class DataSelectorPlainPython:
    """
    Partial implementation of a class to hold a data selector widget.
    """
    def __init__(
        self,
        year_range_input=(1800, 2000),
        window_size=2,
        polynomial_order=1,
    ):
        self.year_range = year_range_input
        self.window_size = window_size
        self.polynomial_order = polynomial_order
