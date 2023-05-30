from bs4 import BeautifulSoup

html_file = open("generic_simple.html", mode="r", encoding="utf-8")
content = html_file.read()
soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())

# print(soup.get_text())
# print(soup.title)
# print(soup.find("div"))

for i in soup.find_all("a"):
    i["href"]
print(i)
