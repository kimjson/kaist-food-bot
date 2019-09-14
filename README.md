<!--
title: KAIST Food Bot
description: Telegram bot which pushes new posts of ARA(KAIST community site) Food board every 11 am.
layout: Doc
framework: v1
platform: AWS
language: Python
authorLink: 'https://github.com/steinkim'
authorName: 'Jaesung Kim'
authorAvatar: 'https://avatars0.githubusercontent.com/u/15705385?s=460&v=4'
-->
# Serverless Telegram Bot
Telegram bot which pushes new posts of ARA(KAIST community site) Food board every 11 am.

## Usage

### What do I need?
- A AWS key configured locally, see [here](https://serverless.com/framework/docs/providers/aws/guide/credentials/).
- NodeJS. I tested with v10.16.1.
- A Telegram account.

### Installing
```
# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install

# Get a bot from Telegram, sending this message to @BotFather
$ /newbot

# Put the token received into a file called serverless.env.yml, like this
$ cat serverless.env.yml
TELEGRAM_TOKEN: <your_token>

# Deploy it!
$ npm run deploy # development stage
$ npm run deploy:production # production stage

# With the URL returned in the output, configure the Webhook
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

Now, just start a conversation with the bot :)
