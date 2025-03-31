import pandas as pd
import os

# Step 1: Define the folder containing the CSV files
folder_path = r'C:\Users\ranji\OneDrive\Academics\Classes Taken By Me\Advanced ITT\2021_Syllabus\Class Materials\Excel\PowerQuery\BhavCopy'  # <-- Change this path

# Step 2: Define the output file name
output_filename = 'Combined_Bhavcopy.csv'  # <-- Change the name if needed

# Step 3: Construct the full output file path
output_csv = os.path.join(folder_path, output_filename)

# Step 4: Check if the output file already exists — ABORT if it does
if os.path.exists(output_csv):
    print(
        f"File '{output_filename}' already exists in the folder. Aborting to avoid overwriting the existing file.")
    exit()

# Step 5: List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Step 6: Create a list to store DataFrames
all_dataframes = []

# Step 7: Read and append each CSV file
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df['Source File'] = file  # Optional: Add source file name column
    all_dataframes.append(df)

# Step 8: Combine all DataFrames into one
combined_df = pd.concat(all_dataframes, ignore_index=True)

# Step 9: Export the final DataFrame to a CSV file
combined_df.to_csv(output_csv, index=False)

# Final Step: Confirm to the user
print(f"✅ Combined CSV saved to: {output_csv}")
