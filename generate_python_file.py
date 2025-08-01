from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

URL = """
https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/
""".strip()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

session = requests.Session()
session.get(URL, headers=headers)

# Use GraphQL to get question frontendId
graphql_url = "https://leetcode.com/graphql"
slug = [p for p in urlparse(URL).path.split("/") if p][1]
query = {
    "operationName": "questionTitle",
    "variables": {"titleSlug": slug},
    "query": """
    query questionTitle($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
      }
    }
    """
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Referer": f"https://leetcode.com/problems/{slug}/",
    "x-csrftoken": session.cookies.get("csrftoken", ""),
    "Content-Type": "application/json"
}

res = session.post(graphql_url, json=query, headers=headers)
data = res.json()

question_num = int(data["data"]["question"]["questionFrontendId"])
title = data["data"]["question"]["title"].replace(" ", "_").lower()
filename = f"_{question_num:05d}_{title}.py"

# Get the problem description
res_html = session.get(URL.strip(), headers=headers)
soup = BeautifulSoup(res_html.text, "html.parser")
description = soup.select_one('meta[property="og:description"]').get("content")  # type: ignore
content = f'"""\n{description}\n"""\n'

# Save the file
python_file_path = Path(filename)
print(python_file_path)
if not python_file_path.exists():
    with python_file_path.open("w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {filename}")
else:
    raise FileExistsError(f"File {filename} already exists")