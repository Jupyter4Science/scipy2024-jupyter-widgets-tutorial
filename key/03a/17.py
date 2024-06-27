constraint_check = DataSelectorModelDraft6()

# This should work, since polynomial_order is 1 by default
constraint_check.window_size = 5

# This should fail, since polynomial_order is larger than window_size
constraint_check.polynomial_order = 6
