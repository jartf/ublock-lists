import urllib.request
import os
from urllib.parse import urlparse, parse_qs

MASTER = "import-urls.txt"
MIRROR_DIR = "mirror"

AUTHOR_ALIASES = {
    "celenityy": "celenity",
}

def get_author_repo_filename(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    path_parts = [p for p in parsed.path.split("/") if p]

    if hostname == "raw.githubusercontent.com":
        return path_parts[0].lower(), path_parts[1].lower(), path_parts[-1]

    if hostname == "gitlab.com":
        return path_parts[0].lower(), path_parts[1].lower(), path_parts[-1]

    if hostname == "gitflic.ru":
        author = path_parts[1].lower() if len(path_parts) > 1 else hostname
        repo = path_parts[2].lower() if len(path_parts) > 2 else "misc"
        qs = parse_qs(parsed.query)
        filename = qs.get("file", [path_parts[-1]])[0]
        return author, repo, filename

    domain_parts = hostname.split(".")
    author = domain_parts[-2].lower() if len(domain_parts) >= 2 else domain_parts[0].lower()
    repo = path_parts[0].lower() if path_parts else "misc"
    filename = path_parts[-1] if len(path_parts) > 1 else repo
    return author, repo, filename

def mirror():
    urls = []
    with open(MASTER, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("!") or line.startswith("#"):
                continue
            urls.append(line)

    for url in urls:
        if "jartf" in url:
            print(f"Skipping own list: {url}")
            continue

        author, repo, filename = get_author_repo_filename(url)
        author = AUTHOR_ALIASES.get(author, author)
        out_dir = os.path.join(MIRROR_DIR, author, repo)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, filename)

        print(f"Mirroring: {url}\n  → {out_path}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "uBlock Origin"})
            with urllib.request.urlopen(req, timeout=15) as r:
                content = r.read().decode("utf-8", errors="replace")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Mirrored: ({len(content):,} bytes)")
        except Exception as e:
            print(f"  Failed: {e}")

    print("Mirror complete.")

if __name__ == "__main__":
    mirror()
