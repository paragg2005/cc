import streamlit as st
import pydeck as pdk
import requests


def get_iss_location():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    view_state = pdk.ViewState(latitude=latitude, longitude=longitude, zoom=3, bearing=-29.36, pitch=40.5)
    layer = pdk.Layer('ScatterplotLayer', data=[latitude, longitude], get_position=[latitude,longitude], get_radius=100000,
                      get_fill_color=[0, 255, 0])
    map_ = pdk.Deck(layers=[layer], initial_view_state=view_state)
    map_.update()
    map_.show()

    st.pydeck_chart(map_)



st.title("INTERNATIONAL SPACE STATION TRACKER")
st.write("This app displays the live location of International Space Station")


if st.button('Display Location'):
     get_iss_location()
