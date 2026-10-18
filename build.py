#!/usr/bin/env python3
"""Rebuild the asset pack, the page's web images and the zip from the game repo's marketing/steam/.

    python3 build.py [--src ~/Desktop/desktop_rpg/marketing/steam]

Only game screenshots, renders, GIFs, capsules and the logo go in: the Beowulf licence allows them in this
game's digital advertising (3.1). Never add raw sprite sheets or effect strips from the packs.
"""

from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

from PIL import Image

DIR = Path(__file__).resolve().parent
PACK = DIR / "PressKit_MilosDayShift"
WEB = DIR / "assets" / "img"

# (source relative to marketing/steam, destination relative to the pack)
FILES = [
    ("logo/final/library_logo_1280w.png", "01_Logo_and_Icons/Logo_1280w.png"),
    ("logo/final/logo_12x.png", "01_Logo_and_Icons/Logo_pixel_12x.png"),
    ("logo/final/logo_4x.png", "01_Logo_and_Icons/Logo_pixel_4x.png"),
    ("logo/final/logo_1x.png", "01_Logo_and_Icons/Logo_pixel_1x.png"),
    ("community/client_icon_256x256.png", "01_Logo_and_Icons/Icon_256.png"),
    ("community/community_icon_184x184.png", "01_Logo_and_Icons/Icon_184.png"),
    ("screenshots/screenshot_1_cheer_desktop.png", "02_Screenshots/01_Desktop_Cheer.png"),
    ("screenshots/screenshot_2_camp.png", "02_Screenshots/02_Camp.png"),
    ("screenshots/screenshot_3_guardian_desktop.png", "02_Screenshots/03_Desktop_Guardian.png"),
    ("screenshots/screenshot_4_town_menu_desktop.png", "02_Screenshots/04_Desktop_Town.png"),
    ("screenshots/screenshot_5_deep_desktop.png", "02_Screenshots/05_Desktop_Deep_Floors.png"),
    ("screenshots/screenshot_6_boss.png", "02_Screenshots/06_Boss.png"),
    ("screenshots/screenshot_7_mimic.png", "02_Screenshots/07_Mimic.png"),
    ("screenshots/screenshot_8_small_window_desktop.png", "02_Screenshots/08_Desktop_Small_Window.png"),
    ("store/main_capsule_1232x706.png", "03_Key_Art_and_Capsules/Capsule_Main_1232x706.png"),
    ("store/header_capsule_920x430.png", "03_Key_Art_and_Capsules/Capsule_Header_920x430.png"),
    ("store/vertical_capsule_748x896.png", "03_Key_Art_and_Capsules/Capsule_Vertical_748x896.png"),
    ("library/library_capsule_600x900.png", "03_Key_Art_and_Capsules/Capsule_Portrait_600x900.png"),
    ("store/small_capsule_462x174.png", "03_Key_Art_and_Capsules/Capsule_Small_462x174.png"),
    ("library/library_hero_3840x1240.png", "03_Key_Art_and_Capsules/Key_Art_No_Logo_3840x1240.png"),
    ("gifs/gif_1_clock_in_WIDE_DRAFT.gif", "04_GIFs/01_Clock_In.gif"),
    ("gifs/gif_2_cheer_DRAFT.gif", "04_GIFs/02_Cheer.gif"),
    ("gifs/gif_3_forge_DRAFT.gif", "04_GIFs/03_Forge.gif"),
    ("gifs/gif_4_boss_DRAFT.gif", "04_GIFs/04_Boss.gif"),
    ("renders/hero_camp_2304.png", "05_Transparent_Renders/Camp_Wide.png"),
    ("renders/shot_camp.png", "05_Transparent_Renders/Camp.png"),
    ("renders/shot_fight_cheer.png", "05_Transparent_Renders/Fight_Cheer.png"),
    ("renders/shot_fight_deep.png", "05_Transparent_Renders/Fight_Deep.png"),
    ("renders/shot_guardian.png", "05_Transparent_Renders/Guardian.png"),
    ("renders/shot_boss.png", "05_Transparent_Renders/Boss.png"),
    ("renders/shot_mimic.png", "05_Transparent_Renders/Mimic.png"),
]

# Web copies: (pack path, web name, max width). Screenshots become JPEGs; PNGs keep transparency.
WEB_IMAGES = [
    ("03_Key_Art_and_Capsules/Key_Art_No_Logo_3840x1240.png", "hero.jpg", 2400),
    ("01_Logo_and_Icons/Logo_1280w.png", "logo.png", 1280),
    ("01_Logo_and_Icons/Icon_184.png", "favicon.png", 64),
    ("03_Key_Art_and_Capsules/Capsule_Main_1232x706.png", "capsule.jpg", 1232),
    ("03_Key_Art_and_Capsules/Capsule_Header_920x430.png", "header.jpg", 920),
    ("03_Key_Art_and_Capsules/Capsule_Portrait_600x900.png", "portrait.jpg", 600),
    ("05_Transparent_Renders/Camp.png", "render_camp.png", 900),
    ("05_Transparent_Renders/Boss.png", "render_boss.png", 900),
] + [(f"02_Screenshots/{p.split('/')[-1]}", p.split("/")[-1].replace(".png", ".jpg"), 1280)
     for _, p in FILES if p.startswith("02_Screenshots/")]


def web_copy(src: Path, dst: Path, width: int) -> None:
    im = Image.open(src)
    if im.width > width:
        resample = Image.NEAREST if src.stat().st_size < 20_000 else Image.LANCZOS  # keep tiny pixel art crisp
        im = im.resize((width, round(im.height * width / im.width)), resample)
    if dst.suffix == ".jpg":
        im.convert("RGB").save(dst, quality=86, optimize=True, progressive=True)
    else:
        im.save(dst, optimize=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=Path.home() / "Desktop/desktop_rpg/marketing/steam")
    args = ap.parse_args()

    shutil.rmtree(PACK, ignore_errors=True)
    for src, dst in FILES:
        out = PACK / dst
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(args.src / src, out)
    shutil.copy2(DIR / "Factsheet.txt", PACK / "Factsheet.txt")

    shutil.rmtree(WEB, ignore_errors=True)
    WEB.mkdir(parents=True)
    for src, name, width in WEB_IMAGES:
        web_copy(PACK / src, WEB / name, width)

    # The desktop: the screenshots' sky wallpaper (public domain) and Fluent Emoji 3D icons (MIT, notice kept).
    sky = Image.open(args.src / "wallpaper/sky_rawpixel_3259446.jpg")
    sky.resize((2400, round(sky.height * 2400 / sky.width)), Image.LANCZOS).save(
        WEB / "sky.jpg", quality=78, optimize=True, progressive=True)
    icons = DIR / "assets" / "icons"
    shutil.rmtree(icons, ignore_errors=True)
    icons.mkdir(parents=True)
    for name in ("folder", "document", "notes", "spreadsheet", "trash"):
        Image.open(args.src / f"icons/fluent/{name}.png").convert("RGBA").resize((96, 96), Image.LANCZOS).save(
            icons / f"{name}.png", optimize=True)
    shutil.copy2(args.src / "icons/fluent/LICENSE", icons / "LICENSE-fluent-emoji.txt")
    Image.open(args.src / "community/client_icon_256x256.png").resize((96, 96), Image.NEAREST).save(icons / "milo.png")

    zpath = DIR / "PressKit_MilosDayShift.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(PACK.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, f.relative_to(DIR))
    print(f"{len(FILES)} files -> {PACK.name}/, {len(WEB_IMAGES)} web images, "
          f"zip {zpath.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
