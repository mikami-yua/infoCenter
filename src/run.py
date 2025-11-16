# run.py
import json
from src import bloomberg_info
from src import config_info
from util import url2html

def main():
    # 1️⃣ 获取所有 RSS 条目
    all_entries = []
    for rss_cfg in config_info.CONFIG:
        fetcher = bloomberg_info.RSSFetcher(rss_cfg)
        try:
            feed = fetcher.fetch()
            parsed_entries = fetcher.parse(feed)
            all_entries.extend(parsed_entries)
        except Exception as e:
            print(f"Error fetching {rss_cfg.get('name')}: {str(e)}")

    # 2️⃣ 根据 FILTERS 筛选感兴趣条目
    filtered_results = bloomberg_info.filter_entries(all_entries, config_info.FILTERS)

    # 3️⃣ 合并所有关注主题条目为单列表，去掉重复 URL
    urls_to_fetch = {}
    for topic_entries in filtered_results.values():
        for entry in topic_entries:
            urls_to_fetch[entry['link']] = entry['title']  # 使用 dict 去重

    entries_list = [{'title': title, 'link': link} for link, title in urls_to_fetch.items()]

    # 4️⃣ 将 URL 转成 HTML
    html_json = url2html.fetch_html_for_entries(entries_list)

    # 5️⃣ 输出结果
    print(json.dumps(html_json, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()