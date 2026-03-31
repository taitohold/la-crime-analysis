# Los Angeles Crime Data Analysis
This project analyzes crime trends in Los Angeles using LAPD public safety data. The goal is to explore patterns in crime over time, location, and demographics using numpy and matplotlib to visualize the data.

## Dataset
- Source: LAPD Crime Data (2020–2024)
- [LAPD Crime Data - LA Open Data Portal](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-2024/2nrs-mtv8/about_data)
- Contains information on crime incidents, including date, time, location, crime type, and victim demographics.

## Tools Used
- Python
- pandas
- matplotlib
- requests

## How to Run
1. Install dependencies: `pip install pandas matplotlib requests`
2. Run `01_get_data.py` to fetch the data
3. Run `02_clean_data.py` to clean and process the data
4. Run `03_visualize.py` to generate the charts

## Analysis Performed
- Top 10 most common crimes
- Crime trends over time (yearly and by crime type)
- Crime distribution by hour of day and day of the week
- Crime distribution across areas (top 10 areas)
- Victim demographics (age distribution)
- Reporting delay analysis by crime seriousness
- Reporting delay comparison across crime types
- Heatmap of crime frequency by hour and day
- Identity theft analysis (age distribution and percentage by area)

## Key Insights
- Crime activity peaks around midday, with noticeable spikes on Wednesdays and Fridays, indicating higher activity during afternoon hours.
- Serious crimes are generally reported more quickly than less serious crimes, suggesting differences in urgency.
- Identity theft has the longest reporting delays among major crime types.
- Identity theft increased significantly from 2021 to 2022, becoming one of the most frequently reported crimes.
- Individuals between the ages of 30 and 40 are the most affected by identity theft.
- Reporting delays vary significantly by crime type: violent crimes such as assault are typically reported immediately (median near 0 days), while crimes like identity theft and theft-related offenses show longer reporting delays and greater variability.

## Project Structure
data/
cleaned_crime_data.csv
get_data.py
clean_data.py
visualize.py
charts/
README.md

## Future Work
- Apply machine learning to predict crime patterns and other data.