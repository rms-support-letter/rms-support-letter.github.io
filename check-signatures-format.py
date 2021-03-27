import os
import re


ok = True

def report(arg):
    global ok
    ok = False
    print(arg)


for file_name in sorted(os.listdir("_data/signed")):
    if not file_name.endswith(".yaml"):
        report(f"{file_name} has invalid extension: expected .yaml.")

    if " " in file_name:
        report(f"{file_name} file name contains spaces. Please remove them.")

    if any(c.lower() not in "abcdefghijklmnopqrstuvwxyz0123456789_-. " for c in file_name):
        report(f"{file_name} file name contains special characters, which may render the file unusable for Windows users. Please remove these characters.")

    with open(f"_data/signed/{file_name}") as f:
        contents = f.read().replace("\r", "")

    if "\n\n" in contents.rstrip("\n") or contents.startswith("\n"):
        report(f"{file_name} contains empty lines. Please remove them.")

    if contents.endswith("\n\n\n"):
        report(f"{file_name} contains too many trailing empty lines. Please remove them.")

    existing_keys = set()
    for i, line in enumerate(contents.split("\n")):
        if not line:
            continue
        if line.strip() == "":
            report(f"{file_name} has an empty line {i + 1} with whitespace. Please remove this line.")
            continue
        if line != line.rstrip():
            report(f"{file_name} has excess whitespace at the end of line {i + 1}.")
        if line != line.lstrip():
            report(f"{file_name} has excess whitespace at the beginning of line {i + 1}.")
        line = line.strip()

        if ":" in line:
            key = line[:line.index(":")]
            value = line[line.index(":") + 1:]
            if key.strip() == "" or any(c.lower() not in "abcdefghijklmnopqrstuvwxyz" for c in key):
                key = None
                value = line
        else:
            key = None
            value = line

        if key is None:
            report(f"{file_name} has line {i + 1} which does not seem to specify a key, such as 'name:' or 'link:'. Please prepend the line with key or remove the line entirely.")
            continue

        if key != key.strip():
            report(f"{file_name} contains a space between the key '{key}' and the colon, please remove it.")
        key = key.strip()

        if key != key.lower():
            report(f"{file_name} contains a non-lowercase key {key} on line {i + 1}. Please convert it to lowercase.")
        key = key.lower()

        if not value.startswith(" "):
            report(f"A space is missing after '{key}:' in {file_name} on line {i + 1}. Please add it.")
        value = value[1:]
        if value != value.strip():
            report(f"{file_name} contains too many spaces after '{key}:' on line {i + 1}, please keep exactly one space.")
        value = value.strip()
        if value == "":
            report(f"{file_name} contains an empty '{key}:' on line {i + 1}, please fix this.")
            continue

        if key in existing_keys:
            report(f"{file_name} contains duplicate key '{key}'.")
        existing_keys.add(key.lower())

        if key == "name":
            if any(c.strip() == "" and c != " " for c in value):
                report(f"{file_name} contains an unexpected special whitespace character on line {i + 1}. Please replace it with a space.")
            if len(" ".join(value.split())) < len(value):
                report(f"{file_name} contains double space on line {i + 1}. Please keep a single space.")
        elif key == "link":
            if any(c.strip() == "" for c in value):
                report(f"{file_name} contains unexpected whitespace on line {i + 1}. Please remove whitespace from the link.")
            if value.startswith("mailto:"):
                if "@" not in value:
                    report(f"{file_name} uses mailto: on line {i + 1}, but the part that follows doesn't look like e-mail and does not contain '@' character. Please fix the address.")
            elif "://" in value:
                protocol = value.split("://")[0]
                if protocol not in ("http", "https"):
                    report(f"{file_name} uses a strange protocol '{protocol}' on line {i + 1}. Please use https:// or http://.")
            elif "@" in value and not value.startswith("mailto:"):
                report(f"{file_name} seems to use a e-mail in a link on line {i + 1}. Please add 'mailto:' before the e-mail.")
            elif value == "/#":
                pass
            else:
                report(f"{file_name} doesn't specify any link protocol on line {i + 1}. Please add https:// or http://.")
        else:
            report(f"{file_name} contains an unrecognized key {key} on line {i + 1}. Only 'name:' and 'link:' are supported.")

    if "name" not in existing_keys:
        report(f"{file_name} doesn't contain a name. Please specify your name or your alias.")
    if "link" not in existing_keys:
        report(f"{file_name} doesn't contain a link. Please specify a link to your online profile, e.g. on GitHub. If you really don't have a link, use /#")


if not ok:
    raise SystemExit(1)
