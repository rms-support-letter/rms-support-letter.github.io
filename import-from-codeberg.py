import requests
from _importer import parse_and_import_signature


page = 1
while True:
    comments = requests.get(f"https://codeberg.org/api/v1/repos/rms-support-letter/rms-support-letter/issues/comments?page={page}").json()
    if not comments:
        break
    for comment in comments:
        author = comment["user"]["login"]
        content = comment["body"]
        parse_and_import_signature(content, author)
    page += 1
