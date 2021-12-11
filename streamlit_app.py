from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):
    st.subheader('JimBot:' + key)
    
    if(key == "Snail"):
        st.error("Losing")
    elif(key == "Scalper"):
        st.success("Winning")
    else:
        st.error("Not started")
        
    st.markdown(f"<h4 style='text-align: left; margin-left: 30px;'> Coins: 1/20 | Mode: TEST </h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: left; margin-left: 30px;'> Profit%: 1% | Profit$: 100.1 </h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: left; margin-left: 30px;'> Win: 1 | Loss: 1  | WL%: 100  </h4>", unsafe_allow_html=True)
    
# And within an expander
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")


# And within an expander
my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")
