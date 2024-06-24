# AUTOGENERATED! DO NOT EDIT! File to edit: ../03a_pydantic.ipynb.

# %% auto 0
__all__ = ['DataSelectorModelDraft6']

# %% ../03a_pydantic.ipynb 97
from typing import Annotated
from pydantic import model_validator, BaseModel, Field

# %% ../03a_pydantic.ipynb 98
class DataSelectorModelDraft6(BaseModel, validate_assignment=True):
    year_range: tuple[int, int] = (1800, 2000)
    window_size: Annotated[int, Field(ge=2, le=100)] = 2
    polynomial_order: Annotated[int, Field(ge=1, le=10)] = 1

    # mode="after" means the validator runs after pydantic has checked that the individual
    # fields have values that are valid.
    @model_validator(mode="after")
    def limit_polynomial_order(self):
        
        if self.polynomial_order > self.window_size - 1:
            # Handle a bad polynomial order or window size
            raise ValueError("Polynomial order must be smaller than window size")
            
        # If we got this far the polynomial order is consistent with the window size
        # so return self. Failing to return self will end up causing an error.
        return self
