# message logger by DJ::Ötzi, 2021

import discord
import json
import os
from datetime import datetime
from datetime import date

token = '' #add you token here

class MainClient(discord.Client):
    async def on_ready(self):
        print('Logged in: {0}!'.format(self.user))

    async def on_message(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        now_date = date.today()
        current_date = now_date.strftime("%d/%m/%Y");
        output = {
                   "Guild": '{0.guild}'.format(message),
                   "Channel": '{0.channel}'.format(message),
                   "Date": current_date,
                   "Time": current_time,
                   "Author": '{0.author}'.format(message),
                   "Content": '{0.content}'.format(message)
                 }
        outputasstr = json.dumps(output, indent=4)
        print('\n\n'+outputasstr)
        f = open("log.json", "a")
        f.write(outputasstr)
        f.write('\n\n')
        f.close()

client = MainClient()
client.run(token)
