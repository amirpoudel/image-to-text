import csv

def extract_sources(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        urls = [row[1].strip() for row in reader if len(row) >= 2]

    with open(output_csv, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for url in urls:
            writer.writerow([url])

# Example usage
input_csv = 'html-data/mitre-attack/index.csv'
output_csv = 'html-data/mitre-attack/visited_url.csv'
extract_sources(input_csv, output_csv)



def remove_duplicate_file_source(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)

    first_row_written = False
    with open(output_csv, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for row in rows:
            if not first_row_written:
                writer.writerow(row)
                first_row_written = True
            elif row != ['file', 'source']:
                writer.writerow(row)

# Example usage
# input_csv = 'html-data/mitre-attack/index.csv'
# output_csv = 'html-data/mitre-attack/index.csv'
# remove_duplicate_file_source(input_csv, output_csv)


# # Example usage
# source_csv = 'html-data/mitre-attack/index.csv'
# destination_csv = 'html-data/mitre-attack/visited_url.csv'
# copy_urls(source_csv, destination_csv)
# print("URLs copied successfully!")