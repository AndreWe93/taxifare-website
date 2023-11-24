import streamlit as st
import requests


'''
# NY Taxi Fare Predictor (by AW)
'''

st.markdown('''
Hello friend, please insert the required information to get a taxi fare prediction
''')


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

pickup_datetime = st.text_input("Pickup Date and Time")
pickup_longitude = st.text_input("Pickup Longitude")
pickup_latitude = st.text_input("Pickup Latitude")
dropoff_longitude = st.text_input("Dropoff Longitude")
dropoff_latitude = st.text_input("Dropoff Latitude")
passenger_count = st.text_input("Passenger Count")


if st.button("Predict Fare"):
    url = 'https://taxifare-z2kqlvo2ta-ew.a.run.app/predict'

    params = {
            'pickup_datetime': pickup_datetime,
            'pickup_longitude': pickup_longitude,
            'pickup_latitude': pickup_latitude,
            'dropoff_longitude': dropoff_longitude,
            'dropoff_latitude': dropoff_latitude,
            'passenger_count': passenger_count
        }

    # Make API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Retrieve prediction from JSON response
        prediction = response.json()["fare_amount"]

        # Display prediction to the user
        st.success(f'The predicted fare amount is: ${prediction:.2f}')
    else:
        st.error('Failed to get prediction from the API. Please try again.')
