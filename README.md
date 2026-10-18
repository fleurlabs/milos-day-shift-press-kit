# Milo's Day Shift Press Kit

Public press kit for **Milo's Day Shift** by Fleur Labs, hosted on GitHub Pages.

**Live site:** https://fleurlabs.github.io/milos-day-shift-press-kit/
**Steam:** https://store.steampowered.com/app/5443940/
**Press contact:** milosdayshift@gmail.com

| Path | Purpose |
|------|---------|
| `index.html` / `styles.css` | The press kit page (factsheet, pitch, GIFs, features, screenshots, key art, download) |
| `Factsheet.txt` | Plain-text factsheet (also copied into the pack) |
| `PressKit_MilosDayShift/` | The asset pack: logo and icons, screenshots, capsules and key art, GIFs, transparent renders |
| `PressKit_MilosDayShift.zip` | The same pack as one download |
| `assets/img/` | Smaller copies used by the page |
| `build.py` | Rebuilds the pack, the web copies and the zip from the game's `marketing/steam/` art |

## Updating

Edit `Factsheet.txt` and `index.html` for copy, then `python3 build.py` after any art change (needs Pillow) and commit.

## To do

- [ ] Trailer (embed it under the pitch and add it to the factsheet)
- [ ] Price and release date
- [ ] Replace the draft GIFs when the final ones are cut
- [ ] Socials, if any
