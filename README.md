# Telegram Bot

This BOT is made for sending alert from SIEM to Telegram!

## How to use

Using the docker image, and run it with the mounted `.env` file.

```bash
# for bash
$ docker run -v `pwd`/.env:/app/.env -p <host_port>:80 \
  ghcr.io/kunniii/telegram_alert_bot
```

```fish
# for fish
$ docker run -v (pwd)/.env:/app/.env -p <host_port>:80 \
  ghcr.io/kunniii/telegram_alert_bot
```
