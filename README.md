# ublock-lists

This is a collection of public uBlock Origin filter lists and some custom ones I wrote for YouTube. Plus, GitHub automation scripts to keep everything up to date. This repository is mostly for people who want to replicate my uBO setup or pick pieces from it.

> **⚠️ Warning:** `personal.txt` is mainly for my personal use and is intentionally aggressive. If you just want a couple of lists, use the individual lists instead of the master list. Don't import the master list unless you're replicating my full browser setup or know what you're doing.

## What's in here

### Core files

- [`import-urls.txt`](./import-urls.txt): This is the list of upstream filter list URLs. You can use those links to subscribe to individual lists in uBlock Origin of course. Comments are ignored by the scripts.
- [`personal.txt`](./personal.txt): This is the auto-compiled master list generated from `import-urls.txt` and includes all upstream lists.

### My lists

The [`YouTube/`](./YouTube) directory has two custom lists I wrote for YouTube:

- [`YouTube/anti-adblock-bypass.txt`](./YouTube/anti-adblock-bypass.txt): Bypass YouTube's anti-adblock.
- [`YouTube/cleaner-ui.txt`](./YouTube/cleaner-ui.txt): UI decluttering filters.

### Mirrors

The [`mirror/`](./mirror) directory keeps snapshots of all upstream lists, organised as `mirror/<author>/<repo>/<filename>`, just in case an upstream source goes down or audits are needed.

### Automation scripts

- [`scripts/compile.py`](./scripts/compile.py): Compiles personal.txt from import-urls.txt.
- [`scripts/mirror.py`](./scripts/mirror.py): Mirrors all upstream lists into mirror directory.

Both are standard Python scripts. GitHub Actions runs both weekly on Mondays (mirrors at 02:00 UTC, compile at 03:00 UTC) and on every push.

## How to use

If you want my YouTube lists, copy these URLs into uBO:

[https://raw.githubusercontent.com/jartf/ublock-lists/main/YouTube/anti-adblock-bypass.txt](./YouTube/anti-adblock-bypass.txt)
[https://raw.githubusercontent.com/jartf/ublock-lists/main/YouTube/cleaner-ui.txt](./YouTube/cleaner-ui.txt)

If you want to import the upstream lists directly, copy all text from [import-urls.txt](./import-urls.txt) into uBO’s Import section (comments will be ignored there).

If you want to get the compiled master list directly:

[https://raw.githubusercontent.com/jartf/ublock-lists/main/personal.txt](./personal.txt)

## Upstream sources

This list pulls from these community lists:

<details open>
<summary><strong>My own lists</strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| YouTube anti adblock bypass list | [https://raw.githubusercontent.com/jartf/ublock-lists/main/YouTube/anti-adblock-bypass.txt](./YouTube/anti-adblock-bypass.txt) | Bypasses YouTube's anti-adblock |
| YouTube cleaner UI | [https://raw.githubusercontent.com/jartf/ublock-lists/main/YouTube/cleaner-ui.txt](./YouTube/cleaner-ui.txt) | Declutters YouTube's interface |
</details>

<details open>
<summary><strong><a href="https://github.com/AdGuardTeam/AdGuardFilters">AdGuard</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| AdGuard URL Tracking Filter | [https://filters.adtidy.org/extension/ublock/filters/17.txt](https://filters.adtidy.org/extension/ublock/filters/17.txt) | Removes tracking filters at the end of URLs |
</details>

<details open>
<summary><strong><a href="https://celenity.dev/">celenity</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| BadBlock - Click Tracking/Referral Domains (ABP) | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/click-tracking.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/click-tracking.txt) | Blocks click tracking domains |
| BadBlock - Crap (ABP) | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/crap.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/crap.txt) | General "crap" filters |
| BadBlock - Fonts (ABP) | [https://badblock.celenity.dev/abp/fonts.txt](https://badblock.celenity.dev/abp/fonts.txt) | Blocks third-party fonts |
| BadBlock+ (ABP) | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/badblock%5Fplus.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/badblock%5Fplus.txt) | Expanded BadBlock list |
| Beacon API Stub | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/base/overrides/hardened/block-beacon%5Foverrides.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/base/overrides/hardened/block-beacon%5Foverrides.txt) | Overrides Beacon API |
| Block Page Visibility | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-page-visibility.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-page-visibility.txt) | Blocks Page Visibility API |
| Block WebGL | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webgl.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webgl.txt) | Blocks WebGL |
| Block WebGL - Unbreak | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webgl.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webgl.txt) | Unbreak rules for WebGL blocking |
| Block WebGPU | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webgpu.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webgpu.txt) | Blocks WebGPU |
| Block WebGPU - Unbreak | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webgpu.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webgpu.txt) | Unbreak rules for WebGPU blocking |
| Block WebRTC | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webrtc.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/block-webrtc.txt) | Blocks WebRTC |
| Block WebRTC - Unbreak | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webrtc.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/hardened/unbreak-webrtc.txt) | Unbreak rules for WebRTC blocking |
| NSA Blocklist - Next Generation (ABP) | [https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/nsa-blocklist-ng.txt](https://gitlab.com/celenityy/BadBlock/-/raw/pages/abp/nsa-blocklist-ng.txt) | Blocks Big Brother and some government domains |
| Personal Blocklist (ABP) | [https://badblock.celenity.dev/abp/personal.txt](https://badblock.celenity.dev/abp/personal.txt) | celenity's personal blocklist (thanks :3 ) |
| Phoenix filters | [https://assets.celenity.dev/ublock/phoenix/filters.txt](https://assets.celenity.dev/ublock/phoenix/filters.txt) | Phoenix's built-in filters |
| Phoenix filters - Quick fixes | [https://assets.celenity.dev/ublock/phoenix/quick-fixes.txt](https://assets.celenity.dev/ublock/phoenix/quick-fixes.txt) | Phoenix's quick fixes list |
</details>

<details open>
<summary><strong><a href="https://github.com/DandelionSprout">DandelionSprout</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| (Partially) Anti-PRChina List | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Ant%D1%96%D0%A0R%D0%A1L%D1%96st.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Ant%D1%96%D0%A0R%D0%A1L%D1%96st.txt) | Blocks questionable websites hosted in China |
| Actually Legitimate URL Shortener Tool | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt) | URL shortener allowlist |
| Anti-'Insane religious preachers' List | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiPreacherList.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiPreacherList.txt) | Blocks websites with religious preaching |
| Anti-«Glorification of babies» List | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiGlorificationOfBabiesList.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiGlorificationOfBabiesList.txt) | Blocks websites that "glorify babies" |
| Anti-Astrology List | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiAstrologyList.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiAstrologyList.txt) | Blocks astrology related content |
| Browse websites without logging in | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/BrowseWebsitesWithoutLoggingIn.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/BrowseWebsitesWithoutLoggingIn.txt) | Removes login gates |
| Dandelion Sprout's Anti-Malware List | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout%27s%20Anti-Malware%20List.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout%27s%20Anti-Malware%20List.txt) | Anti-malware list |
| IDN Homograph Attack Protection - Complete Blockage | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Special%20security%20lists/IDNHomographProtectionTotal.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Special%20security%20lists/IDNHomographProtectionTotal.txt) | Protects against [IDN homograph attacks](https://en.wikipedia.org/wiki/IDN_homograph_attack) |
| Remover for Far-Right Tabloid, Alt-Right, Ultranationalist, and Anti-Vaxx Sites | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/TabloidRemover.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/TabloidRemover.txt) | Blocks and removes tabloid/alt-right/anti-vaccine sites |
| Twitter and Mastodon De-Politificator | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/Twitter%20De-Politificator.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/Twitter%20De-Politificator.txt) | Removes political content from Twitter and Mastodon |
| YouTube: Even More Pure Video Experience | [https://raw.githubusercontent.com/DandelionSprout/adfilt/master/YouTubeEvenMorePureVideoExperience.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/YouTubeEvenMorePureVideoExperience.txt) | YouTube UI cleanup |
</details>

<details open>
<summary><strong><a href="https://divested.dev/">Divested</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| Fingerprinting Protection | [https://divested.dev/blocklists/Fingerprinting.ubl](https://divested.dev/blocklists/Fingerprinting.ubl) | Fingerprinting protection list |
</details>

<details open>
<summary><strong><a href="https://fmhy.net/">FMHY</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| FMHY Unsafe sites filterlist - Basic | [https://raw.githubusercontent.com/fmhy/FMHYFilterlist/main/filterlist-basic.txt](https://raw.githubusercontent.com/fmhy/FMHYFilterlist/main/filterlist-basic.txt) | Blocks unsafe sites |
</details>

<details open>
<summary><strong><a href="https://gitlab.com/hagezi">HaGeZi</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| HaGeZi's DynDNS Blocklist | [https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/dyndns.txt](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/dyndns.txt) | Blocks dynamic DNS domains |
| HaGeZi's The World's Most Abused TLDs | [https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-ublock.txt](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-ublock.txt) | Blocks abused/spam top-level domains |
| HaGeZi's Threat Intelligence Feeds DNS Blocklist - mini version | [https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/tif.mini.txt](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/tif.mini.txt) | Mini threat intelligence feed |
| HaGeZi's Ultimate mini DNS/Browser Blocklist | [https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/ultimate.mini.txt](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/ultimate.mini.txt) | Aggressive DNS/browser blocklist |
</details>

<details open>
<summary><strong><a href="https://gitflic.ru/user/magnolia1234">magnolia1234</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| Bypass Paywalls Clean filter | [https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters/blob/raw?file=bpc-paywall-filter.txt](https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters/blob/raw?file=bpc-paywall-filter.txt) | Bypass paywalls |
</details>

<details open>
<summary><strong><a href="https://github.com/yokoffing">yokoffing</a></strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| Block third party fonts | [https://raw.githubusercontent.com/yokoffing/filterlists/main/block%5Fthird%5Fparty%5Ffonts.txt](https://raw.githubusercontent.com/yokoffing/filterlists/main/block%5Fthird%5Fparty%5Ffonts.txt) | Block third-party fonts |
| Privacy Essentials | [https://raw.githubusercontent.com/yokoffing/filterlists/main/privacy%5Fessentials.txt](https://raw.githubusercontent.com/yokoffing/filterlists/main/privacy%5Fessentials.txt) | Privacy essentials list |
| yokoffing's Annoyance List | [https://raw.githubusercontent.com/yokoffing/filterlists/main/annoyance%5Flist.txt](https://raw.githubusercontent.com/yokoffing/filterlists/main/annoyance%5Flist.txt) | Annoyance filters list |
| yokoffing's click2load filters | [https://raw.githubusercontent.com/yokoffing/filterlists/main/click2load.txt](https://raw.githubusercontent.com/yokoffing/filterlists/main/click2load.txt) | Forces media elements to load only on click |
</details>

<details open>
<summary><strong>Others</strong></summary>

| Name | URL | Purpose |
| --- | --- | --- |
| Anti-paywall filters | [https://raw.githubusercontent.com/liamengland1/miscfilters/master/antipaywall.txt](https://raw.githubusercontent.com/liamengland1/miscfilters/master/antipaywall.txt) | Remove paywalls |
| Hide YouTube Shorts | [https://raw.githubusercontent.com/gijsdev/ublock-hide-yt-shorts/master/list.txt](https://raw.githubusercontent.com/gijsdev/ublock-hide-yt-shorts/master/list.txt) | Hide shorts on YouTube |
| Huge AI Blocklist | [https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list.txt](https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list.txt) | Blocks sites with mainly AI-generated content |
| YouTube Neuter | [https://raw.githubusercontent.com/mchangrh/yt-neuter/main/yt-neuter.txt](https://raw.githubusercontent.com/mchangrh/yt-neuter/main/yt-neuter.txt) | YouTube decluttering |
</details>

## Local development

If you somehow want to run the automation scripts locally, you can do so with Python 3. Just make sure to have the `requests` library installed (`pip install requests`). Then you can run:

```bash
python3 scripts/compile.py   # rebuilds personal.txt
python3 scripts/mirror.py    # refreshes mirror/
```

## License

MIT. See [LICENSE](LICENSE).
