import os
import re


regex = re.compile(r"name: (\S+\s)*\S+\nlink: (/#|(https?://|mailto:)[a-zA-Z0-9_().@:%\+~#?&//=-]+)\n{,2}")

ok = True
for file_name in sorted(os.listdir("_data/signed")):
    if not file_name.endswith(".yaml") or file_name[:-5] != file_name[:-5].strip():
        print(file_name, "probably has an invalid name. Please wait for review or use a real name instead or the file name may contains extra whitespaces.")
        ok = False
    with open(f"_data/signed/{file_name}") as f:
        contents = f.read()
    if not re.fullmatch(regex, contents):
        print(file_name, "has invalid format. Please reformat as: \n name: <your name here> (optional organization or company name) \nlink: <link to your profile or site>")
        ok = False

if not ok:
    raise SystemExit(1)
