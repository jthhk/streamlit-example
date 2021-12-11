import streamlit as st

st.set_page_config(
    page_title = 'Binance Volatility Trading Bot',
    page_icon = '✅',
    layout = 'wide',
)

    
def my_widget(key):


    # path to the saved transactions history
    profile_summary_file = user_data_path +"/user_data/"+ "profile_summary.json"

    with open(profile_summary_file) as f:
    profile_summary = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    
    col1, col2 = st.columns([1,3])
    
    if(key == "Snail"):
        col1.metric("Loss", "100.0", "-1%")
        col2.error("Loss%: {profile_summary.realised_session_profit_incfees_perc}% | Loss$: {realised_session_profit_incfees_total} | Win: {profile_summary.trade_losses} | Loss: {profile_summary.trade_wins}  | WL%: {profile_summary.win_ratio} |  Coins: {profile_summary.current_holds}/{profile_summary.slots} | Mode: TEST ")
    elif(key == "Scalper"):
        col1.metric("Win", "100.0", "5%")
        col2.success("Profit%: 1% | Profit$: 100.1 | Win: 1 | Loss: 1  | WL%: 100 |  Coins: 1/20 | Mode: TEST ")
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
    
    