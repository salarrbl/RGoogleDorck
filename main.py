import requests
import random
from bs4 import BeautifulSoup
import urllib.parse

# List of Google Dorks
dorks = [
    '"inurl:login"',
    '"inurl:admin login"',
    '"intitle:"login" inurl:"login""',
    '"inurl:"/admin" intitle:"login""',
    '"inurl:"login" intext:"username" intext:"password""',
    '"inurl:login site:example.com "type="password"""',
    '"inurl:wp-login.php"',
    '"inurl:administrator login"',
    '"inurl:admin/index.php"',
    '"inurl:admin intitle:"login""'
]
user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:112.0) Gecko/20100101 Firefox/112.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36 Edge/110.0.1587.57'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0.3 Safari/537.36'
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1'
    'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1'
    'Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.200205.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/70.0.3728'
    'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; AS; rv:11.0) like Gecko'
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)'
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)'
    'Mozilla/5.0 (compatible; DuckDuckBot/1.0; +https://duckduckgo.com/duckduckbot)'
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'
    'Mozilla/5.0 (Linux; Android 9; Pixel 2 Build/PQ3A.190801.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36 TelegramBot/5.15'

]
def search_google(dork,start):
    query = urllib.parse.quote(dork)
    url = f"https://www.google.com/search?q={query}&start={start}"
    random_user_agent = random.choice(user_agent)
    headers = {"User-Agent": random_user_agent}

    response = requests.get(url, headers=headers)
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

