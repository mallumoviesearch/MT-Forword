#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 14623143))
    API_HASH = os.environ.get("API_HASH"‚ 51ee2679d47d66aed5795876afc67622)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5203617191:AAGinursk7k3AA9vVcCIJFJSwdG_u48qYTU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@mdfilechannel")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 2119484425)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001694632094))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
