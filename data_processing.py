import pandas as pd
import os

# Define the data folder path
data_folder = 'data'

# List to store dataframes from each CSV file
all_data = []

# Process each CSV file in the data folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

for csv_file in csv_files:
    file_path = os.path.join(data_folder, csv_file)
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Filter for Pink Morsels only
    df = df[df['product'] == 'pink morsel']
    
    # Create sales column (quantity * price)
    df['sales'] = df['quantity'] * df['price']
    
    # Select only the required columns and rename
    df = df[['sales', 'date', 'region']]
    
    # Append to list
    all_data.append(df)

# Combine all dataframes
combined_df = pd.concat(all_data, ignore_index=True)

# Save to output file
output_file = 'output.csv'
combined_df.to_csv(output_file, index=False)

print(f"✅ Processing complete! Output saved to {output_file}")
print(f"📊 Total rows: {len(combined_df)}")
print(f"\n🔍 Preview of output:")
print(combined_df.head(10))