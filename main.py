import os
import discord
import requests
import shutil

HOST = 'https://rtex.probablyaweb.site'
LATEX = r'''
\documentclass{article}
\begin{document}
\pagenumbering{gobble}
\section{Hello, World!}
This is \LaTeX!
\end{document}
'''

def download_file(url, dest_filename):
	response = requests.get(url, stream = True)
	response.raise_for_status()
	with open(dest_filename, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)

def render_latex(output_format, latex, dest_filename):
	payload = {'code': latex, 'format': output_format}
	response = requests.post(HOST + '/api/v2', data = payload)
	response.raise_for_status()
	jdata = response.json()
	if jdata['status'] != 'success':
		raise Exception('Failed to render LaTeX')
	url = HOST + '/api/v2/' + jdata['filename']
	download_file(url, dest_filename)

#render_latex('pdf', LATEX, './out.pdf')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

client.run(os.environ['TOKEN'])
