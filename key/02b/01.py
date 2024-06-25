
def on_window_size_change(change):
    global original_df, selected_df # Remember to access the global variables
    # Update the following call to set the original_df['Smoothed Data'] column
    # values to properly capture the change in window_size value and the
    # current poly_order value.
    original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'],
                                                 change['new'],
                                                 poly_order.value).round(decimals=3)
    selected_df = original_df[(original_df['Year'] >= year_range.value[0])
                              & (original_df['Year'] <= year_range.value[1])]