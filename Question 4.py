# Replace empty strings with NaN for proper handling of missing values
df_patient.replace('', pd.NA, inplace=True)

# Calculate percentage of missing values
missing_values = df_patient[['firstName', 'lastName', 'birthDate']].isna()
missing_percentage = (missing_values.sum() / len(df_patient)) * 100
print(missing_percentage.round(2))  # Output: 0.00, 70.97, 32.26
