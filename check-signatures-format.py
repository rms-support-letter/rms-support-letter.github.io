import os
import re


regex = re.compile(r"name: (\S+\s)*\S+\nlink: (/#|(https?://|mailto:)[a-zA-Z0-9_().@:%\+~#?&//=-]+)\n{,2}")

ok = True
for file_name in sorted(os.listdir("_data/signed")):
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read()
    if not re.fullmatch(regex, contents):
        print(file_name, "has invalid format")
        ok = False

if not ok:
    raise SystemExit(1)
