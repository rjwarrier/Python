import requests
from bs4 import BeautifulSoup
import pandas as pd

# IPL Points Table URL
url = "https://www.iplt20.com/points-table/men"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the points table
table = soup.find('table', class_='ih-td-tab table table-striped')

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract all table rows
rows = table.find_all('tr')[1:]  # Skip header row

# Extract the row data
table_data = []
for row in rows:
    cols = [col.text.strip() for col in row.find_all('td')]
    table_data.append(cols)

# Convert to DataFrame
points_table = pd.DataFrame(table_data, columns=headers)

# Display the full points table
print(points_table)
