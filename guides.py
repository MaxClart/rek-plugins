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

GUIDES.append(guide("cleardaily","ClearDaily","$4.99","Set up a daily login rewards calendar with streaks.",f'''
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
GUIDES.append(guide("clearkoth","ClearKoth","$8.99","Mark out a hill, run king of the hill events and schedule them to start by themselves.",f'''
<h2>2. Mark out a hill</h2><ol><li>Stand at one corner of your hill and type {C("/koth pos1")}.</li><li>Go to the opposite corner and type {C("/koth pos2")}. Include some height so players standing on it are inside.</li><li>Or use {C("/koth wand")}: left-click a block for pos1, right-click for pos2.</li><li>Save it with {C("/koth create spawn")}.</li></ol>
<h2>3. Start an event</h2><p>{C("/koth start spawn")} uses the default capture time, or {C("/koth start spawn 120")} for 120 seconds. A player alone on the hill counts down. If a second player steps on, it's contested and the timer pauses. {C("/koth stop")} ends it early.</p>
<h2>4. Config</h2>{Y("""
capture-seconds: 180
max-duration: 1800
reset-on-leave: true
rewards:
  - "give %player% diamond 5"
schedule:
  - time: "18:00"
    hill: "spawn"
    seconds: 180
""")}
<ul><li><code>capture-seconds</code>: how long a player must hold the hill alone.</li><li><code>max-duration</code>: the event ends with no winner after this many seconds (0 = never).</li><li><code>reset-on-leave</code>: progress goes back to 0 when the capper leaves.</li><li><code>rewards</code>: console commands, with <code>%player%</code> and <code>%hill%</code>.</li><li><code>schedule</code>: daily start times in server local time. The hill must exist.</li></ul>
<p>Save, then run {C("/koth reload")}. Hills and win counts are kept in <code>plugins/ClearKoth/data.yml</code>.</p>
<h2>5. Permissions</h2><ul><li><code>clearkoth.use</code>: <code>/koth list</code> and <code>/koth top</code>. Everyone by default.</li><li><code>clearkoth.admin</code>: everything else. Ops by default, e.g. {LP("clearkoth.admin")}.</li></ul>
<h2>Common questions</h2><h3>Does it support PlaceholderAPI?</h3><p>No, PlaceholderAPI is not supported.</p>
<h3>What was tested?</h3><p>Creating a hill with pos1/pos2, winning an event, contested pausing, <code>/koth top</code> and a scheduled start were tested with bots on Paper 1.21.4. The wand, delete, reload, reset-on-leave and the time limit were not bot-tested.</p>'''))
GUIDES.append(guide("clearclans","ClearClans","$8.99","Let players create and run their own clans, with roles, clan chat, a home and friendly fire.",f'''
<h2>2. Your first clan</h2><ol><li>{C("/clan create Wolves")} creates a clan with you as owner.</li><li>{C("/clan invite Steve")} sends a clickable invite. Steve runs {C("/clan accept")} (or {C("/clan deny")}).</li><li>{C("/clan info")} shows members and roles. {C("/clan promote Steve")} and {C("/clan demote Steve")} change roles.</li></ol>
<h2>3. Chat, home and friendly fire</h2><ul><li>{C("/clan chat hello")} sends one message to the clan. {C("/clan chat")} on its own toggles all your messages into clan chat.</li><li>{C("/clan sethome")} then {C("/clan home")}. Players must stand still for the configured delay.</li><li>{C("/clan ff")} toggles friendly fire for your clan. It's off by default.</li></ul>
<h2>4. Config</h2><p>Edit <code>plugins/ClearClans/config.yml</code> (member limit, home delay, friendly fire default, chat tag, messages), then run {C("/clan reload")}. Data is kept in <code>plugins/ClearClans/data.yml</code>.</p>
<h2>5. Optional clan bank</h2><p>Install Vault and an economy plugin to enable {C("/clan bank deposit 100")}, {C("/clan bank withdraw 100")} and {C("/clan top bank")}.</p>
<h2>Common questions</h2><h3>What was tested?</h3><p>Create, invite, accept, info, clan chat, home, friendly fire, /clan top and the chat tag were tested with two bots on Paper 1.21.4. The clan bank was not tested (no economy plugin was installed), and kick, promote and demote were not bot-tested.</p>'''))
GUIDES.append(guide("clearstaff","ClearStaff","$9.99","Set up vanish, freeze, invsee, staff chat and the punishment menu for your staff team.",f'''
<h2>2. Give staff permissions</h2><p>All permissions default to op. For non-op staff, give them what they need, e.g. {LP("clearstaff.*","Steve")} for everything, or single nodes like <code>clearstaff.vanish</code>, <code>clearstaff.freeze</code>, <code>clearstaff.punish</code>.</p>
<h2>3. Everyday tools</h2><ul><li>{C("/vanish")} (or {C("/v")}) hides you. Staff with <code>clearstaff.vanish.see</code> still see you.</li><li>{C("/freeze Steve")} stops Steve moving and using commands (except the whitelist).</li><li>{C("/invsee Steve")} and {C("/endersee Steve")} are read-only unless you have <code>clearstaff.invsee.edit</code>.</li><li>{C("/sc hello")} for staff chat, or {C("/sc")} to toggle.</li></ul>
<h2>4. Punishments</h2><p>{C("/punish Steve")} opens a menu of your presets (warn, mute, kick, temp ban, ban). Edit durations, icons and reasons in <code>plugins/ClearStaff/config.yml</code>, then {C("/clearstaff reload")}. Bans use the server ban list, so {C("/pardon Steve")} removes them. {C("/unmute Steve")} lifts a mute and {C("/history Steve")} shows past punishments.</p>
<h2>Common questions</h2><h3>What was tested?</h3><p>Vanish, freeze (movement and commands), invsee, endersee, staff chat, the punish menu, the mute and 1-day temp ban presets, /pardon, /unmute and /history were tested with two bots on Paper 1.21.4. Read-only mode, damage blocking while frozen, the warn, kick and permanent ban presets, and mute expiry were not bot-tested.</p>'''))
GUIDES.append(guide("clearspawners","ClearSpawners","$7.99","Set up stackable virtual spawners with storage, collect and sell all.",f'''
<h2>2. Optional: Vault for Sell all</h2><p>Sell all pays through Vault, so install Vault and an economy plugin such as EssentialsX. Without them, everything else works and the Sell all button is greyed out.</p>
<h2>3. Using spawners</h2><ul><li>Place spawners as normal, or give them with {C("/spawners give Steve pig 1 3")} (player, mob, amount, stack).</li><li>Right-click a spawner to open its storage: Collect items, Collect XP or Sell all.</li><li>Right-click it while holding a spawner of the same type to stack. Sneak-right-click does neither.</li><li>Break it with a silk touch tool (or with <code>clearspawners.pickup</code>) to keep the spawner and its stack.</li></ul>
<h2>4. Config</h2><p>Edit <code>plugins/ClearSpawners/config.yml</code> (max stack, drop tables, intervals, XP, prices), then run {C("/spawners reload")}. Data is kept in <code>plugins/ClearSpawners/spawners.yml</code>.</p>
<h2>5. Permissions</h2><ul><li><code>clearspawners.use</code> and <code>clearspawners.sell</code>: everyone by default.</li><li><code>clearspawners.pickup</code> and <code>clearspawners.admin</code>: ops by default.</li></ul>
<h2>Common questions</h2><h3>What was tested?</h3><p>Stacking, storage, Collect items, Collect XP, Sell all (with Vault and EssentialsX), silk touch pickup and restarts were tested with a bot using a pig spawner on Paper 1.21.4. Pickup by permission without silk touch, breaking without silk touch, explosion protection and mobs other than pig were not bot-tested.</p>'''))
GUIDES.append(guide("clearchat","ClearChat","$7.99","Set up the word filter, anti-spam, caps and link blocking, and mentions.",f'''
<h2>2. Config</h2><p>Edit <code>plugins/ClearChat/config.yml</code>: filter words, cooldown, caps limit, link whitelist and mention sound. Then run {C("/chat reload")}.</p>
<h2>3. Staff commands</h2><ul><li>{C("/chat clear")} wipes chat for players without the bypass.</li><li>{C("/chat mute")} mutes global chat (run it again to unmute).</li><li>{C("/chat reload")} reloads the config.</li></ul><p>These need <code>clearchat.admin</code> (ops by default).</p>
<h2>4. Bypass permissions</h2><p>Ops have these by default: <code>clearchat.bypass.filter</code>, <code>.cooldown</code>, <code>.duplicate</code>, <code>.caps</code>, <code>.links</code>, <code>.mute</code>, <code>.clear</code>, or <code>clearchat.bypass.*</code> for all. For example {LP("clearchat.bypass.links")}.</p>
<h2>Common questions</h2><h3>Does it replace my chat format?</h3><p>No. ClearChat only changes the message text, so plugins such as ClearTags keep working. Its own chat format is off by default and skipped when ClearTags is installed.</p>
<h3>What was tested?</h3><p>Censoring, cooldown, duplicate block, caps lowering, link and IP blocking, mentions, /chat mute, /chat clear and op bypass were tested with bots on Paper 1.21.4 alongside ClearTags. Block mode for the filter and caps, and ClearChat's own optional chat format, were not bot-tested.</p>'''))
GUIDES.append(guide("clearbosses","ClearBosses","$9.99","Make your own boss, give it phases and loot, and spawn it for an event.",f'''
<h2>2. Make a boss</h2><p>Open <code>plugins/ClearBosses/config.yml</code> and add a boss under <code>bosses:</code>. The commented Zombie King and Witch Queen examples show every option: mob type, name, health, damage, speed, knockback resistance, equipment, boss bar range, phases, loot and rewards. Then run {C("/boss reload")}.</p>
<h2>3. Phases</h2><p>Each phase triggers at a health percentage with a message and actions:</p><ul><li><code>minions &lt;TYPE&gt; &lt;count&gt;</code></li><li><code>effect &lt;EFFECT&gt; &lt;seconds&gt; &lt;level&gt;</code></li><li><code>knockback &lt;radius&gt; &lt;strength&gt;</code></li><li><code>damage &lt;radius&gt; &lt;amount&gt;</code></li><li><code>lightning &lt;radius&gt;</code></li><li><code>heal &lt;amount&gt;</code></li></ul>
<h2>4. Spawn and manage</h2><ul><li>{C("/boss spawn zombie_king")} spawns at the block you're looking at. Add <code>here</code> for your feet, or <code>&lt;world&gt; &lt;x&gt; &lt;y&gt; &lt;z&gt;</code> (works from console).</li><li>{C("/boss list")} shows alive bosses with health and location.</li><li>{C("/boss kill all")} removes them.</li></ul><p>All commands need <code>clearbosses.admin</code> (ops by default). Minions stay alive after their boss dies until they're killed or the server stops.</p>
<h2>Common questions</h2><h3>What was tested?</h3><p>Spawning, the boss bar, a minion phase, loot, reward commands, /boss list, /boss kill and cleanup after restart were tested with a bot on Paper 1.21.4. Timed spawns, the knockback, damage, lightning and heal actions, top-damager mode with several players, and the Witch Queen example were not bot-tested.</p>'''))
GUIDES.append(guide("cleardialogues","ClearDialogues","$6.99","Create a talking NPC with branching, clickable choices and rewards.",f'''
<h2>2. Write a dialogue</h2><p>Open <code>plugins/ClearDialogues/config.yml</code> and copy the blacksmith example. Each dialogue is made of nodes with MiniMessage lines. Choices can use <code>text</code>, <code>goto &lt;node&gt;</code>, <code>commands [...]</code>, <code>end: true</code>, <code>permission &lt;perm&gt;</code> and <code>once &lt;flag&gt;</code>. Then run {C("/dialogue reload")}.</p>
<h2>3. Place the NPC</h2><p>Stand where it should be and run {C("/dialogue npc create blacksmith")}. Players right-click it to talk. {C("/dialogue npc remove")} removes the nearest one within 5 blocks. {C("/dialogue start blacksmith Steve")} starts a dialogue without an NPC.</p>
<h2>4. Permissions</h2><ul><li><code>cleardialogues.use</code>: talk to NPCs. Everyone by default.</li><li><code>cleardialogues.admin</code>: everything else. Ops by default.</li></ul><p>One-time flags are stored on the player, so they survive restarts.</p>
<h2>Common questions</h2><h3>Does it work with Citizens?</h3><p>No, there is no Citizens support. ClearDialogues spawns its own simple NPCs.</p>
<h3>What was tested?</h3><p>Creating an NPC, typed lines, clickable choices, a reward, one-time locks, expired links, restarts and NPC removal were tested with a bot on Paper 1.21.4. The permission lock was not tested with a player lacking the permission.</p>'''))
GUIDES.append(guide("clearorders","ClearOrders","$5.99","Set up a player-run buy order market with escrow and partial fills.",f'''
<h2>2. Install Vault and an economy</h2><p>ClearOrders needs Vault and an economy plugin such as EssentialsX. Without one, it disables itself and says so in the console.</p>
<h2>3. Config</h2><p>Edit <code>plugins/ClearOrders/config.yml</code> (max orders, listing fee, price limits, blacklist), then run {C("/order reload")}. Data is kept in <code>plugins/ClearOrders/orders.yml</code> and saved after every transaction.</p>
<h2>4. How players use it</h2><ul><li>{C("/order create cobblestone 120 2")} posts an order for 120 cobblestone at $2 each. The $240 total is held in escrow.</li><li>{C("/orders")} opens the menu. Click an order to sell your matching items. {C("/orders search cobblestone")} filters, and {C("/orders mine")} shows your own orders.</li><li>{C("/orders collect")} takes the items bought for you. Anything that doesn't fit stays in the box.</li><li>{C("/order cancel <id>")} (or click it in "Your orders") refunds the unfilled part.</li></ul><p>Only plain items (no custom names, enchantments or damage) can be sold into orders.</p>
<h2>5. Permissions</h2><ul><li><code>clearorders.use</code>: everyone by default.</li><li><code>clearorders.admin</code>: reload and cancel any order. Ops by default.</li><li><code>clearorders.bypass.limit</code>: ignore the max-orders limit.</li></ul>
<h2>Common questions</h2><h3>What was tested?</h3><p>Escrow, partial fills, payment, duplication attempts with fast clicks, shift-clicks, number-key swaps and double-clicks, collecting, cancelling with a refund, and the no-economy shutdown were tested with two bots on Paper 1.21.4 with Vault and EssentialsX. Sorting, search, paging, the max-orders limit and the listing fee were not bot-tested.</p>'''))
GUIDES.append(guide("clearauctions","ClearAuctions","$7.99","Set up a single-server auction house with sort, search, expiry and a collection box.",f'''
<h2>2. Install Vault and an economy</h2><p>ClearAuctions needs Vault and an economy plugin such as EssentialsX. Without one, it disables itself and says so in the console.</p>
<h2>3. Config</h2><p>Edit <code>plugins/ClearAuctions/config.yml</code> (max listings, duration, fees, tax, price limits, blacklist), then run {C("/ah reload")}. Data is kept in <code>plugins/ClearAuctions/auctions.yml</code> and saved after every transaction. Single server only: don't point two servers at the same file.</p>
<h2>4. How players use it</h2><ul><li>Hold an item and run {C("/ah sell 100")} to list the whole stack for $100. Custom, renamed and enchanted items keep their full data.</li><li>{C("/ah")} opens the menu. Click to buy. {C("/ah search sword")} filters, and {C("/ah mine")} shows your listings (click to cancel).</li><li>{C("/ah collect")} gives back items from expired or cancelled listings, or bought items that didn't fit.</li><li>{C("/ah cancel <id>")} cancels a listing. Admins can cancel any, and the item goes back to the seller.</li></ul><p>Aliases: <code>/auction</code>, <code>/auctions</code>.</p>
<h2>5. Permissions</h2><ul><li><code>clearauctions.use</code>: everyone by default.</li><li><code>clearauctions.admin</code>: reload and cancel any listing. Ops by default.</li><li><code>clearauctions.bypass.limit</code> and <code>clearauctions.bypass.fee</code>: no one by default, not even ops.</li></ul>
<h2>Common questions</h2><h3>What was tested?</h3><p>Duplication attempts with every click type, simultaneous buyers, buying while cancelling, enchanted items, sorting, search, limits, blacklist, listing fee, expiry, collection box, restarts and the no-economy shutdown were tested with three bots on Paper 1.21.4 with Vault and EssentialsX. Not tested: paging past 45 listings, the sales tax, the percentage fee, the blocked-names list, a full inventory sending a bought item to the collection box, a payment failure rollback, and economy plugins other than EssentialsX.</p>'''))

PL=[("clearcrates","ClearCrates","Crates, keys, rewards and chances."),("clearkits","ClearKits","Starter, daily and VIP kits with cooldowns."),("cleardaily","ClearDaily","Daily rewards calendar, timezone and streaks."),("clearafk","ClearAFK","AFK timer, kicks and tab tag."),("cleartags","ClearTags","Chat tags, format and unlock permissions."),("clearvotes","ClearVotes","NuVotifier, rewards, milestones and streaks."),("clearkoth","ClearKoth","Hills, boss bar, rewards and schedules."),("clearclans","ClearClans","Clans, roles, chat, home and bank."),("clearstaff","ClearStaff","Vanish, freeze, invsee and punishments."),("clearspawners","ClearSpawners","Stacking, storage, sell all and pickup."),("clearchat","ClearChat","Filter, anti-spam, mentions and mute."),("clearbosses","ClearBosses","Bosses, phases, loot and damage share."),("cleardialogues","ClearDialogues","NPCs, choices, rewards and locks."),("clearorders","ClearOrders","Vault, escrow, filling and collecting."),("clearauctions","ClearAuctions","Vault, selling, buying and expiry.")]
cards="".join(f'<a class="card" href="{s}.html"><h3>{n}</h3><p>{d}</p></a>' for s,n,d in PL)
GUIDES.append(("guides/index.html",f"Guides | {BRAND}","Setup guides for ClearForge plugins.",f'''<div class="hero"><div class="wrap"><h1>Guides</h1><p>Step-by-step setup for every ClearForge plugin. New here? Start with getting started.</p>
<p><a class="btn" href="getting-started.html">Getting started</a></p></div></div>
<section><div class="wrap"><h2>Start here</h2><div class="grid"><a class="card" href="getting-started.html"><h3>Getting started</h3><p>Install any ClearForge plugin on Paper 1.21, plus troubleshooting.</p></a></div>
<h2>Plugin guides</h2><div class="grid">{cards}</div></div></section>'''))
