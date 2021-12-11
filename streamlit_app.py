from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):
    st.subheader('JimBot updates for' + key)
    st.markdown(f"<h4 style='text-align: left; margin-left: 30px;'> Started: {started.split('.')[0]} | Running for: {run_for}</h4>", unsafe_allow_html=True)

# And within an expander
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")


# And within an expander
my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")
