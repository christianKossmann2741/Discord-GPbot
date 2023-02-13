<div align="center">
  <h1>Discord GPbot</h1>
 </div>

## What its about

The Discord GPbot is a simple python application made for those who want to integrate an openai chatbot within Discord. It's very simple and straight forward.  
When called within a server, the bot will answer in character with its description (That can be defined at openYBSB.py) and it saves the conversation in "history.txt" for context. You can adjust the amount of context the API will use (Consider that your wallet may suffer the consequences).

## How to install

You will need to install 2 pip libraries before being able to run it. Those are "openai" (communicates with openai's API) and "discord" (communicates with discord's API). For that, you run the following commands:
<br>
If you are using mac or linux:

```bash
  sudo pip install openai
```

```bash
  sudo pip install discord
```

Or if you are using windows:

```bash
  pip install openai
```

```bash
  pip install discord
```

After that you will need to update the "apikey.txt" file to include your, openai API key. You will also need to create a discord bot with the correct permissions (It only needs to be able to answer) and get bot's token and put it in "discordBot.py" in the "token variable". After that you will only need to edit the AI's personality at "openYBSB.py" (It has a template there that you can follow).

### Some Useful Notes and warnings

As you can probably see, this is a very (VERY) simple application that is not very well optimized, so take this as a warning about bugs and unorthodox behavior. I would advise you to be very careful of the amount of context and history that you send to the AI, it can become very heavy and that would be very expensive. A final warning would be to be careful with your description and the way you talk to the AI, considering that it does not have a filter for content, so it can be a magnet for NSFW content (Wink wink)