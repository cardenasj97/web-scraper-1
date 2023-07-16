import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.juan-cardenas.com/"
response = requests.get(url)
html_content = response.text
# print(f"Your request to {url} came back w/ status code {response.status_code}")
# print(response.text)

soup = BeautifulSoup(html_content, "html.parser")
# print(soup)

links = soup.find_all("a")

# keyword = "About"
# links = soup.find_all("a", text=lambda text: text and keyword in text.lower())
# print(titles)

data = []

for link in links:
    linkText = link.text
    if linkText != "" and "About" in linkText:
        data.append([linkText])

# print(data)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Done!")
