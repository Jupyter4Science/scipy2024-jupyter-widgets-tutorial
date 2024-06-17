
def on_window_size_change(change):
    global original_df, selected_df # Remember to access the global variables
    # catch the change in the window_size widget value and update the original_df
    original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'],
                                                 change['new'],
                                                 poly_order.value).round(decimals=3) # original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'], window_size, poly_order).round(decimals=3)
    selected_df = original_df[(original_df['Year'] >= year_range.value[0])
                              & (original_df['Year'] <= year_range.value[1])]