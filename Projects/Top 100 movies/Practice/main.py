from bs4 import BeautifulSoup
import requests

with open("website.html") as file:
    content=file.read()

soup=BeautifulSoup(content,'html.parser')
# print(soup.prettify())
print(soup.title) #return element
print(soup.title.name) #return tag name
print(soup.title.string) #return text inside tag
all_anchor=soup.find_all(name="a") #select all tags
print(all_anchor)

for anchor in all_anchor:
    print(anchor.getText())
    print(anchor.get("href"))

head=soup.find(name="h1",id="name") #select using id
print(head)
section_head=soup.find(name="h3",class_="heading") #select using class
print(section_head)
docs=soup.select_one(selector="p a") #nested selection using parent
print(docs)
heading=soup.select(".heading") #using selector class
print(heading)
head2=soup.select("#name") # using selector id
print(head2)

response=requests.get(url="https://news.ycombinator.com/news")
y_news=response.text

soup2=BeautifulSoup(y_news,'html.parser')
anchor=soup2.select_one(selector=".titleline a")
headings=anchor.getText()
link=anchor.get("href")
upvote=soup2.find(name="span" ,class_="score").getText()

print(headings,link,upvote)


