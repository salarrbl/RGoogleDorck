import requests
import sys
import random
from bs4 import BeautifulSoup
import urllib.parse

# Function to load proxies from a file
def load_proxies(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]

# Function to get a random proxy from the list
def get_random_proxy(proxies):
    return random.choice(proxies)

# Update the search_google function to use a proxy
def search_google(dork, start, proxies):
    query = urllib.parse.quote(dork)
    url = f"https://www.google.com/search?q={query}&start={start}"
    # Get a random proxy
    proxy = get_random_proxy(proxies)
    proxy_dict = {
        "http": proxy,
        "https": proxy,
    }
    response = requests.get(url, proxies=proxy_dict)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract URLs from search results
    links = []
    for item in soup.find_all('a'):
        href = item.get('href')
        if href and "url?q=" in href:
            url = href.split("url?q=")[1].split("&")[0]
            links.append(url)

    return links

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <dorks_file> <proxy_file>")
        return

    dorks_file = sys.argv[1]
    proxy_file = sys.argv[2]

    with open(dorks_file, 'r') as file:
        dorks = file.readlines()

    # Load proxies from the file
    proxies = load_proxies(proxy_file)

    all_links = []
    start = input("Enter the start parameter for Google search: ")

    for dork in dorks:
        print(f"Searching for dork: {dork.strip()}")
        links = search_google(dork.strip(), start, proxies)
        all_links.extend(links)

    print("Found URLs:")
    for link in all_links:
        print(link)
        with open('results.txt', 'a') as file:
            file.write(link + '\n')

if __name__ == "__main__":
    main()

