from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):
    st.subheader('JimBot updates')

# And within an expander
my_expander = st.expander("Bot1", expanded=True)
with my_expander:
    clicked = my_widget("second")


