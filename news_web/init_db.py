from web_server.models import NewsItem, Subscription


if __name__ == '__main__':
    NewsItem.ensure_indexes()
    Subscription.ensure_indexes()
