import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Video Game Sales Forecast",
    layout="wide"
)

# Add title and description
st.title("📊 Video Game Sales Forecast")
st.markdown("### ARIMA Model Predictions")

def load_model():
    try:
        with open('arima_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found!")
        return None

def create_forecast_plot(predictions, start_date):
    # Create dates for x-axis
    dates = [start_date + timedelta(days=30*i) for i in range(len(predictions))]
    
    # Create the plot
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=predictions,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#1f77b4', width=2),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Sales Forecast',
        xaxis_title='Date',
        yaxis_title='Predicted Sales ($)',
        template='plotly_white',
        hovermode='x unified'
    )
    
    return fig

# Main app
def main():
    # Load the model
    model = load_model()
    
    if model:
        # Create two columns
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Add input for number of months
            months = st.slider(
                "Number of months to forecast",
                min_value=1,
                max_value=12,
                value=3,
                help="Select the number of months you want to forecast"
            )
            
            if st.button("Generate Forecast"):
                try:
                    # Make predictions
                    forecast = model.forecast(steps=months)
                    predictions = [round(float(x), 2) for x in forecast]
                    
                    # Display predictions in a table
                    df_predictions = pd.DataFrame({
                        'Month': range(1, months + 1),
                        'Predicted Sales ($)': predictions
                    })
                    st.dataframe(df_predictions, use_container_width=True)
                    
                    # Create and display plot in the second column
                    with col2:
                        start_date = datetime.now()
                        fig = create_forecast_plot(predictions, start_date)
                        st.plotly_chart(fig, use_container_width=True)
                        
                except Exception as e:
                    st.error(f"Error generating forecast: {str(e)}")
        
        # Add information about the model
        with st.expander("ℹ️ Model Information"):
            st.write("This application uses an ARIMA model trained on historical video game sales data.")
            st.write("The model was trained using historical sales data and can forecast future sales trends.")
            # Get model specification if available
            try:
                spec = model.specification
                st.write("Model specification:", spec)
            except:
                st.write("Model specification not available.")
            
    else:
        st.warning("Please make sure the ARIMA model file (arima_model.pkl) is in the same directory as this script.")

if __name__ == "__main__":
    main()