import feedparser
import json
from src import config_info

class RSSFetcher:
    def __init__(self, config):
        self.config = config
        self.source = config.get("source")
        self.parser = config.get("parser")

    def fetch(self):
        return feedparser.parse(self.source)

    def parse(self, feed):
        if callable(self.parser):
            return self.parser(feed)

        # 默认返回标题和链接
        return [{"title": entry.title, "link": entry.link} for entry in feed.entries]

def filter_entries(entries, filters):
    """根据 filters 筛选条目"""
    results = {}
    for topic, keywords in filters.items():
        matched = []
        for entry in entries:
            title_lower = entry["title"].lower()
            if any(kw.lower() in title_lower for kw in keywords):
                matched.append(entry)
        results[topic] = matched
    return results

def main():
    all_entries = []
    # 抓取所有 RSS 源
    for item in config_info.CONFIG:
        fetcher = RSSFetcher(item)
        try:
            feed = fetcher.fetch()
            parsed_entries = fetcher.parse(feed)
            all_entries.extend(parsed_entries)
        except Exception as e:
            print(f"Error fetching {item.get('name')}: {str(e)}")

    # 根据 FILTERS 过滤感兴趣的条目
    filtered_results = filter_entries(all_entries, config_info.FILTERS)
    print(json.dumps(filtered_results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()