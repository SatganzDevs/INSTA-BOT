import sys
import time


# Import instabot library
from instabot import Bot



# Create a variable bot.
bot = Bot()
bot.login(username="muhamatpatihuzzikri",password="zikri2011")

bot.unfollow_non_followers()