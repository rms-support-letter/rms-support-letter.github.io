import os
from collections import defaultdict


file_name_by_link = defaultdict(list)

for file_name in sorted(os.listdir("_data/signed")):
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read().replace("\r", "")
    link = next(line for line in contents.split("\n") if line.startswith("link:"))[5:].strip()
    if link == "/#":
        continue
    file_name_by_link[link].append(file_name)

for link, file_names in file_name_by_link.items():
    if len(file_names) == 1:
        continue
    print(link, "duplicates:", file_names)
