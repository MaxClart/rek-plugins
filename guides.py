# Setup guides, exec'd by build.py (uses BRAND, ISSUES, sell from there). Facts come only from /workspace/products/<name>/.
def C(t): return f"<code>{html.escape(t)}</code>"
def Y(t): return f"<pre><code>{html.escape(t.strip(chr(10)))}</code></pre>"
def LP(node,who="&lt;player&gt;"): return f"<code>/lp user {who} permission set {node} true</code>"
def foot(s,n,price):
    return f'''<h2>Ready to go?</h2><div class="card"><p>{n} is {price}. Pay with Bitcoin and the download arrives automatically.</p>
<p><a class="btn" href="{sell(n)}" target="_blank" rel="noopener">Buy {n}</a> <a class="btn alt" href="../plugins/{s}.html">{n} plugin page</a> <a class="btn alt" href="getting-started.html">Getting started</a></p></div>
<p class="muted">Stuck? <a href="{ISSUES}">Open an issue on GitHub</a>.</p>'''
def guide(s,n,price,intro,body):
    return (f"guides/{s}.html",f"{n} setup guide | {BRAND}",f"Step-by-step setup guide for {n} on Paper 1.21.",
f'''<div class="hero"><div class="wrap"><p class="muted"><a href="index.html">Guides</a> / {n}</p><h1>{n} setup guide</h1><p>{intro}</p>
<p><a class="btn" href="{sell(n)}" target="_blank" rel="noopener">Buy {n} &mdash; {price}</a> <a class="btn alt" href="../plugins/{s}.html">Plugin page</a></p></div></div>
<section><div class="wrap">
<h2>1. Install</h2><p>Follow the <a href="getting-started.html">getting started guide</a>: put <code>{n}-1.0.0.jar</code> in <code>plugins/</code>, restart, and check the console. The config is created at <code>plugins/{n}/config.yml</code>.</p>
{body}
{foot(s,n,price)}</div></section>''')
GUIDES=[]
gs=f'''<div class="hero"><div class="wrap"><p class="muted"><a href="index.html">Guides</a> / Getting started</p><h1>Getting started</h1><p>How to install any ClearForge plugin on a Paper 1.21 server, the right way.</p></div></div>
<section><div class="wrap">
<h2>What you need</h2><ul><li>A Paper 1.21 server (our plugins are tested on Paper 1.21.4). Folia isn't supported yet.</li><li>Java 21.</li><li>Access to your server's files (FTP or your host's file manager) and console.</li></ul>
<h2>1. Download the jar</h2><p>After you pay, Sell.app sends you a delivery email and shows a delivery page. Download the plugin's <code>.jar</code> file from there (for example <code>ClearKits-1.0.0.jar</code>).</p>
<h2>2. Put it in /plugins</h2><ol><li>Stop your server.</li><li>Upload the jar into the <code>plugins/</code> folder of your server.</li></ol>
<h2>3. Restart, don't /reload</h2><p>Start the server again with a full restart. Avoid <code>/reload</code>: it can leave plugins in a broken state. After you edit a config later, use the plugin's own reload command instead (each guide lists it).</p>
<h2>4. Check the console</h2><p>Watch the console while the server starts. You should see the plugin being enabled. Red errors that mention the plugin name mean something is wrong, see troubleshooting below. In game, <code>/plugins</code> lists it in green when it's loaded.</p>
<h2>5. Find config.yml</h2><p>On first start the plugin creates <code>plugins/&lt;PluginName&gt;/config.yml</code>, for example <code>plugins/ClearKits/config.yml</code>. Every config is commented. Edit it, save, then run the plugin's reload command.</p>
<h2>6. Give permissions</h2><p>Each plugin's player permission is on for everyone by default, and admin permissions are for ops by default. To give extra permissions, use a permissions plugin. LuckPerms is a common free option:</p>
<ul><li>One player: {LP("clearkits.kit.vip","Steve")}</li><li>A whole group: <code>/lp group vip permission set clearkits.kit.vip true</code></li></ul>
<h2>Troubleshooting</h2>
<h3>Wrong Java version</h3><p>If the console says the plugin was compiled for a newer Java version (an "UnsupportedClassVersionError"), your server isn't on Java 21. Switch to Java 21 in your host's panel, or install it, and restart.</p>
<h3>Plugin not loading</h3><ul><li>Check the jar is directly in <code>plugins/</code>, not in a subfolder, and ends in <code>.jar</code>.</li><li>Check you're running Paper 1.21, not Spigot, Bukkit or Folia.</li><li>Restart fully and read the first error in the console that mentions the plugin.</li></ul>
<h3>Permissions not working</h3><ul><li>Check the node is spelt exactly as in the guide.</li><li>Ops have admin permissions by default; test with a non-op account too.</li><li>With LuckPerms, check what a player has with <code>/lp user &lt;player&gt; permission info</code>.</li></ul>
<p>Still stuck? <a href="{ISSUES}">Open an issue on GitHub</a> with the console error.</p>
<p><a class="btn alt" href="index.html">All guides</a></p></div></section>'''
GUIDES.append(("guides/getting-started.html",f"Getting started | {BRAND}","How to install ClearForge plugins on Paper 1.21.",gs))

GUIDES.append(guide("clearcrates","ClearCrates","$9.99","Set up your first crate, give out keys and show players the exact drop chances.",f'''
<h2>2. Configure your first crate</h2><p>The default config comes with a crate called <code>vote</code>. Each crate has a <code>display</code> name, <code>rows</code> for the menu size, a <code>key</code> item and a list of <code>rewards</code>.</p>
{Y("""
crates:
  vote:
    display: "<aqua><bold>Vote Crate"
    rows: 3
    key:
      material: TRIPWIRE_HOOK
      name: "<aqua>Vote Key"
""")}
<p>Each reward has a <code>slot</code> (where it sits in the preview), a <code>chance</code>, the <code>material</code>, <code>amount</code> and <code>name</code>. Chances are weights, so they don't need to add up to 100: the preview works out the real percentage for players.</p>
<p>For a command reward, such as money, set <code>give-item: false</code> and add <code>commands</code>. <code>%player%</code> is replaced with the winner's name:</p>
{Y("""
      money:
        slot: 16
        chance: 5
        material: GOLD_BLOCK
        amount: 1
        name: "<gold>$1,000"
        give-item: false
        commands:
          - "eco give %player% 1000"
""")}
<p>Under <code>animation</code> you can set <code>enabled</code>, the spin length in <code>ticks</code> (20 = 1 second) and the <code>sound</code>. Messages are under <code>messages</code> and use MiniMessage colours.</p>
<h2>3. First commands</h2><ul>
<li>{C("/crate list")} shows every crate.</li>
<li>{C("/crate edit vote")} opens the in-game editor: drag items in, close to save.</li>
<li>{C("/crate setchance vote 10 15")} sets the chance of the reward in slot 10 of the vote crate.</li>
<li>{C("/crate give Steve vote 3")} gives Steve 3 vote keys.</li>
<li>{C("/crate preview vote")} shows the rewards and their chances.</li>
<li>{C("/crate reload")} reloads the config after editing the file.</li></ul>
<p>Players right-click a key to open its crate and left-click it to preview.</p>
<h2>4. Permissions</h2><ul><li><code>clearcrates.use</code>: list and preview crates. Everyone has it by default.</li><li><code>clearcrates.admin</code>: give, edit, setchance and reload. Ops by default. Give it to staff with {LP("clearcrates.admin")}.</li></ul>
<h2>Common questions</h2>
<h3>Do the chances need to add up to 100?</h3><p>No. They're weights, and the preview shows each reward's real percentage.</p>
<h3>What if a player's inventory is full?</h3><p>The reward drops at their feet, so it's never lost.</p>
<h3>Does it need other plugins?</h3><p>No. PlaceholderAPI (<code>%clearcrates_keys_&lt;crate&gt;%</code>), ItemsAdder and Nexo are optional hooks.</p>'''))

GUIDES.append(guide("clearkits","ClearKits","$7.99","Set up a starter kit, a daily kit and VIP kits with cooldowns and a click-to-claim menu.",f'''
<h2>2. Configure your kits</h2><p>Each kit under <code>kits</code> has a <code>display</code> name, an <code>icon</code>, a menu <code>slot</code>, <code>public</code>, a <code>cooldown</code>, <code>items</code> and optional <code>commands</code>.</p>
<ul><li><code>cooldown</code> is in seconds: <code>0</code> means no cooldown, <code>-1</code> means one time only, <code>86400</code> is one day.</li>
<li><code>public: true</code> means everyone can use it. Otherwise players need <code>clearkits.kit.&lt;name&gt;</code>.</li></ul>
{Y("""
  daily:
    display: "<yellow>Daily"
    icon: GOLDEN_APPLE
    slot: 12
    public: true
    cooldown: 86400
    items:
      - {material: COOKED_BEEF, amount: 16}
      - {material: TORCH, amount: 32}
    commands:
      - "eco give %player% 100"
""")}
<p><code>first-join-kit: starter</code> gives the starter kit once to brand-new players. Set it to <code>""</code> to turn it off. The menu title and size are under <code>gui</code> (<code>title</code>, <code>rows</code>).</p>
<h2>3. First commands</h2><ul>
<li>{C("/kits")} opens the menu, {C("/kit daily")} claims the daily kit.</li>
<li>Hold the items you want, then {C("/kit create pvp 3600")} saves your inventory as a kit called pvp with a one-hour cooldown. Use {C("-1")} for one time only.</li>
<li>{C("/kit give Steve vip")} gives Steve the VIP kit, ignoring the cooldown.</li>
<li>{C("/kit reset Steve daily")} resets Steve's cooldown for one kit (leave the kit out to reset all).</li>
<li>{C("/kit delete pvp")} deletes a kit, {C("/kit reload")} reloads the config.</li></ul>
<h2>4. Permissions</h2><ul><li><code>clearkits.use</code>: open the menu and claim kits you can access. Everyone by default.</li>
<li><code>clearkits.kit.&lt;name&gt;</code>: access to a non-public kit, e.g. {LP("clearkits.kit.vip")}. <code>clearkits.kit.*</code> gives every kit.</li>
<li><code>clearkits.bypass.cooldown</code>: ignore cooldowns. Ops by default.</li><li><code>clearkits.admin</code>: create, delete, give, reset and reload. Ops by default.</li></ul>
<h2>Common questions</h2>
<h3>Why can I claim every kit with no cooldown?</h3><p>On Paper, ops have every kit and ignore cooldowns by default. Test with a non-op account.</p>
<h3>Do cooldowns survive a restart?</h3><p>Yes, they're saved to <code>data.yml</code>.</p>
<h3>Full inventory?</h3><p>Leftover items drop at the player's feet.</p>'''))

GUIDES.append(guide("cleardaily","ClearDaily","$6.99","Set up a daily login rewards calendar with streaks.",f'''
<h2>2. Configure the calendar</h2>
{Y("""
timezone: "Europe/London"     # when the "day" rolls over
reset-on-miss: true           # missing a whole day sends the player back to day 1
loop: true                    # after the last day, start again from day 1
remind-on-join: true          # tell players on join when a reward is waiting
""")}
<p>Set <code>timezone</code> to your players' timezone. Turn off <code>reset-on-miss</code> if you don't want streaks to reset, and <code>loop</code> if the calendar should stop after the last day.</p>
<p>Rewards go under <code>days</code>, up to 45 days. Each day has an <code>icon</code>, a <code>name</code>, and <code>items</code> and/or <code>commands</code> (with <code>%player%</code>):</p>
{Y("""
days:
  1: {icon: BREAD, name: "<white>16 Bread", items: [{material: BREAD, amount: 16}]}
  3: {icon: GOLD_INGOT, name: "<yellow>$250", commands: ["eco give %player% 250"]}
""")}
<p>Unlisted day numbers in between are skipped. The menu title is <code>gui.title</code>, and all texts are under <code>messages</code>.</p>
<h2>3. First commands</h2><ul>
<li>{C("/daily")} (or {C("/rewards")}) opens the calendar.</li>
<li>{C("/daily setday Steve 5")} moves Steve to day 5.</li>
<li>{C("/daily reset Steve")} resets Steve's streak.</li>
<li>{C("/daily reload")} reloads the config.</li></ul>
<h2>4. Permissions</h2><ul><li><code>cleardaily.use</code>: open the calendar and claim. Everyone by default.</li><li><code>cleardaily.admin</code>: reset, setday and reload. Ops by default, e.g. {LP("cleardaily.admin")}.</li></ul>
<h2>Common questions</h2>
<h3>When does a new day start?</h3><p>At midnight in the <code>timezone</code> you set.</p>
<h3>Is progress saved?</h3><p>Yes, in <code>data.yml</code>, so it survives restarts.</p>'''))

GUIDES.append(guide("clearafk","ClearAFK","$4.99","Set up AFK detection that AFK pools and piston loops can't fool.",f'''
<h2>2. Configure detection and kicks</h2>
{Y("""
afk-after: 300            # seconds without activity before a player is marked AFK
kick:
  enabled: true
  after: 900              # seconds AFK (after being marked AFK) before kicking
  only-when-full: false   # only kick AFK players when the server is at max players
  message: "<red>You were kicked for being AFK too long."
announce: true            # broadcast when players go AFK / come back
tab-tag:
  enabled: true
  format: "<gray>[AFK] </gray><name>"
""")}
<ul><li>Set <code>kick.enabled: false</code> if you never want to kick AFK players, or <code>only-when-full: true</code> to kick only when the server is full.</li>
<li>Players get a warning in the last 30 seconds before a kick.</li>
<li>Only real activity resets the timer: turning your head, chatting, commands, interacting, and breaking or placing blocks. Being pushed by water, pistons or vehicles doesn't count.</li></ul>
<h2>3. First commands</h2><ul><li>{C("/afk")} sets yourself AFK by hand.</li><li>{C("/afk list")} shows who's AFK.</li><li>{C("/afk check Steve")} shows how long Steve has been inactive.</li><li>{C("/afk reload")} reloads the config.</li></ul>
<h2>4. Permissions</h2><ul><li><code>clearafk.use</code> and <code>clearafk.list</code>: everyone by default.</li><li><code>clearafk.admin</code>: reload. Ops by default.</li>
<li><code>clearafk.bypass.kick</code>: never kicked. Ops by default. Give it to staff with {LP("clearafk.bypass.kick")}.</li><li><code>clearafk.bypass</code>: never marked AFK automatically. Nobody by default.</li></ul>
<h2>Common questions</h2><h3>Why wasn't I kicked while testing?</h3><p>Ops have <code>clearafk.bypass.kick</code> by default. Test with a non-op account.</p>'''))

GUIDES.append(guide("cleartags","ClearTags","$5.99","Set up chat tags that players unlock by permission and pick from a menu.",f'''
<h2>2. Configure tags and chat format</h2>
{Y("""
chat-format: "<tag><name><gray>: </gray><message>"   # <tag> is empty when no tag is equipped
menu-title: "<dark_gray>Choose your tag"
tags:
  vip:
    display: "<gold>[VIP] "
    icon: GOLD_INGOT
    description: "For our supporters"
""")}
<p>Each tag has an id (here <code>vip</code>), a <code>display</code> shown in chat (MiniMessage, so colours and gradients work), an <code>icon</code> for the menu and a <code>description</code>. Add as many as you like. Texts are under <code>messages</code>.</p>
<h2>3. First commands</h2><ul><li>{C("/tags")} opens the menu. {C("/tags vip")} equips a tag, {C("/tags clear")} removes it.</li>
<li>{C("/tags set Steve vip")} sets Steve's tag, {C("/tags set Steve none")} removes it.</li><li>{C("/tags reload")} reloads the config.</li></ul>
<h2>4. Permissions</h2><p>Players need <code>cleartags.tag.&lt;id&gt;</code> to equip a tag, or <code>cleartags.tag.*</code> for all. Pair it with a permissions plugin such as LuckPerms:</p>
<ul><li>{LP("cleartags.tag.vip")}</li><li><code>/lp group vip permission set cleartags.tag.vip true</code></li></ul>
<p><code>cleartags.use</code> (open the menu) is on for everyone, and <code>cleartags.admin</code> (set and reload) is for ops by default.</p>
<h2>Common questions</h2><h3>Why does a tag show as grey dye?</h3><p>The player hasn't unlocked it yet: give them its permission.</p><h3>Is a database needed?</h3><p>No, the equipped tag is saved on the player.</p>'''))

GUIDES.append(guide("clearvotes","ClearVotes","$6.99","Set up vote rewards, milestones, streaks and vote links.",f'''
<div class="note"><strong>NuVotifier is required for real votes.</strong> ClearVotes receives votes from <a href="https://github.com/NuVotifier/NuVotifier">NuVotifier</a> (free). Install and set it up first, then add your server to your vote sites. Without it, only <code>/votes test</code> works.<br><span class="warn">Live votes from vote sites haven't been tested yet.</span> Testing used <code>/votes test</code>.</div>
<h2>2. Configure rewards</h2>
<p>Put your real vote site links in <code>links</code> (clickable on <code>/vote</code>):</p>
{Y("""
links:
  - "<aqua><click:open_url:'https://example.com/vote1'>Vote site 1</click>"
""")}
<p><code>rewards</code> are console commands run for every vote, with <code>%player%</code>:</p>
{Y("""
rewards:
  - "give %player% diamond 1"
  - "xp add %player% 100"
milestones:
  10:
    - "give %player% diamond_block 1"
streaks:
  3:
    - "give %player% golden_apple 1"
""")}
<ul><li><code>milestones</code>: extra commands when a player reaches that vote total (10th, 50th, or any number).</li><li><code>streaks</code>: bonus commands on those days of a daily voting streak.</li>
<li><code>broadcast</code> and <code>messages</code> (<code>thanks</code>, <code>queued</code>) set the texts.</li></ul>
<h2>3. First commands</h2><ul><li>{C("/votes test Steve")} sends a test vote for Steve, so you can check rewards without a vote site.</li><li>{C("/vote")} shows the links and your total and streak.</li>
<li>{C("/votes top")} shows the leaderboard.</li><li>{C("/votes reset Steve")} resets Steve's votes.</li><li>{C("/votes reload")} reloads the config.</li></ul>
<h2>4. Permissions</h2><ul><li><code>clearvotes.use</code>: vote links and stats. Everyone by default.</li><li><code>clearvotes.admin</code>: test, reset and reload. Ops by default, e.g. {LP("clearvotes.admin")}.</li></ul>
<h2>Common questions</h2><h3>What if a player votes while offline?</h3><p>Their rewards are queued and given when they next join.</p>
<h3>Does it work without NuVotifier?</h3><p>Only <code>/votes test</code> works. Real votes from sites need NuVotifier.</p>'''))

PL=[("clearcrates","ClearCrates","Crates, keys, rewards and chances."),("clearkits","ClearKits","Starter, daily and VIP kits with cooldowns."),("cleardaily","ClearDaily","Daily rewards calendar, timezone and streaks."),("clearafk","ClearAFK","AFK timer, kicks and tab tag."),("cleartags","ClearTags","Chat tags, format and unlock permissions."),("clearvotes","ClearVotes","NuVotifier, rewards, milestones and streaks.")]
cards="".join(f'<a class="card" href="{s}.html"><h3>{n}</h3><p>{d}</p></a>' for s,n,d in PL)
GUIDES.append(("guides/index.html",f"Guides | {BRAND}","Setup guides for ClearForge plugins.",f'''<div class="hero"><div class="wrap"><h1>Guides</h1><p>Step-by-step setup for every ClearForge plugin. New here? Start with getting started.</p>
<p><a class="btn" href="getting-started.html">Getting started</a></p></div></div>
<section><div class="wrap"><h2>Start here</h2><div class="grid"><a class="card" href="getting-started.html"><h3>Getting started</h3><p>Install any ClearForge plugin on Paper 1.21, plus troubleshooting.</p></a></div>
<h2>Plugin guides</h2><div class="grid">{cards}</div></div></section>'''))
