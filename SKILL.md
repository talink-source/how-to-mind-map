---
name: how-to-mind-map
description: Build a "how to" mind map of someone's expertise, starting from the outcome they own and asking "how?" until every branch ends in a task someone can put on their calendar, then render it as an interactive HTML map with 1 to 4 competence ratings. Use when someone wants to map their expertise, break an outcome into jobs, find what to hand to AI or a team first, or find content ideas in their know-how.
---

# How-to mind map

A how-to mind map starts from one outcome a person owns ("How to drive growth for a company") and keeps asking "how?" until every branch ends in a task with a clear output. It makes expertise visible: the calls an expert makes on instinct end up written down, where a team or an AI can use them.

The deliverables are an outline file (the source of truth), an interactive HTML map, and a Markdown copy.

## How this skill works with the person

Draft first, ask second. Don't run a long interview. Collect everything in one pass, build the whole map, mark the gaps as open questions inside the map, and resolve them in one batch. The person should spend their time reviewing a draft, not answering questions one at a time.

## Before you start

Read `references/node-rules.md`. Every node you write must pass it. Look at `references/example-outline.txt` for the format and the level of detail expected.

## Step 1: Collect the intake in one message

- If they attached a filled-in intake (`assets/intake-template.md`) or material, start building.
- If they attached nothing, send them the intake template and ask them to fill it in and attach their material. If they'd rather not, ask only these, together in one message:
  1. Finish the sentence "How to ___" with the outcome you own. What does it mean in two or three concrete parts?
  2. Is this your own business, the companies you help, or your team's work?
  3. What big moves or framework do you already use?
  4. What decisions do you make quickly that others get wrong?
  5. Can you attach any playbooks, decks, past deliverables or templates?
- Never ask a question the attached material already answers.

## Step 2: Set the top of the map from the intake

1. Write the top node as "How to [outcome]," with the concrete parts in its note.
2. Use the point of view they chose for every node (see "Whose work it is" in the rules).
3. Use their existing structure as the first two or three levels, in their words.
4. Build from their material first: frameworks, talks, playbooks, deliverables, templates, call notes. Fill gaps with sound general practice only where nothing of theirs covers it. Where you bring in thinking from known practitioners, use the ideas but never put names on nodes.
5. Respect the "leave out" list: no confidential details or names they excluded.

## Step 3: Branch, one level at a time

For each node, ask "how?" and write the three to five jobs that together get it done, in the order the work happens. Then do the same for each child.

- Move down one level of detail at a time: outcome, then approach, then project, then task. Don't jump from strategy straight to a spreadsheet column.
- Put questions, criteria, scripts, thresholds and examples in notes, never as nodes. Notes hold only those specifics: no descriptors that explain or summarize a branch.
- State the rule behind any number instead of an arbitrary count ("until new interviews stop surfacing new themes," not "run 10 interviews").
- Stop each branch at a task someone could schedule today. Keep breaking down anything that is still a project.
- Start any branch about making something happen with its core mechanic (for acquisition: where customers come from and which engine to build), then the supporting bets.
- Carry strategy all the way down to the tactics practitioners run. For acquisition, that means a branch for each channel: search, AI answers, paid search, paid social, organic social, content, creators and earned media.

## Step 4: Write the outline file

Format, two spaces per level:

```
- How to drive growth for a company
  : How a growth operator helps a company get more customers, keep them longer, and get them to spend more.
  - Identify what's limiting growth
    - Demand: not enough people are buying
      - Acquisition: get more customers
        - Find where customers come from today
          - Build an acquisition baseline
            - Count new customers by source for each of the last 12 months
              : Use tracked source and "How did you hear about us?" answers side by side.
```

Lines starting with `- ` are nodes. Lines starting with `: ` are notes on the node above. A note starting with `: ? ` is an open question for the owner. Write the file in sections for a large map, then join them.

### Open questions instead of interviews

When a node needs the owner's judgment and their material doesn't settle it, write your best general-practice version of the node and add an open question to it:

```
- Set the most the company will pay to win a customer
  : ? What ratio of lifetime value to acquisition cost do you hold clients to, and when do you break it?
```

Ask open questions where the owner's specific know-how matters most: the calls they make on instinct, their thresholds, the tools and templates they actually use. Don't ask about things general practice already answers well. The map shows each one with a "?" badge and an "Open questions" button that steps through them.

## Step 5: Build the map

```
python3 scripts/build_map.py outline.txt --title "How to Drive Growth for a Company" \
    --out-html mind-map.html --out-md mind-map.md [--ratings ratings.json]
```

- `--eyebrow` (optional) adds a small label above the title, such as the owner's name ("Sam's mind map"). Leave it out for no label.
- `--ratings` (optional) builds ratings into the HTML, from a ratings export or the JSON inside a saved map. See Step 8.
- The script stops on format errors (odd indentation, skipped levels, stray lines) and names the line. Fix and rerun.
- It prints the node count, the deepest level, nodes per level, the number of open questions, and how many branches end at level 6 or above. Review those shallow branches: each must be a true calendar-level task, or it needs breaking down.

## Step 6: Review before handing over

Walk the map against the rules once, branch by branch:

1. Every node is a job, written from the agreed point of view.
2. Every leaf is a schedulable task with a clear output.
3. No node exists only to add depth.
4. Notes carry the specifics a practitioner would save.
5. No arbitrary numbers: every count, window or threshold is either replaced by the rule that decides it or is a definition or named benchmark.
6. Notes are specifics a practitioner would use, never descriptors that explain or summarize a branch.
7. No names, no em dashes, acronyms spelled out on first use.

Then open the HTML and check it renders: click a few nodes, try search, try "Deepest paths" and "Open questions."

## Step 7: Resolve the open questions in one round

Hand over the HTML, Markdown and outline files, and say how many open questions there are. Ask the owner to click "Open questions" in the map and reply with all their answers in one message. Fold each answer into its node (as a node, a child or a note, per the rules), remove the question, and rebuild. If an answer opens a new branch, break it down the same way.

## Step 8: Rate it together

Walk the person through rating nodes 1 to 4 in the map by answering "How well do I do this today?" (click a node, then 1 to 4 in its panel, or press 1 to 4 on the keyboard):

1. Don't know: a blind spot. Find the blind spots.
2. Needs improvement: a known gap. Learn it with AI beside you, so you can tell when its work is good.
3. Can do with focus: done well, but it takes effort every time. Build this first.
4. Autopilot: done so well no one notices how. Get it out of your head so AI and the team can do it your way.

In the map, clicking a rating in the legend lights up every node with that rating and hides the rest, keeping only the chain above each one; click it again, press Esc or click Clear to go back. The 2x2 tab sorts every rated node into these four buckets, laid out as competence (low to high) against awareness (low to high), with each node one click from its place in the map. On the map, each rated node takes its rating color; unrated nodes stay neutral.

### Keeping the work: the file is the work

Ratings never get lost as long as the person uses "Save my map":

- **As they work**, every rating saves in their browser automatically, so a refresh or a closed tab loses nothing on that computer.
- **"Save my map"** saves a complete copy of the map with their ratings written inside the HTML. Reopening that file anywhere, on any computer, brings everything back. In Chrome or Edge on a local file, the first save asks where to put it and later saves update the same file. In other browsers each save downloads a fresh copy.
- **The header shows the state**: "Unsaved changes" (with the Save button highlighted) or "Saved in this file." On a local file, closing the tab with unsaved changes asks for confirmation.
- **Published on claude.ai** with the `db`, `user` and `downloads` capabilities declared, ratings also save to the viewer's Claude account automatically and follow them across devices. The header says "Saved to your account."

Tell the person this in one or two sentences when you hand over the map.

To pick up their work later, ask them to attach the saved HTML. Its ratings sit in the line `const BAKED = /*RATINGS*/{...}/*END*/;`. Copy that JSON into `ratings.json` and pass `--ratings ratings.json` when rebuilding, so a rebuilt map keeps them. "Copy ratings for Claude" in the 2x2 tab gives the same ratings as text they can paste into a chat.

Use the 3s to suggest what to hand to AI or a team first.

## The interactive map

- Click a node to open it and see its notes, its full "how?" chain and its children. The number on the right edge expands or collapses a node.
- Drag to move. Ctrl or Command plus scroll, or the + and − buttons, to zoom. Pinch on touch screens.
- Arrow keys walk the tree; Enter expands or collapses; 1 to 4 rates; / searches; F fits; Esc closes.
- "Show to level" reveals the map one level at a time, useful when presenting.
- "Deepest paths" steps through the longest chains.
- "Focus on this branch" hides everything outside the selected branch.
- The header shows the node count and the number of levels under the title.
- Click a rating in the legend (bottom left) to light up only the nodes with that rating.
- "Hide rating colors" in the legend turns the map neutral (rating numbers stay on the badges); click again to bring the colors back.
- "Collapse all" closes every branch back to the top level, a clean starting point for presenting or walking someone through the map.
- Three tabs share the same data: **Map**, **2x2** (rated nodes in the four competence buckets) and **Outline** (a readable indented list with notes). A rating made in one shows in the others immediately.
- "Save my map" saves a copy of the whole map with the ratings inside.
- "Open questions" steps through every node marked for the owner's input.

## Files

- `INSTALL.md`: how to install the skill in Claude and how a new user should start.
- `assets/intake-template.md`: the one-time intake the person fills in instead of being interviewed.
- `scripts/build_map.py`: validates the outline and builds the HTML and Markdown. It also counts open questions.
- `assets/template.html`: the viewer. Self-contained apart from one Google Fonts link (Fraunces for headings, Manrope for text, IBM Plex Mono for labels); offline it falls back to system fonts. The look is a studio palette: soft sage paper, deep forest ink for the top levels and controls, and white cards. Color means one thing only: a node's 1 to 4 rating, shown as a pastel tile (peach, sand, periwinkle, sage) with a matching border and badge. Unrated nodes stay neutral. To rebrand, change the tokens in the first `:root` block of its stylesheet (`--rN` is a rating's strong color and `--rNbg` its pastel), plus the matching dark-mode blocks.
- `references/node-rules.md`: what counts as a node, when to stop, and the quality bar.
- `references/example-outline.txt`: a worked excerpt showing format and depth.
