import os
from collections import defaultdict


file_name_by_name = defaultdict(list)
file_name_by_link = defaultdict(list)

for file_name in sorted(os.listdir("_data/signed")):
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read().replace("\r", "")
    name = next(line for line in contents.split("\n") if line.startswith("name:"))[5:].strip()
    link = next(line for line in contents.split("\n") if line.startswith("link:"))[5:].strip()
    if name[0] == name[0].lower() or " " in name: # looks like a nickname or a full name
        file_name_by_name[name].append(file_name)
    if link != "/#":
        file_name_by_link[link].append(file_name)

for name, file_names in file_name_by_name.items():
    if len(file_names) == 1:
        continue
    print(name, "duplicates:", file_names)

for link, file_names in file_name_by_link.items():
    if len(file_names) == 1:
        continue
    print(link, "duplicates:", file_names)
