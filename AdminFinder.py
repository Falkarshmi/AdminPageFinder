# Admin Page Finder
# It is coded for fun, nothing more!. 
# HTTP.client offer more functionilities which you can use, so browse the page (https://docs.python.org/3/library/http.client.html) for further information.

import http.client
from termcolor import colored

admin_list = open('list.txt', "r")

url = input("please enter the url of the site and ensure not using HTTP or HTTPS, for example www.site.com : ")
print("Admin Pages Found are: ")
for x in admin_list:
      conn = http.client.HTTPConnection(url)
      # u can use http.client.HTTPSConnection for HTTPS connections.
      conn.request('GET', '/'+x.replace('\n', ''))
      url_connection = conn.getresponse()
      if url_connection.status == 200 or url_connection.status == 301:
         print (colored(url+'/'+x, 'green'))
 

