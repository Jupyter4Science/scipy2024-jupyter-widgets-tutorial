
plt.xlabel('Year')
plt.ylabel('Temperature Anomalies over Land w.r.t. 1951-80 (˚C)')
plt.title('Global Annual Mean Surface Air Temperature Change')
plt.plot(selected_df['Year'], selected_df['Temperature'], label='Raw Data')  # plt.plot(subset_df['Year'], subset_df['Temperature'], label='Raw Data')
plt.plot(selected_df['Year'], selected_df['Smoothed Data'], label='Smoothed Data') # plt.plot(subset_df['Year'], subset_df[SG_col], label='Smoothed Data')
plt.legend()
plt.show()
