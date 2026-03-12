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

# Crimes by month
plt.figure(figsize=(10,6))
months_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
monthly_crime = df['month'].value_counts().sort_index()
plt.bar(monthly_crime.index, monthly_crime.values)
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.title("Crimes by Month")
plt.xlabel("Month")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/crimes_by_month.png")
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


# Crimes by day of week
plt.figure(figsize=(10,6))
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_crime = df['day_of_week'].value_counts().reindex(days_order)
plt.bar(daily_crime.index, daily_crime.values)
plt.title("Crimes by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/crimes_by_day.png")
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

# Male vs Female
plt.figure(figsize=(10,6))
crimes_by_sex = df['victim_sex'].value_counts()
plt.bar(crimes_by_sex.index, crimes_by_sex.values)
plt.title("Victims by Sex")
plt.xlabel("Sex")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("charts/victims_by_sex.png")
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
plt.figure(figsize=(10, 6))
df_filtered = df[[]]
part1 = df_filtered[df_filtered['crime_seriousness'] == 1]['days_to_report']
part2 = df_filtered[df_filtered['crime_seriousness'] == 2]['days_to_report']
plt.boxplot([part1, part2], labels=['Part 1 (Serious)', 'Part 2 (Less Serious)'])
plt.title("Days to Report by Crime Seriousness (within 15 days)")
plt.xlabel("Crime Seriousness")
plt.ylabel("Days to Report")
plt.tight_layout()
plt.savefig("charts/days_to_report.png")
plt.close()