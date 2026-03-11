import pandas as pd

df = pd.read_csv("data/crime_data.csv")
# print(df.columns.tolist())
# print(df.dtypes)
# print(df.head(2))

# print(df.iloc[0])

df = df.drop(columns = ['crm_cd_2', 'crm_cd_3', 'crm_cd_4', 'cross_street', 'mocodes', 'weapon_used_cd', 'rpt_dist_no', 'dr_no', 'crm_cd', 'crm_cd_1', 'premis_cd', 'area', 'status'])
df = df.dropna(subset=['crm_cd_desc', 'vict_age', 'vict_sex', 'lat', 'lon'])

df = df[df['vict_age'] > 0]
df = df[df['vict_sex'].isin(['M', 'F'])]

df['date_occ'] = pd.to_datetime(df['date_occ'])
df['hour'] = df['time_occ'] // 100

df['month'] = df['date_occ'].dt.month    
df['day_of_week'] = df['date_occ'].dt.day_name() 
df['year'] = df['date_occ'].dt.year  

df['date_rptd'] = pd.to_datetime(df['date_rptd'])
df['days_to_report'] = (df['date_rptd'] - df['date_occ']).dt.days

df = df.rename(columns={
    'date_rptd': 'date_reported',
    'date_occ': 'date_occured',
    'time_occ': 'time_occured',
    'area_name': 'area',
    'part_1_2': 'crime_seriousness',
    'crm_cd_desc': 'crime',
    'vict_age': 'victim_age',
    'vict_sex': 'victim_sex',
    'vict_descent': 'victim_descent',
    'premis_desc': 'premise',
    'weapon_desc': 'weapon',
    'status_desc': 'status',
    'lat': 'latitude',
    'lon': 'longitude'
})

df.to_csv("data/cleaned_crime_data.csv", index=False)
print(f"Cleaned data saved: {df.shape[0]} rows, {df.shape[1]} columns")