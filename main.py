import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from PIL import Image

st.title("🏈 🏈 OL Rush Yards Over Expected Etc. 🏈 🏈")
st.text("")
st.text("")
ol_ryoe_link = st.secrets["ol_ryoe_url"]
ol_ryoe_csv = ol_ryoe_link.replace('/edit#gid=', '/export?format=csv&gid=')
ol_ryoe = pd.read_csv(ol_ryoe_csv)


exes =[
       'Team RYOE', 'Team Attempts', 'Team AVG RYOE', 'Team EPA', 'Team AVG EPA',
       'Team Success Rate', 'Team 1st&10 Attempts', 'Team 1st&10 AVG RYOE',
       'Team 1st&10 AVG EPA', 'Team 1st&10 Success Rate',
       'TM_short_att', 'Team Short AVG RYOE', 'Team Short AVG EPA',
       'Team Short Conversion Rate', 'Team Power Attempts', 'Team Power AVG RYOE',
       'Team Power AVG EPA', 'Team Power Conversion Rate',
       'Run Blocking Snaps', 'RYOE',
       'AVG RYOE', 'EPA', 'AVG EPA', 'Success Rate', '1st&10 Snaps',
       '1st&10 AVG RYOE', '1st&10 AVG EPA',
       '1st&10 Success Rate', 'Short Snaps',
       'Short AVG RYOE', 'Short AVG EPA', 'Short Conversion Rate',
       'Power Snaps', 'Power AVG RYOE', 'Power AVG EPA',
       'Power Conversion Rate'
       ]

texas=['Team EPA', 'Team Attempts',
       'Team RYOE', 'Team AVG RYOE',  'Team AVG EPA',
       'Team Success Rate', 'Team 1st&10 Attempts', 'Team 1st&10 AVG RYOE',
       'Team 1st&10 AVG EPA', 'Team 1st&10 Success Rate',
       'TM_short_att', 'Team Short AVG RYOE', 'Team Short AVG EPA',
       'Team Short Conversion Rate', 'Team Power Attempts', 'Team Power AVG RYOE',
       'Team Power AVG EPA', 'Team Power Conversion Rate',
       'Run Blocking Snaps', 'RYOE',
       'AVG RYOE', 'EPA', 'AVG EPA', 'Success Rate', '1st&10 Snaps',
       '1st&10 AVG RYOE', '1st&10 AVG EPA',
       '1st&10 Success Rate', 'Short Snaps',
       'Short AVG RYOE', 'Short AVG EPA', 'Short Conversion Rate',
       'Power Snaps', 'Power AVG RYOE', 'Power AVG EPA',
       'Power Conversion Rate'
       ]
image = Image.open("https://thumbs.gfycat.com/OrderlyKnobbyGoldeneye-size_restricted.gif")
st.image(image)

ybox = st.selectbox('Select Y Axis!', texas)
xbox = st.selectbox('Select X Axis!', exes)

games = st.slider('Run Snaps Filter (Player)', 1, 300, 100)
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
    plot = px.scatter(ol_ryoe.round(decimals=2), x=xboxx, y=yboxx, #color='Team',
                      #size='Run Blocking Snaps',
                      #size_max=15,
                      trendline='ols',
                      trendline_scope='overall',
                      #hover_name='Name',
                      hover_data=['Team', 'Season', 'Position', 'Run Blocking Snaps', 'Team Attempts'],
                      template='simple_white')
    plot.update_traces(marker_color="rgba(0,0,0,0)")

    maxDim = ol_ryoe[["Team Attempts"]].max().idxmax()
    maxi = ol_ryoe[maxDim].max()
    for i, row in ol_ryoe.iterrows():
        Team = row['Team'].replace(" ", "-")
        plot.add_layout_image(
            dict(
                source=Image.open("./TM_logos/{Team}.png"),
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="middle",
                x=row[xboxx],
                y=row[yboxx],
                sizex=np.sqrt(row["Run Blocking Snaps"] / ol_ryoe["Run Blocking Snaps"].max()) * maxi * 0.2 + maxi * 0.05,
                sizey=np.sqrt(row["Run Blocking Snaps"] / ol_ryoe["Run Blocking Snaps"].max()) * maxi * 0.2 + maxi * 0.05,
                sizing="contain",
                opacity=0.8,
                layer="above"
            )
        )
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
st.text("")
st.text("Definitions:")
st.caption("")
st.caption("RYOE - Rush Yards Over Expected. My model; inputs: yardline, down, distance, # defenders in the box, "
           "shotgun/pistol/under-center, # blockers*, rusher position['RB',QB','TE','WR']. >= 2min remaining in "
           "each half. Score within 10pts.")
st.caption("*Note: # Blockers- An educated guess based on personnel group."
           "I don't have tracking for where each player lined up.")
st.caption("EPA - Expected Points Added.")
st.caption("Success Rate - Pct of rushes on which yards gained >= yards epected.")
st.caption("Conversion Rate - Pct of rushes on which a 1st Down was gained.")
st.caption("Short - Rush Attempt where <= 2 yards is needed to gain a 1st Down. (3rd & 1, 2nd & 2, etc.)")
st.caption("Power - A 'Short' attempt with >= 8 Defenders in the Box.")

