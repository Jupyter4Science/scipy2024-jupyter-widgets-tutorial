# Outline for 2024 widget tutorial

## Outline is based on the proposal; modifications are welcome

**Last Updated:** June 18, 2024

1. `nbdev` motivation and demonstration -- essentially follow part of 2023 tutorial. **[Drafted, awaiting review]**
    a. Motivation for using nbdev -- generating python modules from notebooks, mention the other features we are not exploring.
    b. "Gotchas"  when using nbdev, e.g. generating code that doesn't execute without some of the notebook cells.
    c. Build dashboard from 2023.
    
2. Intro to widgets **[Drafted, awaiting review]**
    a. Follow the rough flow of notebook 01 from 2023, introducing one of the widgets (e.g. slider) that we will use later. Also include list/widget showing all the widgets.
    b. Demo showing a pandas dataframe with ipydatagrid
    
3. Build same dashboard with pydantic + ipyautoui **[Matt handling this]**
    a. Intro classes
    b. Intro type annotations
    c. Intro pydantic
    d. Express constraints of smoothing window/order in pydantic
    e. Generate control widget with ipyautoui
    f. Connect control widget to dashboard
    
4. Deployment options -- we do NOT need to demonstrate all of these
	- Server-side processing
    a. Binder [Mostly done in README.] **[Nicole has a notebook on this?]**
     b. Nabari(?) **[Juan can look into this]**
     c. Voila **[Nicole has a notebook]**
	- Client-side processing
    a. voici (builds a jupyter lite bundle) on github pages(?) **[Juan]**
     b. nbdev can export some content to static pages using Quarto **[Nicole]**
     c. sphinx (depends on how far along? Depends on Jupyter lite)
     d.. Pycafe ([Examine this link](https://py.cafe/maartenbreddels/ipyvolume-3d-vector-field))
   
   - Alternative Approach: Build dashboard with solara (10-30 minutes) **[Maarten]**
