# Milo's Day Shift Press Kit

Public press kit for **Milo's Day Shift** by Fleur Labs, hosted on GitHub Pages.

**Live site:** https://fleurlabs.github.io/milos-day-shift-press-kit/
**Steam:** https://store.steampowered.com/app/5443940/
**Press contact:** milosdayshift@gmail.com

| Path | Purpose |
|------|---------|
| `index.html` / `styles.css` | The press kit page, styled as a desktop: an "About the game" document (pitch and features), a time card (factsheet), and explorer windows for GIFs, screenshots and art |
| `Factsheet.txt` | Plain-text factsheet (also copied into the pack) |
| `PressKit_MilosDayShift/` | The asset pack: logo and icons, screenshots, capsules and key art, GIFs, transparent renders |
| `PressKit_MilosDayShift.zip` | The same pack as one download |
| `assets/img/` | Smaller copies used by the page, plus the sky wallpaper (rawpixel 3259446, public domain) |
| `assets/icons/` | Desktop icons: Microsoft Fluent Emoji 3D (MIT, notice in `LICENSE-fluent-emoji.txt`) and the game's app icon |
| `build.py` | Rebuilds the pack, the web copies and the zip from the game's `marketing/steam/` art |

## Updating

Edit `Factsheet.txt` and `index.html` for copy, then `python3 build.py` after any art change (needs Pillow) and commit.

## To do

- [ ] Trailer (embed it under the pitch and add it to the factsheet)
- [ ] Price (release planned for March 2027)
- [ ] Replace the draft GIFs when the final ones are cut
- [ ] Socials, if any
