# Install and use the how-to-mind-map skill

## Before you install

- Skills work on Free, Pro, Max, Team and Enterprise plans.
- Skills need code execution. On an individual plan, go to **Settings > Capabilities** and turn on **Code execution and file creation** (called **Create and edit files** in the newer settings layout).
- On a Team or Enterprise plan, an owner may need to turn on code execution and Skills under **Organization settings > Plugins & skills**, on the **Policy** tab.

## Install in Claude (web or desktop app)

1. Keep the file as `how-to-mind-map.zip`. Don't unzip it or rename the folder inside it; the folder name must match the skill name.
2. Go to **Customize > Skills**.
3. Click **+**, then **+ Create skill**, then **Upload a skill**.
4. Upload `how-to-mind-map.zip`.
5. Make sure the skill's toggle is on.

## Install in Claude Code

Unzip it into your skills folder so the path reads `~/.claude/skills/how-to-mind-map/SKILL.md`, or into `.claude/skills/` inside a project to use it only there.

## Share it with your team (Team and Enterprise)

In **Customize > Skills**, open the three-dot menu next to the skill and choose **Share**, or open the skill and choose **Publish to org**. If the Share button is missing, an owner needs to turn on sharing in **Organization settings > Plugins & skills**.

## Use it

1. Download `assets/intake-template.md` from this folder, or ask Claude for the intake template. Fill it in once; short answers are fine.
2. Start a new chat and attach the filled-in intake plus any material it lists (playbooks, decks, past deliverables, templates).
3. Say: **"Build my how-to mind map from this intake."**
4. Claude drafts the whole map in one go and hands back an interactive HTML map, a Markdown copy and the outline file. Where it needed your judgment, it marks the node with a **?** instead of stopping to ask.
5. Open the map, click **Open questions** to step through each one, and reply with all your answers in one message. Claude folds them in and rebuilds the map.
6. Rate the branches 1 to 4 in the map by answering "How well do I do this today?", then open the **2x2** tab to see them sorted into the four buckets. Your 3s, the work you do well but that takes effort every time, are the first things to hand to AI or a team.
7. Click **Save my map** whenever you want to keep your work. It saves a copy of the map with your ratings inside; reopen that file anytime. Your ratings also save in your browser as you go, and the header tells you when there are unsaved changes.

To change the map later, attach your saved map file and say what to change. Claude keeps your ratings when it rebuilds.
