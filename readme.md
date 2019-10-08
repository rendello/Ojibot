# Ojibot: The Ojibwe Reddit and Discord Bot
Ojibot is a bot for Discord and Reddit that performs tasks relating to the
[Ojibwe language](https://en.wikipedia.org/wiki/Ojibwe_language).

*Ojibot is a work in progress and is not finished!*

![Ojibot cover featuring Thunderbird](Gitlab_images/cover.png)

## Synopsis
Ojibot is a *bot* for both the Discord chat application, and the Reddit forum
website. It can respond to user *commands* with different useful functions.
Described in more detail below, these functions include:
- translating to and from Ojibwe,
- transliterating between Latin and Syllabic scripts, and
- getting useful Ojibwe guides

## Usage
Ojibot can be called on reddit with /u/ojibot \<command\>, or on Discord with
!\<command\> (the prompt is configurable on each server).

Parts in square brackets can be omitted.  Commands are case-agnostic. 

| Command | Description |
| --- | --- |
| (No command) | Detects the text's language and translates it into the other. If there's no text at all, it will try to translate the previous comment. |
| eng[lish] | Translates the following words from Ojibwe to English |
| oji[bwe] | Translates the follwing words from English to Ojibwe |
| syl[labics] | Converts text into Ojibwe Syllabics |
| la[tin] | Converts syllabics into romanized text |
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


- [ ] Discord bot
	- [x] Has credentials
	- [x] Setup / basic functionality
	- [x] Responds to specific commands
	- [x] Usable on many servers
	- [ ] Configurable per-server
- [ ] Reddit bot
	- [x] Has credentials
	- [x] Setup / basic functionality
	- [ ] Responds to specific commands
- [ ] Ojibwe to English
	- [x] Finds correct info
	- [x] Formats information correctly
		- [x] Discord
		- [x] Reddit
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
