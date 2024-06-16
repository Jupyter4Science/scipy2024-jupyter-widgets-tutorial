

plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Global Temperature versus Time')
plt.plot(selected_df['Year'], selected_df['Temperature'])  # plt.plot(subset_df['Year'], subset_df['Temperature'], label='Raw Data')
plt.plot(selected_df['Year'], selected_df['Savitzky-Golay']) # plt.plot(subset_df['Year'], subset_df[SG_col], label='Savitzky-Golay Filtered')
plt.show()
