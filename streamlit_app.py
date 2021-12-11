from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def my_widget(key):

    color1 = st.color_picker('选择渐变起始颜色', '#1aa3ff',key=1)
    st.write(f"你选择了{color1}")
    
    
    st.subheader('JimBot:' + key)
    
    if(key == "Snail"):
        st.error("Losing")
    elif(key == "Scalper"):
        st.success("Winning")
    else:
        st.error("Not started")
        
    st.markdown(f"<h4 style='text-align: left; margin-left: 30px;'> Profit%: 1% | Profit$: 100.1  Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST |  
    
# And within an expander
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")


# And within an expander
my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")
