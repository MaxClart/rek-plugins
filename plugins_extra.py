# Extra plugin pages, exec'd by build.py (uses page, buy, ISSUES, html from there).
P=[
 dict(slug="clearkits",name="ClearKits",price="$7.99",jar="ClearKits-1.0.0.jar",
  card="Kits with per-kit cooldowns, one-time kits and a click-to-claim menu. Build kits from your own inventory. No dependencies.",
  lead="Kits that just work. Players open /kits, see exactly which kits are ready, and click to claim. You build kits from your own inventory in seconds.",
  why=[("Live status","every kit in the menu shows Click to claim, Ready in 23h 59m, Already claimed or Locked."),("Build in game","<code>/kit create</code> saves your inventory as a kit, enchantments and names included."),("Survives restarts","cooldowns are saved to <code>data.yml</code>.")],
  feat=["Per-kit cooldowns in seconds, or one-time-only kits (cooldown -1)","First-join kit given automatically to brand-new players (configurable, or off)","Item rewards plus console commands with a %player% placeholder","Public kits, or a per-kit permission clearkits.kit.<name>","Full inventories: leftover items drop at the player's feet, never lost","MiniMessage colours in names, the menu title and all messages","Tab completion on every command"],
  cmds=[("<code>/kits</code>, <code>/kit</code>, <code>/kit &lt;kit&gt;</code>","<code>clearkits.use</code> (everyone), plus <code>clearkits.kit.&lt;kit&gt;</code> for non-public kits"),("<code>/kit create &lt;name&gt; &lt;cooldownSeconds|-1&gt;</code>","<code>clearkits.admin</code> (ops by default)"),("<code>/kit delete &lt;kit&gt;</code>, <code>/kit give &lt;player&gt; &lt;kit&gt;</code>","<code>clearkits.admin</code>"),("<code>/kit reset &lt;player&gt; [kit]</code>, <code>/kit reload</code>","<code>clearkits.admin</code>"),("Ignore cooldowns","<code>clearkits.bypass.cooldown</code> (ops by default)"),("Access every kit","<code>clearkits.kit.*</code>")],
  cmdnote="On Paper, server operators can use every kit and skip cooldowns by default.",
  steps=["Edit the kits in the config, or hold the items you want and run <code>/kit create &lt;name&gt; &lt;cooldown&gt;</code>.","Give non-public kits with the permission <code>clearkits.kit.&lt;name&gt;</code>, then run <code>/kit reload</code> after editing the file."]),
 dict(slug="cleardaily",name="ClearDaily",price="$6.99",jar="ClearDaily-1.0.0.jar",
  card="A daily login rewards calendar with streaks, item and command rewards, and join reminders. No dependencies.",
  lead="Give players a reason to log in every day. They type /daily, see the whole calendar, and click today's reward. Tomorrow they move on to the next day.",
  why=[("Clear calendar","claimed days, today's glowing reward and locked days are all marked."),("Real streaks","miss a whole day and it's back to day 1 (or turn that off)."),("Your timezone","the day rolls over at midnight in the timezone you set.")],
  feat=["Up to 45 days, each with its own icon, name, items and console commands (%player%)","Loop back to day 1 after the last day, or stop (configurable)","Join reminder when a reward is waiting (can be turned off)","Streak card showing total rewards claimed and time until the next one","Progress saved to data.yml, so it survives restarts","Full inventories: leftover items drop at the player's feet, never lost","MiniMessage colours in all names and messages"],
  cmds=[("<code>/daily</code> (or <code>/rewards</code>)","<code>cleardaily.use</code> (everyone by default)"),("<code>/daily reset &lt;player&gt;</code>","<code>cleardaily.admin</code> (ops by default)"),("<code>/daily setday &lt;player&gt; &lt;day&gt;</code>","<code>cleardaily.admin</code>"),("<code>/daily reload</code>","<code>cleardaily.admin</code>")],
  cmdnote="",
  steps=["Set your timezone and the rewards for each day in the config, then run <code>/daily reload</code>."]),
 dict(slug="clearafk",name="ClearAFK",price="$4.99",jar="ClearAFK-1.0.0.jar",
  card="AFK detection that water streams and pistons can't fool, with an [AFK] tab tag, announcements and an optional kick. No dependencies.",
  lead="Know who's really there. Only real activity resets the AFK timer, so AFK pools and piston loops don't keep idle players counted as active.",
  why=[("Hard to fool","only head turns, chat, commands, interacting and breaking or placing blocks count as activity. Being pushed by water, pistons or vehicles doesn't."),("Visible","an [AFK] tag shows in the tab list."),("Fair kicks","a warning in the last 30 seconds, and an option to kick only when the server is full.")],
  feat=["Automatic AFK after a set time (default 5 minutes)","/afk to set yourself AFK by hand","Tab-list tag format you can change","Broadcast when players go AFK and come back (can be turned off)","Optional kick after a set time AFK","/afk list and /afk check <player> to see who's idle and for how long","MiniMessage colours in all messages","Tab completion"],
  cmds=[("<code>/afk</code>","<code>clearafk.use</code> (everyone by default)"),("<code>/afk list</code>, <code>/afk check &lt;player&gt;</code>","<code>clearafk.list</code> (everyone by default)"),("<code>/afk reload</code>","<code>clearafk.admin</code> (ops by default)"),("Never kicked","<code>clearafk.bypass.kick</code> (ops by default)"),("Never marked AFK automatically","<code>clearafk.bypass</code> (nobody by default)")],
  cmdnote="",
  steps=["Set <code>afk-after</code> and the kick options in the config, then run <code>/afk reload</code>."]),
 dict(slug="cleartags",name="ClearTags",price="$5.99",jar="ClearTags-1.0.0.jar",
  card="Players pick a chat tag from a click menu. Tags unlock by permission, so they work with ranks, store packages or crates. No dependencies.",
  lead="Chat tags without the setup headache. Players type /tags, see every tag, and click to equip one. Tags they haven't unlocked show as locked grey dye.",
  why=[("Click menu","unlocked tags show their icon, locked tags show as grey dye, and a barrier removes your tag."),("Unlock by permission","<code>cleartags.tag.&lt;id&gt;</code>, or <code>cleartags.tag.*</code> for all, so tags work with ranks, store packages or crates."),("No database","the equipped tag is saved on the player.")],
  feat=["Tags use MiniMessage, so colours and gradients work","Custom chat format, e.g. <tag><name><gray>: </gray><message>","/tags <tag> and /tags clear for players","/tags set <player> <tag|none> and /tags reload for admins"],
  cmdhead="Who",
  cmds=[("<code>/tags</code>, <code>/tags &lt;tag&gt;</code>, <code>/tags clear</code>","Players"),("<code>/tags set &lt;player&gt; &lt;tag|none&gt;</code>, <code>/tags reload</code>","Admins"),("Unlock a tag","<code>cleartags.tag.&lt;id&gt;</code>, or <code>cleartags.tag.*</code> for all")],
  cmdnote="Pair it with any permissions plugin (such as LuckPerms) to hand out tags.",
  deps="None. Pair it with any permissions plugin (such as LuckPerms) to hand out tags.",
  reqs=["Paper 1.21.4","Java 21"],
  tested="Tested on Paper 1.21.4 with a bot: the menu opened, a locked tag was refused, an unlocked tag equipped, and chat showed the prefix.",
  steps=["Set up your tags and chat format in the config, give players <code>cleartags.tag.&lt;id&gt;</code> permissions, then run <code>/tags reload</code>."]),
 dict(slug="clearvotes",name="ClearVotes",price="$6.99",jar="ClearVotes-1.0.0.jar",
  card="Vote rewards with milestone bonuses, daily streaks and an offline queue. Hooks into NuVotifier.",
  lead="Turn votes into players. ClearVotes hooks into NuVotifier and runs any commands you like when someone votes, with milestone and daily streak bonuses.",
  why=[("Milestones","extra rewards at a player's 10th, 50th (or any) vote."),("Daily streaks","bonus rewards for voting on consecutive days."),("Offline queue","vote while offline and the rewards arrive on your next join.")],
  feat=["Any console commands per vote, with %player%","Broadcast message and clickable vote links on /vote, with the player's total and streak","/votes top leaderboard","/votes test <player> to try rewards without a vote site","/votes reset and /votes reload"],
  cmdhead="What it does",
  cmds=[("<code>/vote</code>","Clickable vote links, plus your total and streak"),("<code>/votes top</code>","Vote leaderboard"),("<code>/votes test &lt;player&gt;</code>","Try rewards without a vote site"),("<code>/votes reset</code>, <code>/votes reload</code>","Reset votes, reload the config")],
  cmdnote="",
  deps="<a href=\"https://github.com/NuVotifier/NuVotifier\">NuVotifier</a> (free) is needed to receive votes from vote sites. Without it, <code>/votes test</code> still works.",
  reqs=["Paper 1.21.4","Java 21","NuVotifier (free) to receive votes from sites"],
  tested="Tested on Paper 1.21.4 with bots using /votes test: rewards were given, /vote showed stats, an offline player's rewards were delivered on join, and /votes top listed both voters. Live votes from a vote site were not tested yet.",
  steps=["Install NuVotifier and add your server to your vote sites.","Set your rewards, milestones, streaks and vote links in the config, then run <code>/votes reload</code>.","Try it with <code>/votes test &lt;player&gt;</code>."]),
]
NEWCARDS="";EXTRA=[]
for x in P:
    n=x["name"];s=x["slug"]
    NEWCARDS+=f'''<div class="card"><img src="assets/{s}-cover.png" alt="{n} cover" width="1200" height="600">
<h3>{n}</h3><p>{html.escape(x["card"])}</p>
<p class="price">{x["price"]}</p><p><a class="btn" href="plugins/{s}.html">View plugin</a> <a class="btn alt" href="plugins/{s}.html#buy">Buy</a></p></div>
'''
    cfgt=html.escape(open(f"/workspace/products/{s}/src/main/resources/config.yml").read())
    why="".join(f"<li><strong>{a}:</strong> {b}</li>" for a,b in x["why"])
    fl="".join(f"<li>{html.escape(f)}</li>" for f in x["feat"])
    rows="".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in x["cmds"])
    note=f'<p class="muted">{x["cmdnote"]}</p>' if x["cmdnote"] else ""
    tst=f'<h2>Tested</h2><p>{html.escape(x["tested"])}</p>' if x.get("tested") else ""
    reqs="".join(f"<li>{html.escape(r)}</li>" for r in x.get("reqs",["Paper 1.21 (tested on 1.21.4; other 1.21.x Paper builds are expected to work)","Java 21","Folia is not supported yet"]))
    steps="".join(f"<li>{t}</li>" for t in x["steps"])
    body=f'''<div class="hero"><div class="wrap"><h1>{n}</h1><p>{html.escape(x["lead"])}</p>
<p class="price">{x["price"]}</p><p><a class="btn" href="#buy">Buy now</a> <a class="btn alt" href="#install">Install guide</a></p></div></div>
<section><div class="wrap"><img src="../assets/{s}-cover.png" alt="{n} cover" width="1200" height="600">
<h2>Why {n}</h2><ul>{why}</ul>
<h2>Features</h2><ul>{fl}</ul>
<h2>Commands &amp; permissions</h2><div class="tablewrap"><table><tr><th>Command</th><th>{x.get("cmdhead","Permission")}</th></tr>
{rows}</table></div>{note}
<h2>Dependencies</h2><p>{x.get("deps","None.")}</p>{tst}
<h2>Example config</h2><pre><code>{cfgt}</code></pre>
<h2>Requirements</h2><ul>{reqs}</ul>
<h2 id="install">Installation</h2><ol><li>Stop your server.</li><li>Put <code>{x["jar"]}</code> in your <code>plugins/</code> folder.</li><li>Start the server so <code>plugins/{n}/config.yml</code> is created.</li>{steps}</ol>
<h2>Support</h2><p>Bugs or questions: <a href="{ISSUES}">open an issue on GitHub</a>.</p>
<h2>Licence</h2><p>One server network per purchase. No redistribution or resale. See the <a href="../terms.html">terms</a>.</p></div></section>
{buy("../",n,x["price"])}'''
    EXTRA.append((f"plugins/{s}.html",f"{n} | {BRAND}",f"{n}: {x['card'].split('.')[0]}. For Paper 1.21.",body))
