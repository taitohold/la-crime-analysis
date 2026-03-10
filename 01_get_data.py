import requests
import pandas as pd
from io import StringIO

url = "https://data.lacity.org/resource/2nrs-mtv8.csv?$limit=900000"

response = requests.get(url)
df = pd.read_csv(StringIO(response.text))
df.to_csv("data/crime_data.csv", index=False)
