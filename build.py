# Generates the HTML pages with a shared header/footer. Run: python3 build.py
import html
BRAND="ClearForge Plugins"
ISSUES="https://github.com/MaxClart/Clearcrates/issues"
def page(path,title,desc,body):
    r="../" if "/" in path else ""
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Press+Start+2P&display=swap">
<link rel="stylesheet" href="{r}css/style.css?v=9">
<script src="{r}js/main.js" defer></script>
</head>
<body>
<header><nav><a class="brand" href="{r}index.html"><i class="cube" aria-hidden="true"></i>Clear<span>Forge</span></a><a href="{r}index.html#plugins">Plugins</a><a href="{r}packs.html">Packs</a><a href="{r}guides/index.html">Guides</a><a href="{r}faq.html">FAQ</a><a href="{r}terms.html">Terms</a><a href="https://clearforge.sell.app" target="_blank" rel="noopener">Full store</a></nav></header>
<main>
{body}
</main>
<footer><div class="wrap"><p>&copy; 2026 {BRAND}. Made for Minecraft server owners and admins.</p><p>ClearForge plugins are built with AI assistance and tested on a real Paper 1.21 server.</p><p>Not affiliated with Mojang or Microsoft.</p></div></footer>
</body>
</html>
'''
SELL="https://clearforge.sell.app"
NOTE='<p class="checkout-note">Checkout is Bitcoin only. No account needed: checkout as a guest.</p>'
HOW='<div class="howbox"><h3>How checkout works</h3><ol><li>Pay in Bitcoin on Sell.app.</li><li>Once the payment confirms on the network, the download is delivered instantly to your email.</li><li>Support: use Sell.app&#39;s contact-the-seller option on your order.</li><li>All sales are final: no refunds on digital files.</li></ol></div>'
def sell(name): return f"{SELL}/product/{name.lower()}"
def buy(r,name="ClearCrates",price="$9.99"):
    return f'''<section id="buy"><div class="wrap"><h2>Buy {name} &mdash; {price}</h2>
<div class="card"><h3>Instant download</h3><p>Pay with Bitcoin through Sell.app and your {name} download is delivered automatically as soon as the payment is confirmed.</p>
<p><a class="btn" href="{sell(name)}" target="_blank" rel="noopener">Buy now with Bitcoin, instant download</a></p>{NOTE}{HOW}</div>
<p class="muted">Checkout is handled by Sell.app. Your download link appears on the order page and is emailed to you.</p></div></section>'''
feat=["Spin animation (length and sound configurable, or turn it off)","Right-click a key to open, left-click to preview","In-game editor: drag items in, close to save","Item and command rewards, with a %player% placeholder","MiniMessage colours in names and messages","Full inventories: rewards drop at the player's feet, never lost","Tab completion on every command"]
cfg=html.escape(open("/workspace/products/clearcrates/src/main/resources/config.yml").read())
index=f'''<div class="hero"><div class="wrap"><h1>Plugins for Minecraft server owners</h1>
<p>Lightweight, honest Paper plugins built for people who run servers. Clear configs, no bloat, real support.</p>
<p><a class="btn" href="#plugins">Browse plugins</a> <a class="btn alt" href="guides/index.html">Setup guides</a> <a class="btn alt" href="faq.html">Server owner FAQ</a></p></div></div>
<section id="plugins"><div class="wrap"><h2>Plugin catalogue</h2>{NOTE}{HOW}<div class="grid">
<div class="card"><img src="assets/clearcrates-cover.png" alt="ClearCrates cover" width="1200" height="600">
<h3>ClearCrates</h3><p>Transparent crates for Paper 1.21: exact drop chances shown, fixed preview slots and lightweight animations. No required dependencies.</p>
<p class="price">$9.99</p><p><a class="btn" href="plugins/clearcrates.html">View plugin</a> <a class="btn alt" href="https://clearforge.sell.app/product/clearcrates" target="_blank" rel="noopener">Buy</a></p></div>
{{NEWCARDS}}</div></div></section>
{{PACKSEC_}}<section id="soon"><div class="wrap"><h2>Coming soon</h2><div class="grid">
<div class="card soon"><p>More server plugins are in the works.<br>Got a request? <a href="{ISSUES}">Tell us what your server needs</a>.</p></div>
<div class="card soon"><p>Next plugin under development&hellip;</p></div></div></div></section>'''
fl="".join(f"<li>{html.escape(f)}</li>" for f in feat)
cc=f'''<div class="hero"><div class="wrap"><h1>ClearCrates</h1><p>Crates your players can trust. Every reward shows its exact drop chance, items always sit where you put them, and openings won't lag your server.</p>
<p class="price">$9.99</p><p><a class="btn" href="#buy">Buy now</a> <a class="btn alt" href="../guides/clearcrates.html">Setup guide</a></p></div></div>
<section><div class="wrap"><img src="../assets/clearcrates-cover.png" alt="ClearCrates cover" width="1200" height="600">
<h2>Why ClearCrates</h2><ul><li><strong>Chances shown:</strong> the preview lists each reward's real percentage, worked out from your weights.</li>
<li><strong>Fixed slots:</strong> you choose every slot, nothing gets shuffled at random.</li>
<li><strong>Lightweight:</strong> one small scheduled task per opening, with no packet tricks.</li></ul>
<h2>Features</h2><ul>{fl}</ul>
<h2>Commands &amp; permissions</h2><div class="tablewrap"><table><tr><th>Command</th><th>Permission</th></tr>
<tr><td><code>/crate list</code>, <code>/crate preview &lt;crate&gt;</code></td><td><code>clearcrates.use</code> (everyone by default)</td></tr>
<tr><td><code>/crate give &lt;player&gt; &lt;crate&gt; [amount]</code></td><td><code>clearcrates.admin</code> (ops by default)</td></tr>
<tr><td><code>/crate edit &lt;crate&gt;</code>, <code>/crate setchance &lt;crate&gt; &lt;slot&gt; &lt;chance&gt;</code></td><td><code>clearcrates.admin</code></td></tr>
<tr><td><code>/crate reload</code></td><td><code>clearcrates.admin</code></td></tr></table></div>
<h2>Optional hooks</h2><p>PlaceholderAPI (<code>%clearcrates_keys_&lt;crate&gt;%</code>), ItemsAdder and Nexo items. None are required.</p>
<h2>Example config</h2><p class="muted">Chances are weights, so they don't need to add up to 100.</p><pre><code>{cfg}</code></pre>
<h2>Requirements</h2><ul><li>Paper 1.21 (tested on 1.21.4; other 1.21.x Paper builds are expected to work)</li><li>Java 21</li><li>Folia is not supported yet</li></ul>
<h2 id="install">Installation</h2><p>Full walkthrough: <a href="../guides/clearcrates.html">ClearCrates setup guide</a>.</p><ol><li>Stop your server.</li><li>Put <code>ClearCrates-1.0.0.jar</code> in your <code>plugins/</code> folder.</li><li>Start the server so <code>plugins/ClearCrates/config.yml</code> is created.</li><li>Edit the config or use <code>/crate edit &lt;crate&gt;</code> in game, then run <code>/crate reload</code>.</li><li>Give keys with <code>/crate give &lt;player&gt; &lt;crate&gt; [amount]</code>.</li></ol>
<h2>Support</h2><p>Bugs or questions: <a href="{ISSUES}">ClearCrates issues on GitHub</a>.</p>
<h2>Licence</h2><p>One server network per purchase. No redistribution or resale. See the <a href="../terms.html">terms</a>.</p></div></section>
{buy("../")}'''
faq=f'''<section><div class="wrap"><h1>FAQ</h1>
<h2>Refunds</h2><p>Plugins are digital goods, so all sales are normally final once the file has been sent. If something doesn't work on your server, open an issue first and we'll help you fix it. If we genuinely can't get it working on a supported setup, get in touch and we'll sort out a fair solution.</p>
<h2>Server owner FAQ</h2>
<h3>Which server software is supported?</h3><p>Every plugin runs on Paper 1.21 (tested on 1.21.4) with Java 21. Folia isn't supported yet. Spigot and Bukkit aren't tested.</p>
<h3>Does it need other plugins?</h3><p>ClearKits, ClearDaily, ClearAFK and ClearTags have no dependencies (ClearTags works best with a permissions plugin such as LuckPerms). For ClearCrates, PlaceholderAPI, ItemsAdder and Nexo are optional hooks. ClearVotes needs NuVotifier (free) to receive votes from vote sites. ClearKoth, ClearStaff, ClearChat, ClearBosses, ClearDialogues and ClearGems have no dependencies (ClearDialogues has no Citizens support). ClearClans needs Vault and an economy plugin only for its clan bank, and ClearSpawners only for Sell all. ClearOrders and ClearAuctions need Vault and an economy plugin (e.g. EssentialsX) to run.</p>
<h3>How many plugins are there?</h3><p>Sixteen: ClearCrates, ClearKits, ClearDaily, ClearAFK, ClearTags, ClearVotes, ClearKoth, ClearClans, ClearStaff, ClearSpawners, ClearChat, ClearBosses, ClearDialogues, ClearOrders, ClearAuctions and ClearGems.</p>
<h3>Are the plugins made with AI?</h3><p>ClearForge plugins are built with AI assistance and tested on a real Paper 1.21 server.</p>
<h3>Can I use it on more than one server?</h3><p>One purchase covers one server network (e.g. a proxy with its backend servers). Please don't redistribute or resell it.</p>
<h3>How do I pay?</h3><p>With Bitcoin through Sell.app, which gives you an instant automatic download. See the Buy section on each plugin page.</p>
<h3>How fast do I get the plugin?</h3><p>Instantly. As soon as Sell.app confirms your Bitcoin payment, the download is delivered automatically.</p>
<h3>Where do I report bugs?</h3><p><a href="{ISSUES}">GitHub issues</a>.</p></div></section>'''
terms=f'''<section><div class="wrap"><h1>Terms</h1>
<ul><li>Each purchase gives one licence for one server network. You may not redistribute, resell or reupload the plugin.</li>
<li>Plugins are digital goods. See the <a href="faq.html">refund policy</a>.</li>
<li>Payments are made in Bitcoin through Sell.app. Crypto transfers can't be reversed, so check the amount before you pay.</li>
<li>Software is provided as is. Always back up your server before installing plugins.</li>
<li>{BRAND} isn't affiliated with Mojang or Microsoft. Minecraft is a trademark of its respective owners.</li></ul></div></section>'''
exec(open("plugins_extra.py").read())
exec(open("guides.py").read())
exec(open("packs_site.py").read())
index=index.replace("{NEWCARDS}",NEWCARDS).replace("{PACKSEC_}",PACKSEC)
for p,t,d,b in EXTRA+GUIDES+[("index.html",f"{BRAND} | Plugins for Minecraft server owners","Paper plugins for Minecraft server owners and admins.",index),
 ("plugins/clearcrates.html",f"ClearCrates | {BRAND}","ClearCrates: transparent crates for Paper 1.21.",cc),
 ("packs.html",f"Plugin packs | {BRAND}","Bundles of ClearForge plugins for Paper 1.21 at a lower price.",packs_page),("faq.html",f"FAQ | {BRAND}","Refunds and server owner FAQ.",faq),("terms.html",f"Terms | {BRAND}","Licence and terms.",terms)]:
    open(p,"w").write(page(p,t,d,b))
