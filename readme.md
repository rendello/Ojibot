
# Ojibot: The Ojibwe Reddit and Discord Bot
Ojibot is a bot for Discord and Reddit that performs tasks relating to the
Ojibwe language, aka Anishinaabemowin.

![Ojibot cover featuring Thunderbird](Gitlab_images/cover.png)

## Synopsis
Reddit is a website composed of many thousands of user-made forums called
'subreddits'. Discord is a site with user-made chatrooms called 'Discord
servers'. Both of these services host dedicated communities of First Nations'
language learners, and both sites allow for automated accounts that respond to
comments with useful information. This project is meant to fill the Ojibwe-language
bot niche!

## Usage
Ojibot can be called on reddit with /u/ojibot <command>, or on Discord with
!<command> or @[ojibot] <command>. The prompt is configurable on each server.

### Commands
Parts in square brackets can be omitted.  Commands are case-agnostic. 

| Command | Description |
| --- | --- |
| eng[lish] | Translates the following words from Ojibwe to English |
| oji[bwe] | Translates the follwing words from English to Ojibwe |
| syl[labics] | Converts text into Ojibwe Syllabics |
| rom[an] | Converts syllabics into romanized text |
| guide | Shows a writing guide for Ojibwe |
| syl-guide | Shows a writing guide for Ojibwe Syllabics |

## Installing
Ojibot should be available anywhere on Reddit at any time, but will only
respond if bots are allowed on the subreddit.

Ojibot needs to be invited to a Discord server by an admin in order to start,
which can be done by clicking this link (Incomplete).

There is no need to install any of these files or install the bot itself, but
as Open Source software you may run it yourself and/or modify it, just be sure
to follow the license and change the fork's name.

### Detailed Command Overview
Commands can take options for more granular outputs. Options are written like
arguments in many programming languages, taking the form
`command(option1="value", option2="other_value")`.

#### eng[lish]
The Ojibwe People's Dictionary, used for this project, uses Fiero Double Vowel
orthography.

In this program, words like “gitchi” or “gici” automatically become “gichi”,
“ânîn” becomes “aaniin”, and so on (if they aren't found right away). The word
is then searched in the database, and the closest match is shown.

If a word is found in the database, the definition will be returned. TODO what other data?

#### oji[bwe]
Same process as above, without the Fiero-orthography conversions.

#### syl[labics]
Words are case-normalized and roughly converted to Fiero double-vowel
orthography. The words are then converted and returned as syllabic text.

The default syllabics use Eastern a-position finals, left-hand w-dot, and vowel
pointing. By default, no lenis-fortis distinction is made.

- [ ] Discord bot
	- [x] Has credentials
	- [x] Setup / basic functionality
	- [x] Responds to specific commands
	- [x] Usable on many servers
	- [ ] Configurable per-server
- [ ] Reddit bot
	- [ ] Has credentials
	- [ ] Setup / basic functionality
	- [ ] Responds to specific commands
- [ ] Ojibwe to English
	- [x] Finds correct info
	- [ ] Formats information correctly
		- [x] Discord
		- [ ] Reddit
	- [ ] Search / return options
	- [x] Normalized (lowercase, Fiero) search
	- [x] Fuzzy search
- [ ] English to Ojibwe
	- [ ] Finds correct info
	- [ ] Formats information correctly
		- [ ] Discord
		- [ ] Reddit
	- [ ] Search / return options
	- [ ] Fuzzy search
- [ ] Romanized to syllabics
	- [ ] Converts
	- [ ] Search / return options
- [ ] Syllabics to romanized
	- [ ] Converts
		- [ ] Uses database instead of guessing
			- [ ] Fuzzy search
	- [ ] Search / return options
- [ ] Guide
	- [ ] Fiero
		- [ ] Discord
		- [ ] Reddit
	- [ ] Syllabic
		- [ ] Discord
		- [ ] Reddit
