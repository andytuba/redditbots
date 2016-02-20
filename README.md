#Setup
Run ./setup.sh

#Add new bots
1. `mkdir someRelatedBots && cp example/example.py someRelatedBots/specificBot.py`
1. Edit `someRelatedBots/specificbot.py` and rename `ExampleRedditBot` to `SpecificBot`
1. Edit `SpecificBot.main` to do something

#Run bot
`source bin/activate; python someRelatedBots/specificbot.py`
