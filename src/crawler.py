import requests
from bs4 import BeautifulSoup
from datetime import datetime

from src.models import Post


def get_posts(target_date):
    response = requests.get('https://ara.kaist.ac.kr/board/Food/')

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('table.articleList tbody tr')

    posts = []
    for row in rows:
        published_date = datetime \
            .strptime(row.select('td.date')[0].text, '%Y/%m/%d') \
            .date()
        if published_date == target_date:
            post_id = row.select('td.articleid')[0].text
            title = row.select('td.title')[0].text
            posts.append(Post(post_id, title, published_date).text)

    return posts
