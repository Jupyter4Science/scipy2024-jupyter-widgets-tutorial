
def on_window_size_change(change):
    global original_df, selected_df # Remember to access the global variables
    original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'], change['new'], poly_order.value) # original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'], window_size, poly_order)
    selected_df = original_df[(original_df['Year'] >= year_range.value[0]) & (original_df['Year'] <= year_range.value[1])]