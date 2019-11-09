import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scraper import scrapedList
import numpy as np
from datetime import date
import csv

def evaluate(dateTime):

    input_dataset_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv")
    input_dataset_labels_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile_labels.csv")
    #print(input_dataset_frame)
    del input_dataset_frame['Unnamed: 0']

    X_train, X_test, y_train, y_test = train_test_split(input_dataset_frame, input_dataset_labels_frame, test_size=0.20, random_state=42)

    ML_Obj = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=100000)

    model = ML_Obj.fit(X_train, np.ravel(y_train)) # model now contains the ML

    dataset = []
    dayVal = dateTime.strftime("%d")
    monthVal = dateTime.strftime("%m")

    wileyScraped, wileyFoodScraped = scrapedList("https://dining.purdue.edu/menus/Wiley/2019/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    hillenbrandScraped, hillenbrandFoodScraped = scrapedList("https://dining.purdue.edu/menus/Hillenbrand/2019/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    windsorScraped, windsorFoodScraped = scrapedList("https://dining.purdue.edu/menus/Windsor/2019/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    fordScraped, fordFoodScraped = scrapedList("https://dining.purdue.edu/menus/Ford/2019/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")

    notableFoods = "Notables:\n||__Ford__: " + str(fordFoodScraped) + "\n\n"
    notableFoods += "__Wiley__: " + str(wileyFoodScraped) + "\n\n"
    notableFoods += "__Hillenbrand__: " + str(hillenbrandFoodScraped) + "\n\n"
    notableFoods += "__Windsor__: " + str(windsorFoodScraped) + "\n"
    notableFoods += "||"

    if fordScraped != None:
        dataset.append(fordScraped)
    else:
        dataset.append([0] * 25)

    if wileyScraped != None:
        dataset.append(wileyScraped)
    else:
        dataset.append([0] * 25)
    if hillenbrandScraped != None:
        dataset.append(hillenbrandScraped)
    else:
        dataset.append([0] * 25)
        
    if windsorScraped != None:
        dataset.append(windsorScraped)
    else:
        dataset.append([0] * 25)

    queryDataFrame = pd.DataFrame(dataset)
    queryDataFrame.columns = ['oge_chkn','ppc_chkn','tenders','pep_pizza','hamburg','shrimp','ML_Pizza','slop_jo','pasta','min_cornd','coulotte','clam_strip','cheese_rav', 'ML_pizza','SS_chkn',
                              'mac','fraldinha','wonton','popper','mac_pizza','fajita','tso_chkn','hamburg','mozz_stk','mac']


    queryDataFrame.to_csv(r'C:\Users\Andy\PycharmProjects\DiscordBot_Py\intermediary.csv')


    # output format: [{ford} {wiley} {hillenbrand} {windsor}]
    df_predict = model.predict(queryDataFrame)

    return (str(df_predict)), notableFoods