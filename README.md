_# Werewolf

A zero-player version of the social deduction game
designed by [Dimitry Davidoff](https://en.wikipedia.org/wiki/Mafia_(party_game))
with rules modifications by [Andrew Plotkin](https://www.eblong.com/zarf/werewolf.html).

The roles are :

- 1 Medical
- 1 Seer
- 3 Villagers
- 2 Werewolves

## Getting Started

Install dependencies via (poetry)[https://python-poetry.org/] :

```shell
poetry install
```

Run `mv .env_template .env` file and add your OPENAI_API_KEY. Sign up at [https://www.openai.com/](https://www.openai.com/)

- You can configure your model(Default is 'gpt-3.5-turbo') and your rate_limit and token_limit in api.py

- make DEBUG=True in api.py if you want to see all messages passed to GPT model.

```shell
source .env
poetry run python run.py
```

It will save a log file in the bellow format in the records/ folder.

## log.json format

every event in the game is a dictionary.

```javascript
{
  'event':"<event_name>",
  'content':"<...>"
}
```

events are :

- roles :

```javascript
'content':{
  'player':"<player_number>"
  'role':"<role_string>"
}
```

- cycle :

```javascript
'content':"<day/night>"
```

- speech :

```javascript
'content':{
  'player':"<player_number>"
  'context':"<speech_string>"
}
```

- voted :

```javascript
'content':{
  'player':"<player_number>"
  'voted_to_player':"<player_number>"
  'reason':"<complete response>"
}
```

- vote_start :

```javascript
'content':{
  'player':"<player_number>"
  'voted_to_player':"<player_number>"
  'reason':"<complete response>"
}
```

- healed :

```javascript
'content':{
  'player':"<player_number>"
  'reason':"<complete response>"
}
```

- targeted :

```javascript
'content':{
  'player':"<player_number>"
  'reason':"<complete response>"
}
```

- killed :

```javascript
'content':{
  'player':"<player_number>"
}
```

- inquired :

```javascript
'content':{
  'player':"<player_number>"
  'context':"<True: if player is werewolf>"
  'reason':"<complete response>"
}
```

- notetaking :

```javascript
'content':{
  'player':"<player_number>"
  'context':"<speech_string>"
}
```

- end :

```javascript
'content':{
  'winner':"<Werewolves/Villagers>"
}
```

## Prompts

- Game Introduction('prompts/') : rules and the role of the player
- Game Reports('prompts/) :
  - Speeches in last round
  - Game status : alive players in separation of the teams.
  - Players status : aliveness of players based on their number
  - Agent previous SPECIAL actions
  - Agent previous VOTES
  - Notes that have taken by the agent
- Commands('/game.py') :
  - Speak command
  - Vote command
  - targeting/healing/killing/inquiring command
