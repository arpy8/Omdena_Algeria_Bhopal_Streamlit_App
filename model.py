import joblib
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from plotly import graph_objects as go
from datetime import datetime, date

from utils import *
from config import *

CUR_DATE = datetime.now().date()

def load_data(file_path):
    ds_name = file_path
    df = pd.read_csv(ds_name)
    df.index = pd.to_datetime(df.index)

    return df
    
def plot_data(df, year, place):
    df_before = df[df.index <= '2023-07-01']
    df_after = df[df.index >= '2023-07-01']
    fig = go.Figure([go.Scatter(x=df_before.index, y=df_before.water_availability, name='collected'),
                 go.Scatter(x=df_after.index, y=df_after.water_availability, name='forecasted')
                ])
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Value',
        title=f'Final Forecasting of Water Availability in {place} for the next {year} {"years" if year > 1 else "year"}'
    )
    
    st.plotly_chart(fig)
    return df
   
def load_model(selected):
    model_path = ALGERIA_MODEL if selected == "Algeria" else BHOPAL_MODEL
    model = joblib.load(model_path)
    return model

def main():
    # try:
    st.write('<center><h1>Forecast Water Availability</h1></center><br>', unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Algeria", "Bhopal"],
        icons=["water", "water"],
        styles=CSS2,
        orientation="horizontal"
    )
    
    data = load_data(ALGERIA_AGG_DATASET if selected=="Algeria" else BHOPAL_AGG_DATASET)
    population_data = load_data(ALGERIA_POPULATION if selected=="Algeria" else BHOPAL_POPULATION)
    population_data.date = pd.to_datetime(population_data.date)

    model = load_model(selected)

    mode = option_menu(
        menu_title=None,
        options=["Yearly", "Dated"],
        styles=CSS2,
        orientation="horizontal"
    )
    
    if mode == "Dated":

        col1, col2, col3 = st.columns(3)
        with col1:
            day = st.number_input('Day', min_value=1, max_value=31, value=datetime.now().day)
        with col2:
            month = st.number_input('Month', min_value=1, max_value=12, value=datetime.now().month)
        with col3:
            year = st.number_input('Year', min_value=1900, max_value=2262, value=datetime.now().year)
        try:
            pred_date = date(year, month, day)
            delta = pred_date - CUR_DATE
            number_input = delta.days
            
        except ValueError as e:
            st.error(f"Invalid date: {e}")

    if mode == "Yearly":    
        num_days_input = st.slider("Number of years to forecast", 1, 10, 1)
        number_input = 365*int(num_days_input)

    forecast_button = st.empty()
    
    if forecast_button.button("Forecast"):
        df_forecast = recursive_multi_step_forecasting_monthly(data, TARGET, model, number_input)
        df_and_forecast = pd.concat([data, df_forecast], axis=0)
        
        df_and_forecast['population'] = [population_data[population_data.date.dt.year == y][' Population'].values[0] for y in df_and_forecast.index.year]
        daily_water_demand_lcd = 200
        daily_water_demand_mld = daily_water_demand_lcd * df_and_forecast['population']*10**(-6)
        df_and_forecast['water_availability'] = df_and_forecast.daily_water_volume - daily_water_demand_mld

        plot_data(df_and_forecast, place=selected ,year=number_input)
        st.balloons()
            
        forecast_button.empty()
        
    # except Exception as e:
    #     st.error(f"{e}")

if __name__=="__main__":
    main()