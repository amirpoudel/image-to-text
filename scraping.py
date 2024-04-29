import csv
import requests
from bs4 import BeautifulSoup

url = 'https://attack.mitre.org/software/'

def get_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        print('Success!')
        print(response.text)
        #write the content to a file
        with open('html-data/mitre_attack_software.html', 'w') as file:
            file.write(response.text)

        with open('html-data/html-index.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["file","source"])
            writer.writerow(["mitre_attack_software.html",url])

    else:
        print('Failed to fetch the page. Status code:', response.status_code)




def parsed_page():
    with open('html-data/mitre_attack_software.html', 'r') as file:
        html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table containing the software data
        table = soup.find('table', class_='table')

        # Check if the table is found
        if table:
            # Extracting table headers
            headers = [th.text.strip() for th in table.find('thead').find_all('th')]

            # Initialize list to store data
            data_rows = []

            # Extract data from each row of the table body
            for row in table.find('tbody').find_all('tr'):
                # Extract data from each cell of the row
                cells = row.find_all(['th', 'td'])
                row_data = [cell.text.strip() for cell in cells]
                data_rows.append(row_data)

            # Define the path for the output CSV file
            output_file_path = 'software_data.csv'

            # Write the extracted data to the CSV file
            with open(output_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                # Write header row
                writer.writerow(headers)
                # Write data rows
                writer.writerows(data_rows)

            print(f"Data saved to {output_file_path}")
        else:
            print('Table not found')

# Call the function to parse the page
parsed_page()