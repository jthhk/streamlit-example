import streamlit as st

def my_widget(key):

    
    st.caption(key)
    col1, col2 = st.columns([1,3])
    
    if(key == "Snail"):
        col1.metric("Loss", "100.0", "-1%")
        col2.error("Loss%: 1% | Loss$: 100.1 | Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST ")
    elif(key == "Scalper"):
        col1.metric("Win", "100.0", "5%")
        col2.success("Profit%: 1% | Profit$: 100.1 | Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST ")
    else:
        col1.metric("N/A", "0", "0%")
        col2.error("Not started")
    
    
# And within an expander
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")


# And within an expander
my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")

# And within an expander
my_expander = st.expander("Jim", expanded=True)
with my_expander:
    clicked = my_widget("Jim")
    
    