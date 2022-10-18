import streamlit as st
from datetime import date,datetime,timedelta

import pandas as pd
#import matplotlib.image as mpimg

from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.set_page_config(page_title="Israel Election 2022 Sentiment Analyses",
                                    page_icon=":bar_chart:",
                                    layout="wide")

START="2022-01-01"

today=date.today() + timedelta(days=1)

TODAY=today.strftime("%Y-%m-%d") 

twitter_leaders = ("netanyahu",
                                  "yairlapid",
                                  "naftalibennett",
                                  "itamarbengvir",
                                  "bezalelsm",
                                  "ariyederi",
                                  "AvigdorLiberman",
                                  "gantzbe",
                                  "Gabi_Ashkenazi",
                                  "Gafni_Moshe",
                                  "MeravMichaeli",
                                  "NitzanHorowitz",
                                  "mnsorabbas",
                                  "AyOdeh",
                                  "StellaWeinstei3")

full_name_leaders=("Benjamin Netanyahu",
                                      "Yair Lapid",
                                      "Naftali Bennett",
                                      "Itamar Bengvir",
                                      "Bezalel Smotrich",
                                      "Ariye Deri",
                                      "Avigdor Liberman",
                                      "Benny Gantz",
                                      "Gabi Ashkenazi",
                                      "Gafni Moshe",
                                      "Merav Michaeli",
                                      "Nitzan Horowitz",
                                      "Mansour Abbas",
                                      "Ayman Odeh",
                                      "Stella Weinstein")

partie=("Likud",
               "Yesh Atid",
               "Yamina",
               "Otzma Yehudit",
               "Religious Zionist Party",
               "Shas",
               "Yisrael Beiteinu",
               "Blue and White",
               "Blue and White",
               "United Torah Judaism",
               "Labor Party",
               "Merez",
               "United Arab List",
               "Hadash",
               "3040")

display_list = ("Tweets","Positive Tweets","Negative Tweets","Analyses")

#st.write(today)

header               = st.container()
dataset              = st.container() 
features             = st.container()
modelTraining  = st.container()

with header:
      st.title="Israel, Election , 2022"
      st.text="I analyzed the tweets  Israel Presidential Election Candidates during their Election Campaign, to find out what exactly where they saying"
      
with dataset:
       st.header('Twitter data set related to election in Israel,2022')
       st.text="Data set"

@st.cache
       
#define tupple

def concatStr(s1,s2,s3,s4):
    return "{}{}{}{}".format(s1,s2,s3,s4)

def load_data(leader):
       st.image(concatStr('out/',leader,'_twitter.png',''))
              
       df1 = pd.read_excel(
       io=concatStr('out/',leader,'_2022.xlsx',''),
       engine='openpyxl',
       sheet_name=concatStr(leader,'_2022','',''),
       skiprows=0,
       usecols='C,G:I'
       )
       
       NegativeDF=df1.sort_values(by=['Polarity']).query('Polarity<0')
       PositiveDF=df1.sort_values(by=['Polarity']).query('Polarity>0')
       
       df2 = pd.read_excel(
       io=concatStr('out/',leader,'_analyses_2022.xlsx',''),
       engine='openpyxl',
       sheet_name=concatStr(leader,'_analyses_2022','',''),
       skiprows=0,
       usecols='D:F'
       )
       
       st.subheader("Sentiment distribution of the tweets")
       st.image(concatStr('out/',leader,'_pie.png',''))
       
       st.subheader("Wordcloud for all the tweets")
       st.image(concatStr('out/',leader,'.png',''))  
       
       selected_display_list =st.selectbox("Choose the option to display",display_list)  
       if selected_display_list in display_list:
            if selected_display_list=='Tweets':
               st.dataframe(df1)
            if selected_display_list=='Positive Tweets':
               st.dataframe(PositiveDF)
            if selected_display_list=='Negative Tweets':
               st.dataframe(NegativeDF)
            if selected_display_list=='Analyses':
                st.dataframe(df2)

    #return data

selected_leader = st.selectbox("Select leader in order to get data set",full_name_leaders)

if selected_leader in full_name_leaders:
     x = full_name_leaders.index(selected_leader)
     st.subheader("This is the analysis of "+selected_leader+"'s twitter account during the 2022 presidential election.")
     
    # Get twitter name
     #st.subheader(twitter_leaders[x])
     load_data(twitter_leaders[x])


