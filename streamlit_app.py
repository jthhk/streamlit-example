import json
from types import SimpleNamespace

import streamlit as st

st.set_page_config(
    page_title = 'Binance Volatility Trading Bot',
    page_icon = '✅',
    layout = 'wide',
)

    
def my_widget(key):


    # path to the saved transactions history
    profile_summary_file = "profile_summary.json"

    with open(profile_summary_file) as f:
        profile_summary = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    
    win_ratio =  profile_summary.tradeWins / (profile_summary.tradeWins + profile_summary.tradeLosses)
    
    col1, col2 = st.columns([1,3])
    
    if(key == "Snail"):
        col1.metric("Loss", str(profile_summary.historicProfitIncFees_Total), str(profile_summary.historicProfitIncFees_Percent) + "%")
        col2.error("Loss%: " + str(profile_summary.historicProfitIncFees_Percent) + " | Loss$: " + str(profile_summary.historicProfitIncFees_Total) + " | Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
        col2.write("12 Dec @ 15:30")
    elif(key == "Scalper"):
        col1.metric("Win", str(profile_summary.historicProfitIncFees_Total), str(profile_summary.historicProfitIncFees_Percent) + "%")
        col2.error("Win%: " + str(profile_summary.historicProfitIncFees_Percent) + " | Win$: " + str(profile_summary.historicProfitIncFees_Total) + " | Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
        col2.write("12 Dec @ 15:30")
    else:
        col1.metric("N/A", "0", "0%")
        col2.info("Not started")
    
    
# Per Algo
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")

my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")

my_expander = st.expander("Jim", expanded=True)
with my_expander:
    clicked = my_widget("Jim")
    
    