import streamlit as st
import pandas as pd

data = pd.read_csv('car_data.csv')

st.sidebar.header('Filter options')

# Text box for car name
car_name = st.sidebar.text_input('Enter car name', '')

# Multiselect for transmission type
transmission_type = st.sidebar.multiselect(
    'Choose Transmission Type',
    options=['Manual', 'Automatic'],
    default=['Manual', 'Automatic']
)

# Slider for selling price range
selling_price_range = st.sidebar.slider(
    'Select a range of selling price',
    0, 20, (0, 20)
)

# Slider for year range
year_range = st.sidebar.slider(
    'Select a range of year',
    2000, 2024, (2000, 2024)
)

# Submit button
if st.sidebar.button('Submit'):
    filtered_data = data

    # Filter by car name if specified
    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]

    # Filter by transmission type
    if transmission_type:
        filtered_data = filtered_data[filtered_data['transmission'].isin(transmission_type)]

    # Filter by selling price range
    filtered_data = filtered_data[(filtered_data['selling_price'] >= selling_price_range[0]) & (filtered_data['selling_price'] <= selling_price_range[1])]

    # Filter by year range
    filtered_data = filtered_data[(filtered_data['year'] >= year_range[0]) & (filtered_data['year'] <= year_range[1])]

    # Show filtered data
    st.write(filtered_data)
else:
    # If no filters are selected, show the original data
    st.write(data)
