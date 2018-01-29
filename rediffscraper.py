import re
import urllib2
from bs4 import BeautifulSoup
date=raw_input("Enter the date in (DD/MM/YYYY) format to view the headlines: ")
day,month,year=date.split('/')
print("Printing the headlines of "+date+" :")
page = urllib2.urlopen("http://www.rediff.com/issues/"+day+month+year[2:]+"hl.html")
soup = BeautifulSoup(page,'html.parser')
d=soup.find_all('div', attrs={'id': 'hdtab1'})
for x in d:
	y=x.find('a',attrs={'target': '_new'})
	print("-"+y.text[6:])
	y=x.find_all('a',attrs={'target': '_new','href': re.compile("http://www.rediff.com/news/")})	
	for z in y:
		print ("-"+z.text+z.nextSibling)#+z.nextElementSibling.nextSibling
