import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from script import *

st.title('Roller Coaster Rankings')

# ===========================================================================
# Import CSV files
# ===========================================================================
steel_winners = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_winners = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
roller_coasters = pd.read_csv('roller_coasters.csv')

# ===========================================================================
# Import CSV files
# ===========================================================================
roller_coaster_type = ['Steel', 'Wood']

# ===========================================================================
# Sidebar
# ===========================================================================
visualization_type = st.sidebar.selectbox(
    'Which kind of visualization do you want to see?',
    [
        'Line chart of the ranking of 1 roller coaster over time',
        'Line chart of the ranking of 2 roller coasters over time',
        'Line chart of the ranking of the top N roller coasters over time',
        'Histogram of a numeric column',
        'Bar graph of the number of inversions of all coasters in a park',
        'Pie chart of the roller coasters status',
        'Scatter plot of two columns'
    ]
)

if visualization_type == 'Line chart of the ranking of 1 roller coaster over time':
    # ===========================================================================
    # Plot the ranking of 1 roller coaster over time
    # ===========================================================================
    st.write('## Plot of the ranking of a roller coaster over time')

    # Type
    user_roller_coaster_type = st.selectbox(
        'Choose the type of the roller coaster : ',
        roller_coaster_type
    )
    if user_roller_coaster_type == 'Steel':
        user_choice_df = steel_winners
    elif user_roller_coaster_type == 'Wood':
        user_choice_df = steel_winners

    # Park
    user_park_name = st.selectbox(
        'Choose the park where the roller coaster is located:',
        user_choice_df['Park']
    )
    roller_coaster_names = user_choice_df[user_choice_df['Park'] == user_park_name]

    # Name
    user_coaster_name = st.selectbox(
        'Choose the coaster:',
        roller_coaster_names.Name.unique()
    )

    # Plot
    st.pyplot(plot_1ranking_over_time(user_coaster_name, user_park_name, user_choice_df))

elif visualization_type == 'Line chart of the ranking of 2 roller coasters over time':
    # ===========================================================================
    # Plot the ranking of 2 rollers coasters over time
    # ===========================================================================
    st.write('## Plot of the ranking of 2 roller coasters over time')

    # Type
    user_roller_coaster_type = st.selectbox(
        'Choose the type of the rollers coasters : ',
        roller_coaster_type
    )
    if user_roller_coaster_type == 'Steel':
        user_choice_df = steel_winners
    elif user_roller_coaster_type == 'Wood':
        user_choice_df = steel_winners

    # Park 1
    user_park_name_1 = st.selectbox(
        'Choose the park where the first roller coaster is located:',
        user_choice_df['Park']
    )
    roller_coaster_names_1 = user_choice_df[user_choice_df['Park'] == user_park_name_1]
    user_coaster_name_1 = st.selectbox(
        'Choose the coaster:',
        roller_coaster_names_1.Name.unique()
    )

    # Park 2
    user_park_name_2 = st.selectbox(
        'Choose the second park:',
        user_choice_df['Park']
    )
    roller_coaster_names_2 = user_choice_df[user_choice_df['Park'] == user_park_name_2]
    user_coaster_name_2 = st.selectbox(
        'Choose the coaster: ',
        roller_coaster_names_2.Name.unique()
    )

    # Plot
    st.pyplot(plot_2ranking_over_time(user_coaster_name_1, user_park_name_1, user_coaster_name_2, user_park_name_2, user_choice_df))

elif visualization_type == 'Line chart of the ranking of the top N roller coasters over time':
    # ===========================================================================
    # Line chart of the ranking of the top N roller coasters over time
    # ===========================================================================
    st.write('## Line chart of the ranking of the top N roller coasters over time')

    user_roller_coaster_type = st.selectbox(
        'Choose the type of the rollers coasters : ',
        roller_coaster_type
    )
    if user_roller_coaster_type == 'Steel':
        user_choice_df = steel_winners
    elif user_roller_coaster_type == 'Wood':
        user_choice_df = steel_winners

    user_top_N = st.selectbox(
        'Show the top ... ',
        list(range(1,21))
    )

    st.pyplot(plot_n_rank(user_top_N, user_choice_df))
