import os


def save_signature(name, link, author):
    with open(f"_data/signed/{author}.yaml", "w") as f:
        f.write(f"name: {name.strip()}\nlink: {link.strip()}\n")


# Apparently most people can't follow a two-line template, e.g. miss 'name:' or
# 'link:' or use 'site:' instead of 'link:' or use 'mailto:' instead of
# 'link: mailto:', etc., so we have to guess in what way their interpretation is
# wrong, and try to make the format at least somewhat correct.
def import_signature_from_lines(name, link, author):
    if name.lower().startswith("name:"):
        name = name[5:]

    if link.lower().startswith("link:"):
        link = link[5:]
    elif link.lower().startswith("site:"):
        link = link[5:]
    elif link.lower().startswith("mail:"):
        link = "mailto:" + link[5:].strip()
    elif link.lower().startswith("email:"):
        link = "mailto:" + link[6:].strip()
    elif link.lower().startswith("mailto:"):
        link = "mailto:" + link[7:].strip()

    # Demangle email
    if "@" in link or "(at)" in link or "[at]" in link:
        link = link.replace("[at]", "@")
        link = link.replace("(at)", "@")
        link = link.replace(" at ", "@")
        link = link.replace("[dot]", ".")
        link = link.replace("(dot)", ".")
        link = link.replace(" dot ", ".")
        link = link.replace(" ", "")

    # Add protocol to links without it
    if "://" not in link:
        if "@" in link:
            if not link.startswith("mailto:"):
                link = f"mailto:{link}"
        elif link.startswith("www.") or link.endswith(".com"):
            link = f"https://{link}"

    if "/" in link or "@" in link:
        save_signature(name, link, author)


def parse_and_import_signature(content, author):
    if os.path.isfile(f"_data/signed/{author}.yaml"):
        return

    content_lines = [line.strip() for line in content.replace("`", "").strip().split("\n") if line.strip()]
    imported = False
    for i in range(len(content_lines) - 1):
        if content_lines[i].lower().startswith("name:") and content_lines[i + 1].lower().startswith("link:"):
            import_signature_from_lines(content_lines[i], content_lines[i + 1], author)
            imported = True
    if not imported and len(content_lines) == 2:
        import_signature_from_lines(*content_lines, author)
