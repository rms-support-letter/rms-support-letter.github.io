import os
import re


regex = re.compile(r"name: (\S+\s)*\S+\nlink: (/#|(https?://|mailto:)[a-zA-Z0-9_().@:%\+~#?&//=-]+)\n{,2}")

ok = True
for file_name in sorted(os.listdir("_data/signed")):
    if not file_name.endswith(".yaml") or file_name[:-5] != file_name[:-5].strip():
        print(file_name, "probably has an invalid name.\nYou may (1) wait for review (2) use a real name instead (3) add .yaml as file extension (4) remove extra whitespaces from the file name")
        ok = False
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read()
    if not re.fullmatch(regex, contents):
        print(file_name, "has invalid format.\nPlease reformat as: \nname: <your name here> (optional organization or company name) \nlink: <link to your profile or site>")
        ok = False

if not ok:
    raise SystemExit(1)
