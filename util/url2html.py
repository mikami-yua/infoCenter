"""
Module: url_to_html.py

功能: 接收URL列表或RSS抓取结果，将每条新闻内容抓取为HTML，封装在JSON内。
适合后续发送给LLM做内容分析。
"""

import requests
from typing import List, Dict


def fetch_html_for_entries(entries: List[Dict]) -> List[Dict]:
    """
    输入: entries = [{"title": ..., "link": ...}, ...]
    输出: [{"title": ..., "link": ..., "html": ...}, ...]
    """
    results = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for entry in entries:
        url = entry.get("link")
        if not url:
            continue
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            html_content = resp.text
            results.append({
                "title": entry.get("title"),
                "link": url,
                "html": html_content
            })
        except Exception as e:
            results.append({
                "title": entry.get("title"),
                "link": url,
                "html": f"Error fetching content: {str(e)}"
            })
    return results


# 示例调用
if __name__ == "__main__":
    test_entries = [
        {"title": "Example", "link": "https://www.bloomberg.com/opinion/articles/2025-11-15/beef-prices-are-high-trump-needs-a-useful-villain"}
    ]
    html_json = fetch_html_for_entries(test_entries)
    import json
    print(json.dumps(html_json, indent=2, ensure_ascii=False))