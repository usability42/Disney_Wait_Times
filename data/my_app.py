import streamlit as st
import pickle
import numpy as np
import pandas as pd

navi_pickle = pickle.load(open('navi_results.pkl', 'rb'))
safari_pickle = pickle.load(open('safari_results.pkl', 'rb'))

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

    st.markdown(html_formatting, unsafe_allow_html=True)

    st.header("Choose Your Rides!")
    options = st.multiselect(["Kiliminjaro Safaris", "Na'vi River Journey"])

    if st.multiselect("Kiliminjaro Safaris"):
        output = safari_est_wait
        st.success('est wait is: {safari_est_wait}')

    if st.multiselect("Na'vi River Journey"):
        output = navi_est_wait
        st.success('est wait is: {navi_est_wait}')


if name == 'main':
    main()
