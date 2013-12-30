from bs4 import BeautifulSoup
import urllib2, re, datetime, os

url='http://apod.nasa.gov/apod/'
response=urllib2.urlopen(url)
content=response.read()
response.close()
soup = BeautifulSoup(content)
url=url+str(re.search(r'"([A-Za-z0-9_\./\\-]*)"', str(soup.find_all('a')[1])).group())[1:-1]
#print url
response=urllib2.urlopen(url)
store = open ( str(datetime.date.today())+".jpg" , 'w')
store.write ( response.read())
store.close()
response.close()

os.system("sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db \"update data set value = '"+str(os.getcwd())+ "/" +str(datetime.date.today())+".jpg"+"'\";")
os.system("killall Dock")
