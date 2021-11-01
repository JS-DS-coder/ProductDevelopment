import streamlit as st
import numpy as np
import pandas as pd

st.title('This is my first app from galileo master')
x = 4

st.write(x,'^2 = ',x**2)

st.write('This is a data frame example')

st.write(pd.DataFrame({'Column A':['A','B','C','D'],
                       'Columna B':[1,2,3,4]}))

"""
# Title: this is a Tittle tag
This a example for dataframes
"""

df = pd.DataFrame({'Column A':['A','B','C','D'],
                       'Columna B':[1,2,3,4]})

df

"""
## Show me some graphs
"""

df_to_plot = pd.DataFrame(np.random.randn(20,3),columns=["columna A","columna b","columna c"])

st.line_chart(df_to_plot)

"""
## Lets plot a map
"""
df_lat_lon = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])

st.map(df_lat_lon)

if st.checkbox('Show Dataframe'):
    df_lat_lon

"""
## Lets try some widgets

### 1.Slider
"""

x = st.slider('Select a value for x',min_value=1,max_value=100)
y = st.slider('Select a power for x',min_value=0,max_value=5)
st.write(x,'power',y,x**y)

"""

### 2. Options
"""
def test():
    st.write('Funcion ejecutada')

option_list = range(1,10)
option = st.selectbox('Which number do you like best?',option_list,on_change=test)

st.write('Your favorite number is ',option)

"""

### 3. Progress Bar
"""

import time
label = st.empty()
progress_bar = st.progress(0)
for i in range(0,101):
    label.text (f'The value is: {i}')
    progress_bar.progress(i)
    time.sleep(0.05)

st.sidebar.write('this is a sidebar')

option1 = st.sidebar.selectbox('Select a side number',option_list)
st.sidebar.write('The selection is:',option1)

st.sidebar.write('another slider')

another_slider = st.sidebar.slider('Select range',0.0,100.0,(25.0,75.0))
st.sidebar.write('the range selected is:',another_slider)