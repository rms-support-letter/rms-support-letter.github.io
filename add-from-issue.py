import subprocess
from _importer import parse_and_import_signature


parts = subprocess.run(["gh", "issue", "view", "837", "-c"], capture_output=True).stdout.split(b"\n--\n")

for info, content in zip(parts[::2], parts[1::2]):
    info_dict = {}
    for line in info.decode().split("\n"):
        key, value = line.split(":\t")
        info_dict[key] = value

    author = info_dict["author"]
    parse_and_import_signature(content.decode(), author)
