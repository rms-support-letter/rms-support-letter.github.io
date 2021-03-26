import os
import re


regex = re.compile(r"name: (\S+\s)*\S+\nlink: (/#|(https?://|mailto:)[a-zA-Z0-9_().@:%\+~#?&//=-]+)\n{,2}")

ok = True
for file_name in sorted(os.listdir("_data/signed")):
    if not file_name.endswith(".yaml") or file_name[:-5] != file_name[:-5].strip():
        print(file_name, "is probably a invalid name. Please wait for review or use a real name instead.")
        ok = False
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read()
    if not re.fullmatch(regex, contents):
        print(file_name, "has invalid format. Please check the format example on README and don't forget to add .yaml as file extension")
        ok = False

if not ok:
    raise SystemExit(1)
