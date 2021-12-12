import json
from types import SimpleNamespace

import datetime
from datetime import datetime

import streamlit as st
import os

st.set_page_config(
    page_title = 'Binance Volatility Trading Bot',
    page_icon = '✅',
    layout = 'wide',
)

def left(s, amount):
    return s[:amount]

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M')
    


def fetchMarketSentiment():
    """make a get api call to http://https://api.alternative.me/fng"""
    url = "https://api.alternative.me/fng"
    response = requests.get(url)
    data = response.json()
    data = data['data'][0]
    
    st.write("Market sentiments For Today ")
    st.write("\nFear Index: {}\nGreed Index: {}".format(data['value'], 100-int(data['value'])))
    st.write("\nSentiments:{}".format(data['value_classification']))
    #return data
    
    
def my_widget(key):


    # path to the saved transactions history
    profile_summary_file = "/app/streamlit-example/" + key +  "/profile_summary.json"
    
    with open(profile_summary_file) as f:
        profile_summary = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    
    last_updated = modification_date(profile_summary_file)
    
    win_ratio =  round((profile_summary.tradeWins / (profile_summary.tradeWins + profile_summary.tradeLosses)) * 100,2)
    started = left(profile_summary.botstart_datetime,16)
    start_date = datetime.fromisoformat(profile_summary.botstart_datetime)
    run_for = str(datetime.now() - start_date).split('.')[0]
        
    col1, col2 = st.columns([1,3])
    
    if(key == "Snail"):
        col1.metric("Lose", str(round(profile_summary.historicProfitIncFees_Total,2)), str(round(profile_summary.historicProfitIncFees_Percent,1)))
        col2.error("Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
    elif(key == "Scalper"):
        col1.metric("Profit", str(round(profile_summary.historicProfitIncFees_Total,2)), str(round(profile_summary.historicProfitIncFees_Percent,1)))
        col2.success("Win: " + str(profile_summary.tradeWins) + " | Loss: " + str(profile_summary.tradeLosses) + " | WL%: " + str(win_ratio) + "%")
    else:
        col1.metric("N/A", "0", "0%")
        col2.info("Not started")
    
    col2.write("Last Updated: " + str(last_updated) + " |  Started:" + str(started) + " | Running:" + str(run_for))

my_expander = st.expander("Index", expanded=True)
with my_expander:
    clicked = fetchMarketSentiment()
    
# Per Algo
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")

my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")


    
    