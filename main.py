import pandas as pd
import streamlit as st
import plotly.express as px


st.title("🏈 🏈 OL Rush Yards Over Expected Etc. 🏈 🏈")
st.text("")
st.text("")
ol_ryoe_link = st.secrets["ol_ryoe_url"]
ol_ryoe_csv = ol_ryoe_link.replace('/edit#gid=', '/export?format=csv&gid=')
ol_ryoe = pd.read_csv(ol_ryoe_csv)


exes =['RYOE', 'Run Blocking Snaps',
       'AVG RYOE', 'EPA', 'AVG EPA', 'Success Rate', '1st&10 Snaps',
       '1st&10 AVG RYOE', '1st&10 AVG EPA',
       '1st&10 Success Rate', 'Short Snaps',
       'Short AVG RYOE', 'Short AVG EPA', 'Short Conversion Rate',
       'Power Snaps', 'Power AVG RYOE', 'Power AVG EPA',
       'Power Conversion Rate', 'Team Attempts',
       'Team RYOE', 'Team AVG RYOE', 'Team EPA', 'Team AVG EPA',
       'Team Success Rate', 'Team 1st&10 Attempts', 'Team 1st&10 AVG RYOE',
       'Team 1st&10 AVG EPA', 'Team 1st&10 Success Rate',
       'TM_short_att', 'Team Short AVG RYOE', 'Team Short AVG EPA',
       'Team Short Conversion Rate', 'Team Power Attempts', 'Team Power AVG RYOE',
       'Team Power AVG EPA', 'Team Power Conversion Rate'
       ]

texas=['EPA', 'Run Blocking Snaps',
       'AVG RYOE', 'RYOE', 'AVG EPA', 'Success Rate', '1st&10 Snaps',
       '1st&10 AVG RYOE', '1st&10 AVG EPA',
       '1st&10 Success Rate', 'Short Snaps',
       'Short AVG RYOE', 'Short AVG EPA', 'Short Conversion Rate',
       'Power Snaps', 'Power AVG RYOE', 'Power AVG EPA',
       'Power Conversion Rate', 'Team Attempts',
       'Team RYOE', 'Team AVG RYOE', 'Team EPA', 'Team AVG EPA',
       'Team Success Rate', 'Team 1st&10 Attempts', 'Team 1st&10 AVG RYOE',
       'Team 1st&10 AVG EPA', 'Team 1st&10 Success Rate',
       'TM_short_att', 'Team Short AVG RYOE', 'Team Short AVG EPA',
       'Team Short Conversion Rate', 'Team Power Attempts', 'Team Power AVG RYOE',
       'Team Power AVG EPA', 'Team Power Conversion Rate'
       ]

ybox = st.selectbox('Select Y Axis!', texas)
xbox = st.selectbox('Select X Axis!', exes)

games = st.slider('Run Snaps Filter', 1, 300, 100)
ol_ryoe = ol_ryoe.loc[ol_ryoe['Run Blocking Snaps'] >= games]

yearmin, yearmax = st.slider('Season Filter', 2016, 2022, (2016, 2022))
ol_ryoe = ol_ryoe.loc[ol_ryoe['Season'] >= yearmin]
ol_ryoe = ol_ryoe.loc[ol_ryoe['Season'] <= yearmax]

for xbrick in exes:
    if xbox == xbrick:
        xboxx = xbrick
for ybrick in texas:
    if ybox == ybrick:
        yboxx = ybrick

def interactivePlot2():
    plot = px.scatter(ol_ryoe.round(decimals=2), x=xboxx, y=yboxx, color='Team',
                      color_discrete_map={'ARI': '#97233F',
                                          'ATL': '#A71930',
                                          'BAL': '#241773',
                                          'BUF': '#00338D',
                                          'CAR': '#0085CA',
                                          'CHI': '#C83803',
                                          'CIN': '#FB4F14',
                                          'CLE': '#FF3C00',
                                          'DAL': '#002244',
                                          'DEN': '#002244',
                                          'DET': '#0076B6',
                                          'GB': '#203731',
                                          'HOU': '#03202F',
                                          'IND': '#a5acaf',
                                          'JAX': '#006778',
                                          'KC': '#E31837',
                                          'LA': '#003594',
                                          'LAC': '#007BC7',
                                          'LAR': '#003594',
                                          'LV': '#000000',
                                          'MIA': '#008E97',
                                          'MIN': '#4F2683',
                                          'NE': '#C60C30',
                                          'NO': '#D3BC8D',
                                          'NYG': '#0B2265',
                                          'NYJ': '#003F2D',
                                          'OAK': '#000000',
                                          'PHI': '#004C54',
                                          'PIT': '#FFB612',
                                          'SD': '#007BC7',
                                          'SEA': '#002244',
                                          'SF': '#AA0000',
                                          'STL': '#003594',
                                          'TB': '#A71930',
                                          'TEN': '#002244',
                                          'WAS': '#5A1414'},
                      size='Run Blocking Snaps',
                      size_max=15,
                      trendline='ols',
                      trendline_scope='overall',
                      hover_name='Name',
                      hover_data=['Team', 'Season', 'Position', 'Run Blocking Snaps', 'Team Attempts'],
                      template='simple_white')

    plot.update_layout(
        xaxis_title=xboxx,
        yaxis_title=yboxx,
        #legend_title="Name [select from table above]",
        #plot_bgcolor="rgb(0,0,0)",
        #paper_bgcolor="rgb(0,0,0)"
    )
    #plot.update_traces(marker={'size': 12})

    st.plotly_chart(plot)


interactivePlot2()
st.text("")
st.caption("Data= nflverse")
st.caption("Author= @CFGordon")
st.text("")
st.text("")
st.text("Definitions:")
st.text("")
st.caption("RYOE - Rush Yards Over Expected. My model, inputs: yardline, down, distance, # defenders in the box, "
           "shotgun/pistol/under-center, # blockers*, rusher position['RB',QB','TE','WR']")
st.caption("*Note: # Blockers- An educated guess based on personnel group."
           "I don't have tracking for where each player lined up.")
st.caption("EPA - Expected Points Added.")
st.caption("Success Rate - Pct of rushes on which yards gained >= yards epected.")
st.caption("Conversion Rate - Pct of rushes on which a 1st Down was gained.")
st.caption("Short - Rush Attempt where <= 2 yards is needed to gain a 1st Down. (3rd & 1, 2nd & 2, etc.)")
st.caption("Power - A 'Short' attempt with >= 8 Defenders in the Box.")

