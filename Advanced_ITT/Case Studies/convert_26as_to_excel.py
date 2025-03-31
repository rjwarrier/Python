import pandas as pd   # For working with tabular data and exporting to Excel
import re             # For using regular expressions to extract structured text
import os             # For handling file paths

# Step 1: Define the path to the input 26AS text file
source_path = r'C:\Users\ranji\Downloads\ARXPR8200M-2015\ARXPR8200M-2015.txt'

# Step 2: Get the folder path where the source file is located
output_dir = os.path.dirname(source_path)

# Step 3: Open and read the content of the text file
with open(source_path, 'r') as file:
    raw_text = file.read()

# Step 4: Extract only the "PART A - TDS" section from the text
deductors = raw_text.split(
    "^PART A - Details of Tax Deducted at Source^")[1].split("^PART A1 -")[0]

# Step 5: Split the text into separate blocks based on deductor entries
deductor_blocks = re.split(r'\n(?=\d+\^)', deductors.strip())

# Step 6: Loop through each block and extract relevant data into a list of dictionaries
records = []
for block in deductor_blocks:
    lines = block.strip().split('\n')  # Split block into individual lines
    # First line has the deductor's name and TAN
    header_line = lines[0]
    deductor_info = header_line.split("^")
    deductor_name = deductor_info[1]   # Extract deductor name
    tan = deductor_info[2]             # Extract TAN

    # Step 7: Loop through each transaction line within the block
    for line in lines[1:]:
        if line.strip().startswith("^") and not "No Transactions Present" in line:
            # Remove leading/trailing ^ and split
            parts = line.strip("^").split("^")
            if len(parts) == 9:
                # Append parsed transaction to records list
                records.append({
                    "Deductor Name": deductor_name,
                    "TAN": tan,
                    "Sr. No.": parts[0],
                    "Section": parts[1],
                    "Transaction Date": parts[2],
                    "Status of Booking": parts[3],
                    "Date of Booking": parts[4],
                    "Remarks": parts[5],
                    "Amount Paid / Credited (Rs.)": parts[6],
                    "Tax Deducted (Rs.)": parts[7],
                    "TDS Deposited (Rs.)": parts[8]
                })

# Step 8: Convert the list of records into a Pandas DataFrame
df = pd.DataFrame(records)

# Step 9: Create full path to save the Excel file in the same folder as the input file
output_excel_path = os.path.join(output_dir, "Form26AS_TDS_Converted.xlsx")

# Step 10: Write the DataFrame to an Excel file (requires openpyxl installed)
df.to_excel(output_excel_path, index=False)

# Step 11: Print the saved file location
print(f"Excel file saved at: {output_excel_path}")
