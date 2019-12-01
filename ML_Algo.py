import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scraper import scrapedList
import numpy as np
from dotenv import load_dotenv
from datetime import date
import csv
from dotenv import load_dotenv
import os
import ast

load_dotenv()

OUTPUTFILE_PATH = os.getenv('OUTPUTFILE_PATH')
OUTPUTFILE_LABELS_PATH = os.getenv('OUTPUTFILE_LABELS_PATH')
INTERMEDIARY_PATH = os.getenv('INTERMEDIARY_PATH')
ONGOING_LIST = os.getenv('ONGOING_LIST')

def checkCache(dataset, to_feed, to_feed_notables, dateTime):
    counter = 0
    for index, row in dataset.iterrows():  # first, check if the specified date is cached
        if (counter == 4):                 # break when 4 of the dining courts have been added to to_feed
            break

        element = ast.literal_eval(row['0']) # take the retrieved row (which is a String of a list) and convert it into a list, held in 'element'

        if str(element[0]).zfill(2) + "/" + str(element[1]).zfill(2) + "/" + str(element[2]).zfill(2) == dateTime.strftime("%Y/%m/%d"): # if the cached row's date is the same as the specified date's dateTime object
            counter = counter + 1
            if (element[3][0] != None):
                to_feed.append(element[3][0])
                to_feed_notables.append(element[3][1])
            else:
                to_feed.append([0] * 25)
                to_feed_notables.append("The dining court appears to be closed.")

    return counter

def evaluate(dateTime):
    input_dataset_frame = pd.read_csv(OUTPUTFILE_PATH)
    input_dataset_labels_frame = pd.read_csv(OUTPUTFILE_LABELS_PATH)

    del input_dataset_frame['Unnamed: 0']

    X_train, X_test, y_train, y_test = train_test_split(input_dataset_frame, input_dataset_labels_frame, test_size=0.20,
                                                        random_state=42)

    ML_Obj = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=100000)

    model = ML_Obj.fit(X_train, np.ravel(y_train))  # model now contains the ML

    dayVal = dateTime.strftime("%d")
    monthVal = dateTime.strftime("%m")
    yearVal = dateTime.strftime("%Y")

    dataset = pd.read_csv(ONGOING_LIST)
    to_feed = []
    to_feed_notables = []

    counter = checkCache(dataset, to_feed, to_feed_notables, dateTime)  # if counter == 0, date not in cache. if anything else, date in cache.

    if (counter == 0): # if the counter is 0, that is to say, the specified date wasn't cached, scrape from site.
        wileyScraped, wileyFoodScraped = scrapedList(
            "https://dining.purdue.edu/menus/Wiley/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(
                dayVal).zfill(
                2) + "/Dinner")
        hillenbrandScraped, hillenbrandFoodScraped = scrapedList(
            "https://dining.purdue.edu/menus/Hillenbrand/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(
                dayVal).zfill(
                2) + "/Dinner")
        windsorScraped, windsorFoodScraped = scrapedList(
            "https://dining.purdue.edu/menus/Windsor/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(
                dayVal).zfill(
                2) + "/Dinner")
        fordScraped, fordFoodScraped = scrapedList(
            "https://dining.purdue.edu/menus/Ford/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(
                dayVal).zfill(
                2) + "/Dinner")
        notableFoods = "Notables:\n||__Wiley__: " + str(wileyFoodScraped) + "\n\n"
        notableFoods += "__Hillenbrand__: " + str(hillenbrandFoodScraped) + "\n\n"
        notableFoods += "__Windsor__: " + str(windsorFoodScraped) + "\n\n"
        notableFoods += "__Ford__: " + str(fordFoodScraped) + "||\n"

        if wileyScraped != None:
            to_feed.append(wileyScraped)  # if the dining court was NOT closed,
            # append the set of scraped foods to to_feed (may be the empty set of all 0s)
        else:
            to_feed.append([0] * 25)  # if the dining court was closed, append set of empty foods to to_feed

        if hillenbrandScraped != None:
            to_feed.append(hillenbrandScraped)  # if the dining court was NOT closed,
            # append the set of scraped foods to to_feed (may be the empty set of all 0s)
        else:
            to_feed.append([0] * 25)  # if the dining court was closed, append set of empty foods to to_feed

        if windsorScraped != None:
            to_feed.append(windsorScraped)  # if the dining court was NOT closed,
            # append the set of scraped foods to to_feed (may be the empty set of all 0s)
        else:
            to_feed.append([0] * 25)  # if the dining court was closed, append set of empty foods to to_feed

        if fordScraped != None:
            to_feed.append(fordScraped)  # if the dining court was NOT closed,
            # append the set of scraped foods to to_feed (may be the empty set of all 0s)
        else:
            to_feed.append([0] * 25)  # if the dining court was closed, append set of empty foods to to_feed
    else:
        notableFoods = "Notables:\n||__Wiley__: " + str(to_feed_notables[0]) + "\n\n"  #
        notableFoods += "__Hillenbrand__: " + str(
            to_feed_notables[1]) + "\n\n"  # Create string with list of notable foods
        notableFoods += "__Windsor__: " + str(
            to_feed_notables[2]) + "\n\n"  # for printing by the bot to the server later
        notableFoods += "__Ford__: " + str(to_feed_notables[3]) + "||\n"  #

    queryDataFrame = pd.DataFrame(to_feed) # turn the to_feed list into a DataFrame
    queryDataFrame.columns = ['oge_chkn', 'ppc_chkn', 'tenders', 'pep_pizza', 'hamburg', 'shrimp', 'ML_Pizza',
                              'slop_jo', 'pasta', 'min_cornd', 'coulotte', 'clam_strip', 'cheese_rav', 'ML_pizza',
                              'SS_chkn',
                              'mac', 'fraldinha', 'wonton', 'popper', 'mac_pizza', 'fajita', 'tso_chkn', 'hamburg',
                              'mozz_stk', 'mac']

    queryDataFrame.to_csv(INTERMEDIARY_PATH)

    # output format of df_predict: [{wiley} {hillenbrand} {windsor} {ford}]

    df_predict = model.predict(queryDataFrame)  # find the labels (score) for each row (unique dining court), store in df_predict

    return (str(df_predict)), notableFoods
