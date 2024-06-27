from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com'

response = requests.get(url=URL)
yc_webpage = response.content
soup = BeautifulSoup(yc_webpage, 'html.parser')
titles = soup.find_all(name='span', class_='titleline')
news_titles = []
news_links = []
for title in titles:
    news_titles.append(title.getText())
    news_links.append(title.find(name='a').get('href'))


scores = soup.find_all(name='span', class_='score')
viewer_scores = []
for score in scores:
    viewer_scores.append(int(score.getText().split()[0]))


print(f'Most upvoted article: {news_titles[viewer_scores.index(max(viewer_scores))]} \nNumber of upvotes: {max(viewer_scores)} \nAvailable at:{news_links[viewer_scores.index(max(viewer_scores))]} ')


