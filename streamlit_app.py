from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):

    
    st.subheader('JimBot:' + key)
    
    if(key == "Snail"):
        st.error("Losing - Loss%: 1% | Loss$: 100.1 | Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST ")
    elif(key == "Scalper"):
        st.success("Winning - Profit%: 1% | Profit$: 100.1 | Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST ")
    else:
        st.error("Not started")
    
    
# And within an expander
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")


# And within an expander
my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")
