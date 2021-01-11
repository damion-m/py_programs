# Code Tutorial from https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46

import requests
import re
import pandas as pd
import csv
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os


# class with functions for crawling
class PyCrawler(object):
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()
       # self.proxy_orbit_key = os.getenv("PROXY_ORBIT_TOKEN")
       # self.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        #self.proxy_orbit_url = f"https://api.proxyorbit.com/v1/?token={self.proxy_orbit_key}&ssl=true&rtt=0.3&protocols=http&lastChecked=30"

    def get_html(self, url):
        try:
           # proxy_info = requests.get(self.proxy_orbit_url).json()
            #proxy = proxy_info['curl']
            html = requests.get(url)#',' headers={"User-Agent":self.user_agent}, proxies={"https":proxy, "https":proxy}, timeout=5)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    # method for getting links from htmls visited
    def get_links(self, url):
        html = self.get_html(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)
        for i, link in enumerate(links):
            if not urlparse(link).netloc:
                link_with_base = base + link
                links[i] = link_with_base

        return set(filter(lambda x: 'mailto' not in x, links))

    # Extract info from pages
    def extract_info(self, url):
        html = self.get_html(url)
        meta = re.findall("<meta .*?name=[\"'](.*?)['\"].*?content=[\"'](.*?)['\"].*?>", html)
        return dict(meta)

    def create_dataframe(self, url):
       data = self.get
        symbols = []
        names = []
        last_sales = []
        change_nets = []
        share_volumes = []

        for row in meta:
            columns= row.findall('td')
            if(len(columns)):
                names.append(columns[1].text)
                last_sales.append(columns[2].text)
                change_nets.append(columns[3].text)
                share_volumes.append(columns[4].text)
        data = pd.DataFrame(data = names, last_sales, change_nets, share_volume, columns=Names, Last Sales, Change Nets, Share Volumes)
        return data
    # Crawl each page and extract each link
    def crawl(self, url):
        for link in self.get_links(url):
            if link in self.visited:
                continue
            self.visited.add(link)
            info = self.extract_info(link)

           # print(f"""Link: {link} Description: {info.get('description')} Keywords: {info.get('keywords')}""")
            print
            data = self.create_dataframe()
            self.crawl(link)

    def start(self):
        self.crawl(self.starting_url)

if __name__ == "__main__":
    usr_input = input("Enter url")
    crawler = PyCrawler(usr_input)
    crawler.start()
