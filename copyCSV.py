import csv

def copy_urls(source_csv, destination_csv):
    with open(source_csv, 'r', newline='') as source_file:
        reader = csv.reader(source_file)
        next(reader)  # Skip header row
        urls = [row[1] for row in reader]  # Extract URLs from the second column

    with open(destination_csv, 'w', newline='') as dest_file:
        writer = csv.writer(dest_file)
        for url in urls:
            writer.writerow([url])

# Example usage
source_csv = 'html-data/mitre-attack/index.csv'
destination_csv = 'html-data/mitre-attack/visited_url.csv'
copy_urls(source_csv, destination_csv)
print("URLs copied successfully!")