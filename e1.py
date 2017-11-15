#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr) #download url
html = resp.content #look at the html content of that url
soup = bs(html, "html.parser") #use beautiful soup to scrape the html content
rows = soup.find_all("tr", "election_item") #find all tags with class "election_item"
Year = [] #create empty list for Years
for row in rows:
    Year.append(row.contents[1].text) #search rows and append all the years (in index 1) to the Year list

IDelection = [] #create empty list of IDelection

for i in range(len(rows)):
    IDelection.append(rows[i]["id"][-5:]) #put the election IDs (the last 5 numbers) into the IDelection list

#print(Year, IDelection)
    ### TA: This is all inside the loop! you do all this  per each row
    with open('IDelection','w') as IDelection_file: #write an ID election file
            with open('Year','w') as Year_file: #write a year file
                for number in IDelection:
                    ### TA: In the line below, why are you only selecting certain characters from the number and year?
                    IDelection_file.write(number[0] + ' ' + number[4]) #add election IDs to IDelection file
                for line in Year:
                    Year_file.write(line[0] + ' ' + line[3]) #add years to Year file
                ### TA: You were supposed to write both the ID and the year to the same file
                ### The way you could have been doing that is by instead of doing a for over the elements of IDelection and Year
                ### Making a for loop over the range of the length of either of those, and then using that as an index
                ### so that you can loop around both at the same time.
    print(number, line) #this prints all the election IDs but then prints the same year (1924) over and over again next to them
    #I have tried adjusting the indents and moving the loops around but it still is not working
    #I also tried making one with statement that included IDelection and Year and got an error that said I needed an integer, not a string

### TA: if you comment the block above and instead you do this, you get what you wanted
'''
with open('IDelection','w') as IDelection_file: #write an ID election file
    for index in range(0,len(IDelection)):
        IDelection_file.write(IDelection[index] + ' ' + Year[index] + '\n') #'\n' is for a new line
        print(IDelection[index], Year[index])
'''

'''
with open('IDelection' , 'Year' , 'w') as IDelection_Year_file:
    for row in IDelection_Year_file:
        IDelection_Year_file.write(number[0] + ' ' + number[9])
        Year_file.write(line[0] + ' ' + line[3])
    print(number, line)
'''
