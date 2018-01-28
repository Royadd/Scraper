import re
import urllib2
from bs4 import BeautifulSoup
date=raw_input("Enter the date in (DD/MM/YYYY) format to view the headlines: ")
day,month,year=date.split('/')
page = urllib2.urlopen("http://www.rediff.com/issues/"+day+month+year[2:]+"hl.html")
soup = BeautifulSoup(page,'html.parser')
x=soup.find_all('a',attrs={'target': '_new','href': re.compile("http://www.rediff.com/news/")})
print("Printing the headlines of "+date+" :")
for y in x:
	headline=y.text
	print (headline+"\n")