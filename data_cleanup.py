import pandas as pd

# Read CSV file
df = pd.read_csv('scholarship_data.csv')

# Drop rows with missing values in the 'View Link' column
if 'View Link' in df.columns:
    df.dropna(subset=['View Link'], inplace=True)
else:
    print("Error: 'View Link' column not found in the dataset.")

# Remove any leading or trailing whitespaces from links
if 'View Link' in df.columns:
    df['View Link'] = df['View Link'].str.strip()

# Remove any duplicate links
if 'View Link' in df.columns:
    df.drop_duplicates(subset=['View Link'], keep='first', inplace=True)

# Reset index after dropping rows
df.reset_index(drop=True, inplace=True)

# Save the cleaned dataset to a new CSV file named 'scholarship_links_cleaned.csv'
df.to_csv('scholarship_links_cleaned.csv', index=False)

print("Cleaned dataset saved as 'scholarship_links_cleaned.csv'")
