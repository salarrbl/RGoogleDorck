import requests
import sys
import random
from bs4 import BeautifulSoup
import urllib.parse

with open(sys.argv[1], 'r') as file:
    dorks = file.readlines()

def search_google(dork,start):
    query = urllib.parse.quote(dork)
    url = f"https://www.google.com/search?q={query}&start={start}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(response.status_code)
    # Extract URLs from search results
    links = []
    for item in soup.find_all('a'):
        href = item.get('href')
        if href and "url?q=" in href:
            url = href.split("url?q=")[1].split("&")[0]
            links.append(url)

    return links

def main():
    all_links = []
    start = input("enter dusi:")
    for dork in dorks:
        print(f"Searching for dork: {dork}")
        links = search_google(dork,start)
        all_links.extend(links)

    print("Found URLs:")
    for link in all_links:
        print(link)
        with open('results.txt', 'a') as file:
            file.write(link + '\n')
if __name__ == "__main__":
    main()

