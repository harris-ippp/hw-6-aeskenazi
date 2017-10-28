#!/usr/bin/env python
#since my e1 and e2 are not working correctly, I am unable to do this part completely.
#I have commented my understanding of this part based on the code Jamie provided in the hints and
#the information I googled
%matplotlib inline
import glob #this will allow me to get all the csv files into one dataframe
import pandas as pd
# The following source helped me with this code
#https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
path = #path of my files that do not exist because e1 and e2 are not working
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame() #create variable for the dataframe
list_ = [] #create empty list
frame.rename(inplace = True, columns = d) # rename to democrat/republican
frame.dropna(inplace = True, axis = 1)    # drop empty columns
frame["Year"] = 2004
for file_ in allFiles:
    df = pd.read_csv(file_,index_col = 0,
                   thousands = ",", skiprows = [1])
    list_.append(df) #append all the csvs into the empty list
frame = pd.concat(list_) #concatenate the list elements into one data frame

frame [["Democratic", "Republican", "Total Votes Cast", "Year"]] #select only these columns
frame.loc[:,"Republican Share"] = "Republican" / "Total Votes Cast" #create a new column in pandas
# source: https://stackoverflow.com/questions/41274332/pandas-creating-a-new-column

graph = frame["Republican Share"].plot(kind = "hist", bins = 24) #create a histogram of republican vote shares for
#each election year
#do this graph for each of the 5 counties indicated
