import pandas
import os
from dotenv import load_dotenv()

load_dotenv()
OUTPUTFILE_PATH = os.getenv('OUTPUTFILE_PATH')


dataFrame = pandas.DataFrame() #insert 2d array of new data here
dataFrame.to_csv(OUTPUTFILE_PATH, mode='a', header=False) # writes dataframe to file in append mode
