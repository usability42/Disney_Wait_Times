import streamlit as st
import pickle
import numpy as np
import pandas as pd
import statsmodels as sm
from sklearn import metrics

navi_data = pd.read_csv('data/navi_covid_weekly3.csv')
safari_data = pd.read_csv('data/safari_covid_weekly3.csv')
everest_data = pd.read_csv('data/everest_covid_weekly3.csv')


with open('models/everest_results.pkl', 'rb') as pickle_in:
    everest = pickle.load(pickle_in)

with open('models/safari_results.pkl', 'rb') as pickle_in:
    safari = pickle.load(pickle_in)


def wild(rides):
    input = rides.astype(np.multiselect)
    navi_est_wait = int(round(navi_results.predict_proba(input)))
    safari_est_wait = int(round(safari_results.predict_proba(input)))
    submit_button = st.button("Submit")

def main():
    st.title("What's Your Wild?")
    html_formatting = """
    <div style="background-color:289C28" ;padding: 8px">
    <h2 style="color:white; text-align:center;">What's Your Wild</h2>
    </div>
    """

    visit_date = st.date_input('Date input')

    st.markdown(html_formatting, unsafe_allow_html=True)

    st.header("Choose Your Rides!")
    ride_options = st.multiselect("Choose Your Rides", ("Kiliminjaro Safaris", "Na'vi River Journey",
    "Everest Expedition"))
    submit_rides = st.button("Submit")
    if submit_rides:
        col_1, col_2 = st.columns(2)
        col_1.header("Ride")
        col_2.header("Est Wait")
        col_1.write("rides_selected")
        col_2.write("model results")

        if "Kiliminjaro Safaris" in ride_options:
            safari_data
            # unpickle or pickle data


        if "Na'vi River Journey" in ride_options:
            navi_data = pd.read_csv('data/navi_covid_weekly3.csv')
            with open('models/navi_results.pkl', 'rb') as pickle_in:
                navi = pickle.load(pickle_in)
            navi_pred = navi.predict(navi_data)

        if "Everest Expedition" in ride_options:
            st.write("snow")


# Correct so far


#if name == 'main':
main()
