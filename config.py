#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5555072872:AAHNmg5SiV9pgiRCa6Lr8QrSS1yFtkfh0jg")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "2936024"))
    API_HASH = os.environ.get("API_HASH", "9ca52986a5251713d12d91a0572bfd05")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1112368404").split())
    
