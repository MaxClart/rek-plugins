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
    steps="".join(f"<li>{t}</li>" for t in x["steps"])
    body=f'''<div class="hero"><div class="wrap"><h1>{n}</h1><p>{html.escape(x["lead"])}</p>
<p class="price">{x["price"]}</p><p><a class="btn" href="#buy">Buy now</a> <a class="btn alt" href="#install">Install guide</a></p></div></div>
<section><div class="wrap"><img src="../assets/{s}-cover.png" alt="{n} cover" width="1200" height="600">
<h2>Why {n}</h2><ul>{why}</ul>
<h2>Features</h2><ul>{fl}</ul>
<h2>Commands &amp; permissions</h2><div class="tablewrap"><table><tr><th>Command</th><th>Permission</th></tr>
{rows}</table></div>{note}
<h2>Dependencies</h2><p>None.</p>
<h2>Example config</h2><pre><code>{cfgt}</code></pre>
<h2>Requirements</h2><ul><li>Paper 1.21 (tested on 1.21.4; other 1.21.x Paper builds are expected to work)</li><li>Java 21</li><li>Folia is not supported yet</li></ul>
<h2 id="install">Installation</h2><ol><li>Stop your server.</li><li>Put <code>{x["jar"]}</code> in your <code>plugins/</code> folder.</li><li>Start the server so <code>plugins/{n}/config.yml</code> is created.</li>{steps}</ol>
<h2>Support</h2><p>Bugs or questions: <a href="{ISSUES}">open an issue on GitHub</a>.</p>
<h2>Licence</h2><p>One server network per purchase. No redistribution or resale. See the <a href="../terms.html">terms</a>.</p></div></section>
{buy("../",n,x["price"])}'''
    EXTRA.append((f"plugins/{s}.html",f"{n} | {BRAND}",f"{n}: {x['card'].split('.')[0]}. For Paper 1.21.",body))
