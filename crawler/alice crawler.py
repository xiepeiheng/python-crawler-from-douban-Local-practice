import urllib.request
from bs4 import BeautifulSoup
import re

result = urllib.request.urlopen('http://127.0.0.1:5000/alice')
html = result.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
print(soup)