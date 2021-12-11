from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):
    st.subheader('Hello there!')
    clicked = st.button("Click me " + key)

# This works in the main area
clicked = my_widget("first")

# And within an expander
my_expander = st.beta_expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")

