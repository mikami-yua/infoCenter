# config_info.py

# 配置列表，每个字典表示一个抓取目标
CONFIG = [
    {
        "name": "Economics",
        "source": "https://feeds.bloomberg.com/economics/news.rss",
        "parser": None,
    },
    {
        "name": "Industries",
        "source": "https://feeds.bloomberg.com/industries/news.rss",
        "parser": None,
    },
    {
        "name": "Green",
        "source": "https://feeds.bloomberg.com/green/news.rss",
        "parser": None,
    },
    {
        "name": "Markets",
        "source": "https://feeds.bloomberg.com/markets/news.rss",
        "parser": None,
    },
    {
        "name": "Politics",
        "source": "https://feeds.bloomberg.com/politics/news.rss",
        "parser": None,
    },
    {
        "name": "Technology",
        "source": "https://feeds.bloomberg.com/technology/news.rss",
        "parser": None,
    },
    {
        "name": "Wealth",
        "source": "https://feeds.bloomberg.com/wealth/news.rss",
        "parser": None,
    },
    {
        "name": "BView",
        "source": "https://feeds.bloomberg.com/bview/news.rss",
        "parser": None,
    },
]


# 新增关注主题/关键词配置
FILTERS = {
    "BTC": ["BTC", "Bitcoin", "Crypto"],
    "NVIDIA": ["NVIDIA", "NVDA", "GPU", "Graphics"],
    "AI":["AI"]
    # 可以继续添加其他关注主题
}