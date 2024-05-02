import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import csv

#improved - store a visited link in a file for future skip 

class HTMLScraper:

    def __init__(self,base_url,folderPath,visited_url_path ,max_depth=1):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_url_path = visited_url_path
        self.folderPath = folderPath

    # extract name for file from url 
    def split_url(self,url):
        path = url.replace(base_url, "")
        # Sanitize the path to remove invalid characters for directory names
        path = path.replace("/", "-").replace("\\", "-").strip("-")
        # Remove leading slash if present
        if path.startswith("/"):
            path = path[1:]

        if path.endswith("/"):
            path = path[:-1]

        return path


    def get_html_data(self,url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve HTML data from {url}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while retrieving HTML data from {url}: {e}")
            return None

    #save html data on file - working on this 
    def save_html_data(self,url,html_data):
        file_name  = self.split_url(url)
        
        if(file_name == ""):
            file_name = "home"
        file_path = os.path.join(self.folderPath, f"{file_name}.html")
        index_csv_file = os.path.join(self.folderPath, 'index.csv')
         # Ensure that the directory exists, create it if not
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_data)

        with open(index_csv_file, 'w',newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["file","source"])
            writer.writerow([file_name,url])
       


    # explore links on the page also save the html data
    def explore_links(self, url=None, max_depth=None, current_depth=0):
        print(f"current depth : {current_depth}")
        if url is None:
            url = self.base_url

        if self.base_url not in url:
            print(f"Skipping URL {url} as it does not belong to the base URL {self.base_url}")
            return

        if max_depth is None:
            max_depth = self.max_depth

        if current_depth > max_depth:
            return

        visited_urls = set()
        if os.path.exists(self.visited_url_path):
            with open(self.visited_url_path, 'r', encoding='utf-8') as visited_file:
                visited_urls = set(visited_file.read().splitlines())

        if url in visited_urls:
            print(f"URL {url} has already been visited. Skipping...")
            return

        html_data = self.get_html_data(url)
        if html_data:
            self.save_html_data(url, html_data)
            visited_urls.add(url)
            with open(self.visited_url_path, 'a', encoding='utf-8') as visited_file:
                visited_file.write(url + '\n')
            soup = BeautifulSoup(html_data, 'html.parser')
            links = soup.find_all('a', href=True)

            for link in links:
                absolute_url = urljoin(url, link['href'])
                if absolute_url.startswith(self.base_url):
                    print(f"Exploring link: {absolute_url}")
                    self.explore_links(absolute_url, max_depth, current_depth + 1)





# call class
base_url = "https://attack.mitre.org"
folder_path = "html-data/mitre-attack"
visited = "html-data/mitre-attack/visited_url.csv"
max_depth = 1000
scraper = HTMLScraper(base_url,folder_path,visited,max_depth) # max depth 100
scraper.explore_links() # start exploring links and save to location