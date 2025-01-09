import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv
import plotly.graph_objects as go  # Import Plotly for interactive visualizations

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client('s3')

    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists")
        except self.s3_client.exceptions.ClientError as e:
            print(f"Creating bucket {self.bucket_name}")
            try:
                self.s3_client.create_bucket(
                    Bucket=self.bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
                )
                print(f"Successfully created bucket {self.bucket_name}")
            except Exception as e:
                print(f"Error creating bucket: {e}")

    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city):
        """Save weather data to S3 bucket"""
        if not weather_data:
            return False
            
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"
        
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved data for {city} to S3")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False

    # NEW: Function to Create and Save Interactive Plotly Visualizations
    def plot_weather_data_interactive(self, weather_data, city):
        """Create and save an interactive weather chart using Plotly."""
        labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)']
        values = [
            weather_data['main']['temp'],
            weather_data['main']['feels_like'],
            weather_data['main']['humidity']
        ]

        # Create a Plotly bar chart
        fig = go.Figure(data=[
            go.Bar(x=labels, y=values, marker_color=['blue', 'green', 'orange'])
        ])
        fig.update_layout(
            title=f"Weather Data for {city}",
            xaxis_title="Metrics",
            yaxis_title="Values",
            yaxis=dict(range=[0, max(values) + 10])
        )

        # Save the chart as an HTML file
        html_file = f"{city}_weather_chart.html"
        fig.write_html(html_file)
        print(f"Interactive visualization saved as {html_file}")
        return html_file  # Return the HTML file name

    # NEW: Function to Upload Visualizations to S3
    def upload_visualization_to_s3(self, file_name):
        """Upload a visualization to S3."""
        try:
            with open(file_name, "rb") as f:
                self.s3_client.put_object(
                    Bucket=self.bucket_name,
                    Key=f"visualizations/{file_name}",
                    Body=f,
                    ContentType="text/html"
                )
            print(f"Visualization {file_name} uploaded to S3.")
        except Exception as e:
            print(f"Error uploading visualization: {e}")

def main():
    dashboard = WeatherDashboard()
    
    # Create bucket if needed
    dashboard.create_bucket_if_not_exists()
    
    cities = ["Berlin", "Munich", "Paderborn"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = dashboard.fetch_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            
            # Save to S3
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"Weather data for {city} saved to S3!")

            # NEW: Generate and Upload Interactive Visualization
            html_file = dashboard.plot_weather_data_interactive(weather_data, city)
            dashboard.upload_visualization_to_s3(html_file)
        else:
            print(f"Failed to fetch weather data for {city}")

if __name__ == "__main__":
    main()
