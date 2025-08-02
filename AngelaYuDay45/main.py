from bs4 import BeautifulSoup
import requests
# with open("./website.html","r") as file:
#     data = file.read()
# soup = BeautifulSoup(data,'html.parser')
# print(soup.title)
# print(soup.title.string)
#print(soup.prettify())
# print(soup.li) finding the first list .a first anchor etc.

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())

# heading = soup.find(name="h1", id="name")
# print(heading.string)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url)
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage,"html.parser")

articles = soup.find_all(name="span", class_="titleline")
articles_votes = soup.find_all(name="span", class_="score")
article_titles = []
article_links = []
article_upvotes = []
for article in articles:
    article_deeper = article.find(name="a")
    article_titles.append(article_deeper.getText())
    article_links.append(article_deeper.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in articles_votes]

# print(article_titles)
# print(article_links)
# print(article_upvotes)

maximum = max(article_upvotes)
index = article_upvotes.index(maximum)
print(f"Max upvoted site is {article_titles[index]} it's link : {article_links[index]} "
      f"Upvote : {maximum}")


# for title in articles_deeper:
#     print(f"article title{title} : {articles_deeper.get_Text()}")
# article_link = articles_deeper.get("href")
# print(f"article link : {article_link}")
# article_upvotes = soup.find(name="span", class_="score").getText()
# print(f"article upvotes : {article_upvotes}")
# print(f"article : {articles}")