from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def news_search(request):
    keyword = request.GET.get('q', '')  # Assuming 'q' is the query parameter
    news_list = []

    if keyword:
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for news_item in soup.find_all('a', class_='news_tit'):
            title = news_item.get('title')
            link = news_item.get('href')
            news_list.append({'title': title, 'link': link})

    return render(request, 'data/newssearch.html', {'news_list': news_list})


