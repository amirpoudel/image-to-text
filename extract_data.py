from bs4 import BeautifulSoup
import re

# Assuming html_content contains the HTML data
soup = BeautifulSoup(html_content, 'html.parser')

# Extract change summary
change_summary = soup.find('h1').text.strip()

# Extract change details
change_details = []
techniques = soup.find_all('h4')
for technique in techniques:
    technique_id = re.search(r'\[([^]]+)\]', technique.text).group(1)
    technique_name = technique.text.split(']')[1].strip()
    current_version = technique.find_next('b').text.strip()
    description = technique.find_next('p').text.strip()
    change_details.append({
        'technique_id': technique_id,
        'technique_name': technique_name,
        'current_version': current_version,
        'description': description
    })
