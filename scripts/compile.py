import urllib.request
import re
from datetime import datetime, timezone

MASTER = "import-urls.txt"
OUTPUT = "personal.txt"

urls = []
with open(MASTER, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("!") or line.startswith("#"):
            continue
        urls.append(line)

header = f"""! Title: Jarema's master uBO filter list
! Description: Auto-compiled from all sources. Do not edit manually. This list imports all my external and personal filters that I use. You probably shouldn't use this unless you want to replicate my browser.
! Homepage: https://github.com/jartf/ublock-lists
! Last modified: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
! License: MIT
!
! Sources:
"""

for url in urls:
    header += f"!   {url}\n"

header += "\n"

lines = []
for line in urls:
    print(f"Fetching: {line}")
    try:
        req = urllib.request.Request(line, headers={"User-Agent": "uBlock Origin"})
        with urllib.request.urlopen(req, timeout=15) as r:
            content = r.read().decode("utf-8", errors="replace")
        lines.append(f"! --- Source: {line} ---\n{content}\n")
    except Exception as e:
        print(f"  Failed: {e}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(header)
    f.write("\n".join(lines))

print(f"Done, written changes to {OUTPUT}")
