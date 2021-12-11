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
    profile_summary_file = "/app/streamlit-example/" + key +  "/profile_summary.json"

    with open(profile_summary_file) as f:
        profile_summary = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    
    win_ratio =  round((profile_summary.tradeWins / (profile_summary.tradeWins + profile_summary.tradeLosses)) * 100,2)
    
    col1, col2 = st.columns([1,3])
    
    if(key == "Snail"):
        col1.metric("Win", str(round(profile_summary.historicProfitIncFees_Total,2)), str(round(profile_summary.historicProfitIncFees_Percent,1)) + "%")
        col2.error("Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
        col2.write("12 Dec @ 15:30  |  Staretd:" + str(profile_summary.botstart_datetime))
    elif(key == "Scalper"):
        col1.metric("Win", str(round(profile_summary.historicProfitIncFees_Total,2)), str(round(profile_summary.historicProfitIncFees_Percent,1)) + "%")
        col2.error("Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
        col2.write("12 Dec @ 15:30  |  Staretd:" + str(profile_summary.botstart_datetime))
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
    
    