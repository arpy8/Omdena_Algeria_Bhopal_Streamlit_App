import joblib
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

from config import *
from utils import *


def load_data(file_path):
    ds_name = file_path
    df = pd.read_csv(ds_name)
    df.index = pd.to_datetime(df.index)

    return df


def plot_data(df, year, place):
    fig = px.line(df, x=df.index, y=df.columns[-1])
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Value',
        title=f'Final Forecasting of Water Availability in {place} for the next {year} {"year" if year == 1 else "years"}'
    )
    st.plotly_chart(fig)

    return df


def main():
    try:
        st.write('<center><h1>Forecast Water Availability</h1></center><br>', unsafe_allow_html=True)

        selected = option_menu(
            menu_title=None,
            options=["Algeria", "Bhopal"],
            icons=["water", "water"],
            styles=CSS2,
            orientation="horizontal"
        )

        if selected=="Algeria":
            data = load_data(ALGERIA_AGG_DATASET)
            model = joblib.load(ALGERIA_MODEL)
            number_input = st.slider("Number of years to forecast", 1, 50, 1)
            
            forecast_button = st.empty()
            
            if forecast_button.button("Forecast"):
                df_forecast = recursive_multi_step_forecasting_monthly(data, TARGET, model, 365*int(number_input))
                df_and_forecast = pd.concat([data, df_forecast], axis=0)
                daily_water_demand_mld_algiers = DAILY_WATER_DEMAND_LCD * df_and_forecast[df_and_forecast.columns[0]]*10**(-6)
                df_and_forecast['water_availability'] = df_and_forecast.daily_water_volume - daily_water_demand_mld_algiers

                plot_data(df_and_forecast, place="Algeria" ,year=number_input)
                st.balloons()

                forecast_button.empty()

        if selected=="Bhopal":
            data = load_data(BHOPAL_AGG_DATASET)
            model = joblib.load(BHOPAL_MODEL)
            number_input = st.slider("Number of years to forecast", 1, 50, 1)

            forecast_button = st.button("Forecast")

            if forecast_button:
                df_forecast = recursive_multi_step_forecasting_monthly(data, TARGET, model, 365*int(number_input))
                df_bhopal_and_forecast = pd.concat([data, df_forecast], axis=0)
                daily_water_demand_mld_bhopal = DAILY_WATER_DEMAND_LCD * df_bhopal_and_forecast['population'] * 10**(-6)
                df_bhopal_and_forecast['water_availability'] = df_bhopal_and_forecast.daily_water_volume - daily_water_demand_mld_bhopal

                plot_data(df_and_forecast, place="Algeria" ,year=number_input)
                st.balloons()

                forecast_button.empty()

    except Exception as e:
        print(e)


if __name__=="__main__":
    main()