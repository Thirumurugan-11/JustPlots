import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Just Plots")
sf = st.file_uploader("Choose a CSV file")
sk = st.sidebar.number_input("Skiprow value")
row_ul = int(st.sidebar.number_input("Enter start Value"))
row_ll = int(st.sidebar.number_input("Enter End Value"))
#rand_1 = st.sidebar.number_input('Random Value - 1')


def plot():
    st.write(pr1,df[pr1][0],pr2,df[pr2][0])
    f,ax  = plt.subplots(1,1,figsize=(10,4))
    ax.set_xlabel(index)
    st.line_chart(data=df,y=[pr1,pr2])

if sf is not None:
    df = pd.read_excel(sf,skiprows=[int(i) for i in range(1,int(sk)+1)])
    df.dropna(axis = 0, how ='any')
    index = st.sidebar.selectbox("Choose index",options=[i for i in df.columns])
    df.set_index(index,inplace=True)

    if st.button("Show Dataframe"):
        if int(row_ul)==0 and int(row_ll)==0:
            df = df.head(10)
            st.write(df.head(10))
        else:
            print(row_ll,row_ul)
            df = df.iloc[int(row_ul):int(row_ll)]
            st.write(df)

    pr1 = st.sidebar.selectbox("Choose parmeter 1",options=[i for i in df.columns],key=1)
    pr2 = st.sidebar.selectbox("Choose parameter 2",options=[i for i in df.columns],key=2)
    prc = st.sidebar.number_input("Adjust scale parameter1",key=3)
    prc1 = st.sidebar.number_input("Adjust scale parameter2",key=4)

    if int(prc)!=0:
        df[pr1] = df[pr1]/int(prc)
    if int(prc1)!=0:
        df[pr2] = df[pr2]/int(prc1)

    

    if st.button("PLOT"):
        if int(row_ul)!=0 or int(row_ll)!=0:
            df = df.iloc[int(row_ul):int(row_ll)]
        st. empty() 
        plot()
