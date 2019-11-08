import pandas

dataFrame = pandas.DataFrame() #insert 2d array of new data here
dataFrame.to_csv(r'C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv', mode='a', header=False) # writes dataframe to file in append mode