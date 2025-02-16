# **Weather Data Dashboard**

## **Project Overview**
The **Weather Data Dashboard** is a Python-based application designed to fetch real-time weather data from the OpenWeather API, store the data in AWS S3, and display weather details for multiple cities. This project serves as an introduction to integrating external APIs, leveraging cloud storage, and exploring DevOps practices such as version control and environment management.

---

## **Features**
- Fetches and displays weather details such as:
  - Temperature (°C or °F)
  - Feels-like temperature
  - Humidity percentage
  - Weather conditions (e.g., rain, snow)
- Supports tracking weather data for multiple cities.
- Saves weather data with timestamps to an AWS S3 bucket for historical tracking.
- Handles errors gracefully for invalid inputs or API failures.
- Configurable units for temperature (metric or imperial).

---

## **Technical Architecture**
- **Programming Language**: Python 3.x
- **Cloud Provider**: AWS (S3)
- **External API**: OpenWeather API
- **Key Dependencies**:
  - `boto3` (AWS SDK for Python)
  - `requests` (HTTP requests library)
  - `python-dotenv` (Environment variable management)

---

## **Project Structure**
```
weather-dashboard/
  ├── src/
  │   ├── __init__.py
  │   ├── weather_dashboard.py
  ├── tests/
  ├── data/
  ├── .env
  ├── .gitignore
  ├── requirements.txt
  └── README.md
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/KwasiPee/weather_dashboard_pra.git
cd weather-dashboard
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**
Create a `.env` file in the project root directory and add the following:
```plaintext
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_s3_bucket_name
```

### **4. Configure AWS Credentials**
Ensure you have AWS credentials configured on your system. Run the following command to set them up:
```bash
aws configure
```

### **5. Run the Application**
```bash
python src/weather_dashboard.py
```

---

## **Usage**
1. The application will fetch real-time weather data for predefined cities (configurable in the `src/weather_dashboard.py` file).
2. Weather data will be displayed in the terminal.
3. Weather details will also be saved to your AWS S3 bucket in JSON or CSV format.

---

## **What I Learned**
- **API Integration**:
  - Interfacing with the OpenWeather API to fetch live weather data.
- **AWS S3 Management**:
  - Creating and managing AWS S3 buckets programmatically.
- **Environment Management**:
  - Using environment variables for securely storing API keys and configuration settings.
- **Python Development**:
  - Structuring Python applications, handling errors, and adhering to best practices.
- **Git Workflow**:
  - Version control for project development and deployment.

  ## Visualizations

### Weather Data for Munich
The bar chart for **Munich** clearly displays all metrics, including temperature, feels-like temperature, and humidity.

![Munich Weather Chart](images/munich_chart.png)

### Weather Data for Paderborn
Due to the low temperatures in **Paderborn**, the bar chart prominently highlights the **humidity**, with other metrics being less visually significant.

![Paderborn Weather Chart](images/paderborn_chart.png)

### Weather Data for Berlin
Similarly, in **Berlin**, only the **humidity** is visually prominent in the bar chart due to the low temperature values.

![Berlin Weather Chart](images/berlin_chart.png)

---

## Visualization Notes
Due to the low temperatures in **Paderborn** and **Berlin**, their bar charts primarily highlight **humidity** as the most visible metric. In contrast, the chart for **Munich** displays all metrics (temperature, feels-like temperature, and humidity) more evenly.

---

## How to Use
1. Run the Python script to fetch weather data for predefined cities.
2. View the interactive bar charts saved as HTML files or screenshots in the `images/` folder.
3. Visualizations are also available on AWS S3 under the `visualizations/` folder.

---

## Setup Instructions
Refer to the previous sections for setting up the project and running the script.

---

---

## **Future Enhancements**
- Add weather forecasting for cities.
- Integrate more data visualization ( AWS QuickSight).
- Support more cities dynamically via user input or configuration.
- Implement automated testing for robustness.
- Set up a CI/CD pipeline for continuous deployment.

---

## **Dependencies**
- Python 3.x
- `boto3` (for AWS S3 interaction)
- `requests` (for HTTP requests)
- `python-dotenv` (for managing environment variables)

---


