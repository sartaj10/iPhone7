import requests, time
from bs4 import BeautifulSoup
import os
import webbrowser

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

while 1:
	r = requests.get('http://www.apple.com/us/shop/goto/iphone_7/select')
	html_doc = r.text

	soup = BeautifulSoup(html_doc, 'html.parser')

	if soup.find_all("img", alt= "We'll be back soon"):
		print "Yes"
	else:
		notify(	title    = 'Launched',
       			subtitle = 'iPhone 7',
       			message  = 'iPhone 7 launched!')
		webbrowser.open('http://www.apple.com/us/shop/goto/iphone_7/select')
		print "No"
