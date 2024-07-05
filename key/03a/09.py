@dataclass
class DataSelectorDataClass:
    """
    A class to hold a data selector widget using dataclasses.
    """
    year_range: tuple = (1800, 2000)
    window_size: int = 2
    polynomial_order: int = 1
