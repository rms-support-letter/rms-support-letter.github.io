import subprocess
import os


parts = subprocess.run(["gh", "issue", "view", "837", "-c"], capture_output=True).stdout.split(b"\n--\n")

for info, content in zip(parts[::2], parts[1::2]):
    info_dict = {}
    for line in info.decode().split("\n"):
        key, value = line.split(":\t")
        info_dict[key] = value

    author = info_dict["author"]

    content_lines = [line.strip() for line in content.decode().replace("`", "").strip().split("\n") if line.strip()]
    imported = False
    for i in range(len(content_lines) - 1):
        if content_lines[i].lower().startswith("name:") and content_lines[i + 1].lower().startswith("link:"):
            if not os.path.isfile(f"_data/signed/{author}.yaml"):
                with open(f"_data/signed/{author}.yaml", "w") as f:
                    f.write("name:" + content_lines[i][5:] + "\nlink:" + content_lines[i + 1][5:] + "\n")
            imported = True
    if not imported and len(content_lines) == 2:
        name, link = content_lines
        if name.lower().startswith("name:"):
            name = name[5:]
        name = name.strip()
        if link.lower().startswith("link:"):
            link = link[5:]
        link = link.strip()
        if "/" in link or "@" in link:
            if not os.path.isfile(f"_data/signed/{author}.yaml"):
                with open(f"_data/signed/{author}.yaml", "w") as f:
                    f.write(f"name: {name}\nlink: {link}\n")

