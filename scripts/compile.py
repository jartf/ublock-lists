import urllib.request
import re
from datetime import datetime, timezone

MASTER = "personal.txt"
OUTPUT = "compiled.txt"

header = f"""! Title: Jarema's personal master uBlock Origin filter list
! Description: Auto-compiled from all sources. Do not edit manually. This list imports all my external and personal filters that I use. You probably shouldn't use this unless you want to replicate my browser.
! Homepage: https://github.com/jartf/ublock-lists
! Last modified: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
! License: MIT

"""

lines = []
with open(MASTER, encoding="utf-8") as f:
    for line in f:
        m = re.match(r"^!#include\s+(https?://\S+)", line.strip())
        if not m:
            continue
        url = m.group(1)
        print(f"Fetching: {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "uBlock Origin"})
            with urllib.request.urlopen(req, timeout=15) as r:
                content = r.read().decode("utf-8", errors="replace")
            lines.append(f"! --- Source: {url} ---\n{content}\n")
        except Exception as e:
            print(f"  FAILED: {e}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(header)
    f.write("\n".join(lines))

print(f"Done. Written to {OUTPUT}")
