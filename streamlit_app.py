import json
from types import SimpleNamespace

import datetime
from datetime import datetime

import streamlit as st
import os
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np            
from matplotlib import cm
from matplotlib.patches import Circle, Wedge, Rectangle
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title = 'Binance Volatility Trading Bot',
    page_icon = '✅',
    layout = 'wide',
)

def ShowGorF(link,captiontext):
    image = Image.open(link)
    st.image(image, caption=captiontext)

def left(s, amount):
    return s[:amount]

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M')
    

def degree_range(n):
    start = np.linspace(0, 180, n + 1, endpoint=True)[0:-1]
    end = np.linspace(0, 180, n + 1, endpoint=True)[1::]
    mid_points = start + ((end - start) / 2.)
    return np.c_[start, end], mid_points


def rot_text(ang):
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation


def gauge(labels=['extreme fear', 'fear', 'Greed', 'extreme greed'], \
          colors='jet_r', arrow=1, title='', fname=False):

    N = len(labels)

    if arrow > N:
        raise Exception("\n\nThe category ({}) is greated than \
        the length\nof the labels ({})".format(arrow, N))


    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1, :].tolist()
    if isinstance(colors, list):
        if len(colors) == N:
            colors = colors[::-1]
        else:
            raise Exception("\n\nnumber of colors {} not equal \
            to number of categories{}\n".format(len(colors), N))


    fig, ax = plt.subplots()

    ang_range, mid_points = degree_range(N)

    labels = labels[::-1]

    patches = []
    for ang, c in zip(ang_range, colors):
        # sectors
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0., 0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))

    foo = [ax.add_patch(p) for p in patches]

    for mid, lab in zip(mid_points, labels):
        ax.text(0.35 * np.cos(np.radians(mid)), 0.35 * np.sin(np.radians(mid)), lab, \
                horizontalalignment='center', verticalalignment='center', fontsize=14, \
                fontweight='bold', rotation=rot_text(mid))

    r = Rectangle((-0.4, -0.1), 0.8, 0.1, facecolor='w', lw=2)
    ax.add_patch(r)

    ax.text(0, -0.05, title, horizontalalignment='center', \
            verticalalignment='center', fontsize=22, fontweight='bold')

    pos = mid_points[abs(arrow - N)]

    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), \
             width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')

    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))
    plt.title("Greed or Fear", fontsize = 20)
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.tight_layout()
    if fname:
        fig.savefig(fname, dpi=200)
    st.pyplot(fig)



def fetchMarketSentiment():
    """make a get api call to http://https://api.alternative.me/fng"""
    url = "https://api.alternative.me/fng"
    response = requests.get(url)
    data = response.json()
    data = data['data'][0]
    
    st.write("Market sentiments For Today ")
    st.write("\nIndex value: {}".format(data['value']))
    st.write("\nSentiments:{}".format(data['value_classification']))
    st.write("\nNext Update:{}".format(int(data['time_until_update']) / 3600))
    #return data
    #label = format(data['value_classification']). " - " .format(data['value'])

#0 - 24 = extreme fear
#25 - 49 = Fear
#50 - 74 = Greed
#75 - 100 = extreme greed
    score = data['value']
    
    gauge(labels=['extreme fear', 'fear', 'Greed', 'extreme greed'], \
            colors=["#1b0203", "#ED1C24", '#FFCC00', '#007A00'], arrow=2, title="fear")

    
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
    clicked = ShowGorF("https://alternative.me/crypto/fear-and-greed-index.png","Crypto Fear & Greed Index" )
    
# Per Algo
my_expander = st.expander("Scalper", expanded=True)
with my_expander:
    clicked = my_widget("Scalper")

my_expander = st.expander("Snail", expanded=True)
with my_expander:
    clicked = my_widget("Snail")


    
    