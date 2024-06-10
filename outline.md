# Outline for 2024 widget tutorial

## Outline is based on the proposal; modifications are welcome

1. Intro to widgets
    a. Follow the rough flow of notebook 01 from 2023, introducing one of the widgets (e.g. slider) that we will use later. Also include list/widget showing all the widgets.
    b. Demo showing a pandas dataframe with ipydatagrid
2. `nbdev` motivation and demonstration -- essentially follow part of 2023 tutorial.
    a. Motivation for using nbdev -- generating python modules from notebooks, mention the other features we are not exploring.
    b. "Gotchas"  when using nbdev, e.g. generating code that doesn't execute without some of the notebook cells.
    c. Build dashboard from 2023.
3. Build same dashboard with pydantic + ipyautoui
    a. Intro classes
    b. Intro type annotations
    c. Intro pydantic
    d. Express constraints of smoothing window/order in pydantic
    e. Generate control widget with ipyautoui
    f. Connect control widget to dashboard
4. Build dashboard with solara
4. Deployment options -- we do NOT need to demonstrate all of these
    a. Voila
    b. github pages
    c. voici (builds a jupyter lite bundle)
    d. sphinx
