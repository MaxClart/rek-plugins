# ClearForge Plugins

Static shop site for Minecraft server plugins, hosted on GitHub Pages at https://maxclart.github.io/rek-plugins/

- Pages: `index.html`, `plugins/clearcrates.html`, `faq.html`, `terms.html`
- No trackers and no external CDNs. Relative links only. `.nojekyll` included.
- Edit `build.py` and run `python3 build.py` to regenerate the pages, then `python3 check_links.py` to check links and HTML.
- **Card checkout:** set `CARD_CHECKOUT_URL` in `js/main.js` to the Sell.app link and the button switches on by itself.

Not affiliated with Mojang or Microsoft.
