from webex_bot.webex_bot import WebexBot
import os
from GPT import GPT


#Input your webex_bot token
webex_token = ""
#Input your company domain name so that only user in the domain can access this bot, ex: cisco.com
#bot = WebexBot(webex_token, approved_domains = ["cisco.com"])
bot = WebexBot(webex_token)
bot.add_command(GPT())
bot.run()
