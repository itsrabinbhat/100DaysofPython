from bs4 import BeautifulSoup
import requests
WEBSITE = 'https://news.ycombinator.com/news'

res = requests.get(WEBSITE)
yc_webpage_content = res.text

# Extract News article title, link and up voted points
soup = BeautifulSoup(yc_webpage_content, 'html.parser')
articles = soup.find_all('span', class_='titleline')
articles = [span.find('a') for span in articles]
article_titles = [article.text for article in articles]
article_links = [article.get('href') for article in articles]
article_upvotes = [int(score.text.split(' ')[0]) for score in soup.find_all('span', class_='score')]

# Finding the article with the highest up votes
idx_of_max_upvote = article_upvotes.index(max(article_upvotes))

print(article_titles)
print(article_links)
print(article_upvotes)
print(f"The article with the highest upvotes:\nTitle: {article_titles[idx_of_max_upvote]}\n"
      f"Link: {article_links[idx_of_max_upvote]}\nUp votes: {article_upvotes[idx_of_max_upvote]}")
