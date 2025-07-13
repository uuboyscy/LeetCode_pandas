from pathlib import Path

import requests
from bs4 import BeautifulSoup

question_num = 185
url = """
https://leetcode.com/problems/department-top-three-salaries/description/
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

res = requests.get(url.strip(), headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

content = soup.select_one('meta[property="og:description"]').get("content")
content = '"""\n' + content + '\n"""\n'

title = soup.select_one('head > title').text.replace("- LeetCode", "")
title = title.strip().replace(" ", "_").lower()

python_file_name = f"_{question_num:05d}_{title}.py"

print(python_file_name)
python_file_path = Path(python_file_name)
if not python_file_path.exists():
    with python_file_path.open("w", encoding="utf-8") as f:
        f.write(content)
else:
    raise FileExistsError(f"File {python_file_name} already exists")
