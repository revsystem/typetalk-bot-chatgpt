# Typetalk bot using ChatGPT API

Create a [Typetalk](https://nulab.com/typetalk/) bot using OpenAI's ChatGPT API.

This Typetalk bot operate according to the following specifications.

- Follow the tone and answers according to the pre-defined character settings.
- Summarise the message as a start point of conversation in approximately 30 words and set tag.
- Create conversation flow by passing the part of conversation thread to the ChatGPT API each time you speak.
- The conversaton history pass to ChatGPT API limit latest four messages.
  - Because of the API sepcification that the maximum number of token is 4,096 for the conversation history,questions, and answers combined.
  - You can handle this bot specfication by changing `max_tokens` parameter of ChatGPT API and pre-defined character settings.

Wait a few seconds to receive a response from the ChatGPT API.
![Typetalk bot using ChatGPT API](https://github.com/revsystem/typetalk-bot-chatgpt/assets/17801281/79fe85de-560a-47dd-a6c4-dbba630d3925)

## Setup document

Japanese version is on [Qiita](https://qiita.com/revsystem/items/ac1d5e0111626755e647).

## Recommended System Requirements

- Python 3.11.3 (Python 3.9, 3.10 is also OK.)
  - bottle 0.12.25
  - openai 0.27.6
- ngrok 3.3.0

## Requirement API Keys or Tokens

### OpenAI API Key

Create [your OpenAI API account](https://beta.openai.com/signup) and [API Key](https://platform.openai.com/account/api-keys).

### Typetalk Token

Create [your Nulab account](https://apps.nulab.com/signup) and singin to the Nulab account from [Typetakl.com](https://typetalk.com/signin/redirect/nulab).

#### Create Typetalk bot

1. [Create a new topic](https://support.nulab.com/hc/en-us/articles/9096358253337)
1. [Add a bot and get Typetalki token](https://developer.nulab.com/docs/typetalk/#)
   1. Check both `API Scope`
   1. Not Check `Using Outgoing Webhook`
   1. After clicking on the `Create` button, you will receive a Typetalk Token on the bot detailed view.
1. Copy the Typetalk token from the bot detailed view, and paste it `TYPETALK_TOPIC_ID` in **const.py**.

### ngrok token

Create [your ngrok account](https://dashboard.ngrok.com/signup) and download ngrok binary, crate configuration file [following setup document](https://dashboard.ngrok.com/get-started/setup).
You can also download ngrok binary for each OS from [Install ngrok](https://ngrok.com/download) page.

## Setting environment variables

Add environment variables to your shell dotfile like `.zshrc`.

```shell
export OPENAI_API_KEY="yyyy"
export TYPETALK_TOKEN="xxxx"
```

Apply shell configuration.

```shell
exec $SHELL
```

## Installing Python Packages

```shell
pip install --upgrade pip
python3 -m pip install bottle openai requests
```

## Starting bottle

```shell
python3 index.py
```

```shell
Server Start
Bottle v0.12.25 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:8080/
Hit Ctrl-C to quit.
```

## Starting ngrok

I reccomend you to open this on the another console window or tab.

```shell
ngrok http 8080
```

```shell
Session Status                online
Account                       [YOUR EMAIL_ADDRESS] (Plan: Free)
Version                       3.3.0
Region                        Japan (jp)
Latency                       34ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://xxxx-xxx-xxx-xxx-xxx.ngrok-free.app -> http://localhost:8080
```
