# Importing Modules
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
import asyncio
import random
import scrungle_sounds.sperrmann
import pygame
import os
from tts_test import play_tts

# Main connections/Constants
APP_ID = scrungle_sounds.sperrmann.sperrmann1 # Twitch Dev ID
APP_SECRET = scrungle_sounds.sperrmann.sperrmann2 # Twitch Dev Secret
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_BROADCAST]
TARGET_CHANNEL = '' # Channel Name here


#-------------------------------------
#Simple Commands for testing
async def lurk_command(cmd: ChatCommand):
    await cmd.reply("Thank you for choosing to stay with us. We hope you are having a good time. - Yesman Scrungle")

async def hydrate_command(cmd: ChatCommand):
    await cmd.reply("User has been requested to drink fluids! - Yesman Scrungle")

#-------------------------------------
#test tts
async def tts(cmd: ChatCommand):
    if cmd.parameter: # Chatmessage
        play_tts(cmd.parameter)
    else:
        await cmd.reply("This is empty! Please write something after the testcode! - Yesman Scrungle")

#-----------------------------------------------------------------------------------------------------------------
#
# MAIN BOT - :)
#
# Listen for message
async def on_message(msg : ChatMessage):
    #Print username and Chat Message
    print(f'{msg.user.display_name} - {msg.text}')

async def on_ready(ready_event: EventData):
    # Connect to channel
    await ready_event.chat.join_room(TARGET_CHANNEL)

    #Print ready Message
    print("TTS Bot ready")

#Bot setup
async def run_bot():
    #Authenticate app
    bot = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(bot, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await bot.set_user_authentication(token, USER_SCOPE, refresh_token)

    # initialize chat class
    chat = await Chat(bot)

    # Register Events
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    # Register COMMANDS
    chat.register_command("lurk", lurk_command)
    chat.register_command("hydrate", hydrate_command)
    chat.register_command("tts_test", tts)

    #Start bot
    chat.start()

    try:
        input(" !!press ENTER to stop!! \n")
    finally:
        chat.stop()
        print("Shift over. See you next time.")
        await bot.close()

asyncio.run(run_bot())

#---------------------------------------------------------------------------------------------------------------------
