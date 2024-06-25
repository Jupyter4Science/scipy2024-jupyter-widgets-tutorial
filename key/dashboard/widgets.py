# AUTOGENERATED! DO NOT EDIT! File to edit: ../02b_widgets.ipynb.

# %% auto 0
__all__ = ['DATA_DIR', 'DATA_FILE', 'original_df', 'year_range', 'selected_df', 'selected_data_grid', 'window_size', 'poly_order',
           'plot_view', 'on_range_change', 'update_selected_datagrid', 'on_poly_order_change', 'on_window_size_change',
           'output_plot']

# %% ../02b_widgets.ipynb 7
import pandas as pd
import os
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter
import ipywidgets as widgets # add import statement for Jupyter widgets

# %% ../02b_widgets.ipynb 11
# Load data into memory from file
DATA_DIR = 'data'
DATA_FILE = 'land-ocean-temp-index.csv'

original_df = pd.read_csv(os.path.join(DATA_DIR, DATA_FILE), escapechar='#')

# %% ../02b_widgets.ipynb 14
year_range = widgets.IntRangeSlider(description = 'Range of Years',
                                    style={'description_width': 'initial'})
# The style argument is used to set the width of the description wide enough
# to display the entire text

# %% ../02b_widgets.ipynb 20
year_range.max =  max(original_df['Year']) # set the 'max' attribute of the slider to the minimum year of the our data
year_range.min = min(original_df['Year'])  # and let's do the same for 'min'

# %% ../02b_widgets.ipynb 26
selected_df = original_df[(original_df['Year'] >= year_range.value[0]) & (original_df['Year'] <= year_range.value[1])] # selected_df = original_df[(original_df['Year'] >= from_year) & (original_df['Year'] <= to_year)]

# %% ../02b_widgets.ipynb 36
# Create a function that will change the selected_df based on the range of
# years selected by the user using the year_range widget
def on_range_change(change):
    global selected_df
    selected_df = original_df[(original_df['Year'] >= change['new'][0])
                              & (original_df['Year'] <= change['new'][1])]
    # WARNING: You could have thought to use:
    #  selected_df = original_df[(original_df['Year'] >= year_range.value[0])
    #                             & (original_df['Year'] <= year_range.value[1])]
    # but for many manual interactions, such as a click and drag slider, a high
    # overturn of quickly changing widget values could silently cause
    # unexpected behavior in changing values, so that syntax should be avoided

# %% ../02b_widgets.ipynb 46
year_range.observe(on_range_change, 'value') # year_range.observe()

# %% ../02b_widgets.ipynb 62
from ipydatagrid import DataGrid

# Define a DataGrid widget containing our Pandas dataframe setting column and row sizes
selected_data_grid = DataGrid(selected_df, header_visibility="column", auto_fit_columns=True)

# %% ../02b_widgets.ipynb 65
# Create a handler function that will display the selected dataframe
def update_selected_datagrid(change):
    selected_data_grid.data = selected_df

# Attach the handler function to the year_range widget
year_range.observe(update_selected_datagrid, 'value')

# %% ../02b_widgets.ipynb 71
window_size = widgets.IntSlider(description = 'Window Size', value=20, min=2, max=100,
                                style={'description_width': 'initial'})

# %% ../02b_widgets.ipynb 74
poly_order = widgets.BoundedIntText(description = 'Poly Order', min=1, value=3, max=10,
                                    style={'description_width': 'initial'})

# %% ../02b_widgets.ipynb 84
def on_poly_order_change(change):
    global original_df, selected_df
    # Change the following line that sets the 'Smoothed Data' column of original_df
    # to catch the change in poly_order widget value and update the original_df for it.
    # Remember to also catch the current window_size value.
    original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'],
                                                 window_size.value,
                                                 change['new']).round(decimals=3)
    selected_df = original_df[(original_df['Year'] >= year_range.value[0])
                              & (original_df['Year'] <= year_range.value[1])]

# %% ../02b_widgets.ipynb 85
poly_order.observe(on_poly_order_change, 'value')
window_size.observe(update_selected_datagrid, 'value')

# %% ../02b_widgets.ipynb 90
def on_window_size_change(change):
    global original_data, selected_df, poly_order
    poly_order.max = min(10, change['new'] - 1) # change the maximum of the poly_order widget
    # catch the change in the window_size widget value and update the original_df
    original_df['Smoothed Data'] = savgol_filter(original_df['Temperature'],
                                                 change['new'],
                                                 poly_order.value).round(decimals=3)
    selected_df = original_df[(original_df['Year'] >= year_range.value[0])
                              & (original_df['Year'] <= year_range.value[1])]

# %% ../02b_widgets.ipynb 92
window_size.observe(on_window_size_change, 'value')
window_size.observe(update_selected_datagrid, 'value')

# %% ../02b_widgets.ipynb 96
window_size.value = 10
poly_order.value = 1

# %% ../02b_widgets.ipynb 100
plot_view = widgets.Output() # create an output widget called plot_view

# %% ../02b_widgets.ipynb 102
def output_plot(change):
    plot_view.clear_output(wait=True)
    with plot_view:  # Add with content handler for `plot_view`
        plt.xlabel('Year')
        plt.ylabel('Temperature Anomalies over Land w.r.t. 1951-80 (˚C)')
        plt.title('Global Annual Mean Surface Air Temperature Change')
        plt.plot(selected_df['Year'], selected_df['Temperature'], label='Raw Data')
        plt.plot(selected_df['Year'], selected_df['Smoothed Data'], label='Smoothed Data')
        plt.legend()
        plt.show()

# %% ../02b_widgets.ipynb 107
year_range.observe(output_plot, 'value')
window_size.observe(output_plot, 'value')
poly_order.observe(output_plot, 'value')

# %% ../02b_widgets.ipynb 109
year_range.value = (1900, 2000)
