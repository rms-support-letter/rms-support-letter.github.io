import requests
import os


page = 1
while True:
    comments = requests.get(f"https://codeberg.org/api/v1/repos/rms-support-letter/rms-support-letter/issues/comments?page={page}").json()
    if not comments:
        break
    for comment in comments:
        author = comment["user"]["login"]
        content = comment["body"]

        content_lines = [line.strip() for line in content.replace("`", "").strip().split("\n") if line.strip()]
        for i in range(len(content_lines) - 1):
            if content_lines[i].lower().startswith("name:") and content_lines[i + 1].lower().startswith("link:"):
                if not os.path.isfile(f"_data/signed/{author}.yaml"):
                    with open(f"_data/signed/{author}.yaml", "w") as f:
                        f.write("name:" + content_lines[i][5:] + "\nlink:" + content_lines[i + 1][5:] + "\n")

    page += 1
