import streamlit as st
import numpy as np
import pandas as pd
import time
"""
# Uber pickup Exercise
"""
@st.cache(allow_output_mutation=True)
def downloaddata():
    #data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
    data_url = '/Users/MacbookAir/Documents/maestria/Product Development/streamlit/uber-raw-data-sep14.csv'
    return pd.read_csv(data_url)

nrow =  st.sidebar.slider('No. rows to display:',0,10000,value = 1000)
hour_range = st.sidebar.slider('Select hour range',0,24,(8,17))
st.sidebar.write('the range selected is:',hour_range)


data = (downloaddata()
        #.loc[1:nrow]
        .rename(columns={'Date/Time':'date_time','Lat':'lat','Lon':'lon','Base':'base'})
        .assign(date_time=lambda df:pd.to_datetime(df.date_time))
        .loc[lambda df:(df.date_time.dt.hour >= hour_range[0]) & (df.date_time.dt.hour < hour_range[1])]
        .loc[1:nrow]

        )

data.sort_values('date_time', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
data

st.map(data)

data1 = data.groupby(pd.Grouper(key='date_time',freq='H')).count()

st.bar_chart(data1)