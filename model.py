import joblib
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from plotly import graph_objects as go

from utils import *
from config import *

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
        st.success("Done Selected")
        
        data = load_data(ALGERIA_AGG_DATASET if selected=="Algeria" else BHOPAL_AGG_DATASET)
        st.success("Done Data")
        
        population_data = load_data(ALGERIA_POPULATION if selected=="Algeria" else BHOPAL_POPULATION)
        population_data.date = pd.to_datetime(population_data.date)
        st.success("Done Population Data")
        
        model = joblib.load(ALGERIA_MODEL if selected=="Algeria" else BHOPAL_MODEL)
        st.success("Done Model")
        
        number_input = st.slider("Number of years to forecast", 1, 10, 1)
        forecast_button = st.empty()
        
        if forecast_button.button("Forecast"):
            df_forecast = recursive_multi_step_forecasting_monthly(data, TARGET, model, 365*int(number_input))
            df_and_forecast = pd.concat([data, df_forecast], axis=0)
            st.success("Done Forecasted Data")
            
            df_and_forecast['population'] = [population_data[population_data.date.dt.year == y][' Population'].values[0] for y in df_and_forecast.index.year]
            daily_water_demand_lcd = 200
            daily_water_demand_mld = daily_water_demand_lcd * df_and_forecast['population']*10**(-6)
            df_and_forecast['water_availability'] = df_and_forecast.daily_water_volume - daily_water_demand_mld
            st.success("Done Water Availability")

            plot_data(df_and_forecast, place=selected ,year=number_input)
            st.success("Done Water Availability")
            st.balloons()
                
            forecast_button.empty()
        
    # except Exception as e:
    #     st.error(f"{e}")

if __name__=="__main__":
    main()