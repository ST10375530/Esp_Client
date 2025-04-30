import requests

def get_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'za',  # South Africa
        'apiKey': 'e6a38ddfb9384b47a8c2e936cb3ba2cb'
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    news = get_news()
    print(news)
