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

def render_latex(latex, dest_filename, output_format = 'png'):
	payload = {'code': latex, 'format': output_format}
	response = requests.post(HOST + '/api/v2', data = payload)
	response.raise_for_status()
	jdata = response.json()
	if jdata['status'] != 'success':
		raise Exception('Failed to render LaTeX')
	url = HOST + '/api/v2/' + jdata['filename']
	download_file(url, dest_filename)

#render_latex( LATEX, './out.pdf')