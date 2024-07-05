class DataSelectorModelDraft5(BaseModel, validate_assignment=True):
    year_range: tuple[int, int] = (1800, 2000)
    window_size: Annotated[int, Field(ge=2, le=100)] = 2
    polynomial_order: Annotated[int, Field(ge=1, le=10)] = 1
