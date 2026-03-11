#!/usr/bin/env python3
"""
Download moodboard assets for single grid:
- Pamposh: 01, 04 + 2 Kashmiri lotus (Wikimedia). Removed 02, 03, 05.
- Yemberzal: 01, 04, 05 + 2 natural (Unsplash). Removed 02, 03.
- Kong Posh: 01 = Wikipedia Crocus sativus; 02–05 Unsplash.
- Gulab: 01 and 03 = natural rose (Unsplash); 02, 04, 05 unchanged.
- Gul-e-Lala: 01–05 unchanged.
- Handicrafts + Brand unchanged.
"""

import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Install requests: pip install requests")
    sys.exit(1)

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
UNSPLASH_DOWNLOAD = "https://unsplash.com/photos/{id}/download?force=true&w=2400"

# Pamposh: keep 01, 04; add 2 Kashmiri lotus (Wikimedia)
PAMPOSH = [
    ("01kdXGe5jaQ", "floral/pamposh_01.jpg"),
    ("8o7rGsKl1WM", "floral/pamposh_04.jpg"),
    (
        "https://upload.wikimedia.org/wikipedia/commons/c/c7/Indian_Lotus_%28Nelumbo_nucifera%29.jpg",
        "floral/pamposh_kashmir_01.jpg",
    ),
    ("RbDRZIOJ2gY", "floral/pamposh_kashmir_02.jpg"),  # Pink lotus on lily pad (natural)
]

# Yemberzal: 01, 04, 05 + 2 natural
YEMBERZAL = [
    ("6dwahjrGbNw", "floral/yemberzal_01.jpg"),
    ("WMi_7XsOT64", "floral/yemberzal_04.jpg"),
    ("n13s6zcvk6Y", "floral/yemberzal_05.jpg"),
    ("0gLJJLhkYQI", "floral/yemberzal_natural_01.jpg"),  # Field of daffodils
    ("pwERKEUYiUQ", "floral/yemberzal_natural_02.jpg"),   # Yellow daffodils grassy field
]

# Kong Posh: 01 = Wikimedia Crocus sativus; 02–05 Unsplash
KONG_POSH = [
    (
        "https://upload.wikimedia.org/wikipedia/commons/6/61/Crocus_sativus_002.JPG",
        "floral/kongposh_01.jpg",
    ),
    ("2Qu_IdJdk80", "floral/kongposh_02.jpg"),
    ("yruq0e9bhgE", "floral/kongposh_03.jpg"),
    ("FOrQEwlf22M", "floral/kongposh_04.jpg"),
    ("a2h9qgTmpGA", "floral/kongposh_05.jpg"),
]

# Gulab: 01 and 03 = natural rose; 02, 04, 05 studio
GULAB = [
    ("Q3dKRgt-6WM", "floral/gulab_01.jpg"),   # Bush of red roses natural
    ("v9FQqKROXXE", "floral/gulab_02.jpg"),
    ("PxKrH8ZfVpQ", "floral/gulab_03.jpg"),   # Red roses with green leaves natural
    ("Wtze-gjJ7-Q", "floral/gulab_04.jpg"),
    ("42GQdgyuNpA", "floral/gulab_05.jpg"),
]

# Gul-e-Lala: unchanged
GUL_E_LALA = [
    ("eEU75_b55uw", "floral/gulelala_01.jpg"),
    ("xizg70oqmmw", "floral/gulelala_02.jpg"),
    ("1Q1xsR2bHPw", "floral/gulelala_03.jpg"),
    ("j94dSufPqGI", "floral/gulelala_04.jpg"),
    ("jWZr3Tt0UU4", "floral/gulelala_05.jpg"),
]

HANDICRAFT_ASSETS = [
    (
        "https://upload.wikimedia.org/wikipedia/commons/c/c7/Embroidery_on_a_wollen_shawl_from_Kashmir_01.jpg",
        "handicrafts/01_sozni_embroidery_kashmir_shawl.jpg",
    ),
    (
        "https://upload.wikimedia.org/wikipedia/commons/2/2f/Shawl_MET_ISL35.jpg",
        "handicrafts/02_kashmir_shawl_met.jpg",
    ),
]


def download_file(url: str, dest: Path, session: requests.Session) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    headers = {
        "User-Agent": "MoodboardAssetDownloader/1.0 (educational moodboard)",
        "Accept": "image/*,*/*",
    }
    try:
        r = session.get(url, headers=headers, timeout=30, allow_redirects=True)
        r.raise_for_status()
        content = r.content
        if len(content) < 500:
            print(f"  [skip] too small ({len(content)} bytes)")
            return False
        ct = r.headers.get("Content-Type", "")
        ext = ".jpg"
        if "png" in ct or url.lower().endswith(".png"):
            ext = ".png"
        elif "webp" in ct:
            ext = ".webp"
        if not str(dest).endswith(ext):
            dest = dest.with_suffix(ext)
        dest.write_bytes(content)
        print(f"  -> {dest} ({len(content) // 1024} KB)")
        return True
    except Exception as e:
        print(f"  [fail] {e}")
        return False


def main():
    session = requests.Session()
    ok = 0
    fail = 0

    sets = [
        ("Pamposh", PAMPOSH),
        ("Yemberzal", YEMBERZAL),
        ("Kong Posh", KONG_POSH),
        ("Gulab", GULAB),
        ("Gul-e-Lala", GUL_E_LALA),
    ]

    for name, items in sets:
        print(f"\nDownloading {name}...")
        for item in items:
            if len(item) == 2 and not item[0].startswith("http"):
                photo_id, rel_path = item
                url = UNSPLASH_DOWNLOAD.format(id=photo_id)
            else:
                url, rel_path = item
            dest = ASSETS_DIR / rel_path
            print(f"  {dest.name}")
            if download_file(url, dest, session):
                ok += 1
            else:
                fail += 1

    print("\nDownloading handicrafts...")
    for url, rel_path in HANDICRAFT_ASSETS:
        dest = ASSETS_DIR / rel_path
        print(f"  {dest.name}")
        if download_file(url, dest, session):
            ok += 1
        else:
            fail += 1

    print(f"\nDone: {ok} downloaded, {fail} failed.")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
