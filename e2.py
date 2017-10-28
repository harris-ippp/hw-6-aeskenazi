#!/usr/bin/env python

#although my e1.py is not set up correctly, I am attempting to write code for e2 and e3, although they will not work
import requests
from bs4 import BeautifulSoup as bs

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr) #download url
html = resp.content #look at the html content of that url
soup = bs(html, "html.parser") #use beautiful soup to scrape the html content

csv_list = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
for line in open("IDelection"):
    csv_list.append(IDelection)[0][1][2][3][4] #add all 5 indexes of the election ID to the csvlist.
    #I don't know how to add the ids to the {} part of the url specifically

file_name = Year +".csv" #name the csv file Year + csv. This won't work for mine because the years are all printing as 1924
with open(file_name, "w") as out:
  out.write(resp.text) #download the csv file 
