import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/cleaned_crime_data.csv")

os.makedirs("charts", exist_ok=True)

# Top 10 most common crimes
plt.figure(figsize=(10, 6))
top_crimes = df['crime'].value_counts().head(10).sort_values(ascending=True)
plt.barh(top_crimes.index, top_crimes.values)
plt.title("Top 10 Most Common Crimes")
plt.xlabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/top_crimes.png")
plt.close()

# Crimes by year
plt.figure(figsize=(10,6))
yearly_crime = df['year'].value_counts().sort_index()
plt.xticks([2020, 2021, 2022, 2023, 2024])
plt.plot(yearly_crime.index, yearly_crime.values, marker='o')
plt.title("Crimes by Year")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/crimes_by_year.png")
plt.close()

# Crimes by hours
plt.figure(figsize=(10,6))
hourly_crime = df['hour'].value_counts().sort_index()
plt.xticks(range(0, 24))
plt.bar(hourly_crime.index, hourly_crime.values)
plt.title("Crimes by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/crimes_by_hour.png")
plt.close()

# Top 10 most dangerous areas
plt.figure(figsize=(10,6))
dangerous_areas = df['area'].value_counts().head(10).sort_values(ascending=True)
plt.bar(dangerous_areas.index, dangerous_areas.values)
plt.title("Top 10 Most Dangerous Areas")
plt.xlabel("Area in LA")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/top_crime_areas.png")
plt.close()

# Vicitim age distribution
plt.figure(figsize=(10,6))
plt.hist(df['victim_age'], bins=20)
plt.title("Victims Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/victim_age_dist.png")
plt.close()

# Days to report by crime seriousness
plt.figure(figsize=(10, 6))
df_filtered = df[(df['days_to_report'] <= 15) & (df['days_to_report'] >= 0)]
part1 = df_filtered[df_filtered['crime_seriousness'] == 1]['days_to_report']
part2 = df_filtered[df_filtered['crime_seriousness'] == 2]['days_to_report']
plt.boxplot([part1, part2], labels=['Part 1 (Serious)', 'Part 2 (Less Serious)'])
plt.title("Days to Report by Crime Seriousness (within 15 days)")
plt.xlabel("Crime Seriousness")
plt.ylabel("Days to Report")
plt.tight_layout()
plt.savefig("charts/days_to_report.png")
plt.close()

# Reporting delay by crime type
plt.figure(figsize=(14, 6))
df_filtered = df[(df['days_to_report'] <= 15) & (df['days_to_report'] >= 0)]
top_crimes = df_filtered['crime'].value_counts().head(10).index
data = [df_filtered[df_filtered['crime'] == crime]['days_to_report'].values for crime in top_crimes]
plt.boxplot(data, tick_labels=top_crimes)
plt.title("Reporting Delay by Crime Type (Top 10)")
plt.xlabel("Crime Type")
plt.ylabel("Days to Report")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("charts/reporting_delay_by_crime.png")
plt.close()

# Crime heatmap
plt.figure(figsize=(15, 6))
pivot = df.pivot_table(index='day_of_week', columns='hour', aggfunc='size', fill_value=0)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot = pivot.reindex(days_order)
plt.imshow(pivot, aspect='auto', cmap='YlOrRd')
plt.colorbar(label='Number of Crimes')
plt.xticks(range(24), range(24))
plt.yticks(range(7), days_order)
plt.title("Crime Heatmap by Hour and Day")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
plt.tight_layout()
plt.savefig("charts/heatmap.png")
plt.close()

# Crime trends through years
plt.figure(figsize=(12, 6))
top5 = df['crime'].value_counts().head(5).index
trends = df[df['crime'].isin(top5)].groupby(['year', 'crime']).size().unstack()

for crime in trends.columns:
    plt.plot(trends.index, trends[crime], marker='o', label=crime)

plt.title("Top 5 Crime Trends by Year")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.xticks([2020, 2021, 2022, 2023])
plt.legend()
plt.tight_layout()
plt.savefig("charts/crime_trends.png")
plt.close()

# Identity theft age distribution
plt.figure(figsize=(10,6))
identity_theft = df[df['crime'] == 'THEFT OF IDENTITY']
plt.hist(identity_theft['victim_age'], bins=20)
plt.title("Identity Theft Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/identity_theft_age_dist.png")
plt.close()

# Identity theft by % of crime per area
total_by_area = df.groupby('area').size()
identity_by_area = df[df['crime'] == 'THEFT OF IDENTITY'].groupby('area').size()
identity_pct = (identity_by_area / total_by_area * 100).sort_values(ascending=True).tail(10)

plt.figure(figsize=(10,6))
plt.bar(identity_pct.index, identity_pct.values)
plt.title("Identity Theft by Percentage of Crime Per Area")
plt.xlabel("Area")
plt.ylabel("Percentage")
plt.tight_layout()
plt.savefig("charts/identity_crime_percentage.png")
plt.close()