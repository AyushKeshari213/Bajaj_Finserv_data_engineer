# Impute missing gender values with mode
mode_gender = df_patient['gender'].mode()[0]
df_patient['gender'].fillna(mode_gender, inplace=True)

# Calculate percentage of females
female_percentage = ((df_patient['gender'] == 'F').sum() / len(df_patient)) * 100
print(round(female_percentage, 2))  # Output: 32.26

