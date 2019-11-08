import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scraper import scrapedList
import numpy as np
from datetime import date

def evaluate():

    input_dataset_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv")
    input_dataset_labels_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile_labels.csv")

    X_train, X_test, y_train, y_test = train_test_split(input_dataset_frame, input_dataset_labels_frame, test_size=0.20, random_state=42)

    ML_Obj = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=100000)

    model = ML_Obj.fit(X_train, np.ravel(y_train)) # model now contains the ML

    dataset = []
    today = date.today()
    dayVal = today.strftime("%d")
    monthVal = today.strftime("%m")
    print(dayVal)
    print(monthVal)
    dataset.append(scrapedList("https://dining.purdue.edu/menus/Wiley/2019/" +
                               monthVal.zfill(2) + "/" + dayVal.zfill(2) + "/Dinner"))
    dataset.append(scrapedList("https://dining.purdue.edu/menus/Windsor/2019/" +
                               monthVal.zfill(2) + "/" + dayVal.zfill(2) + "/Dinner"))
    dataset.append(scrapedList("https://dining.purdue.edu/menus/Hillenbrand/2019/" +
                               monthVal.zfill(2) + "/" + dayVal.zfill(2) + "/Dinner"))
    dataset.append(scrapedList("https://dining.purdue.edu/menus/Ford/2019/" +
                               monthVal.zfill(2) + "/" + dayVal.zfill(2) + "/Dinner"))

    queryDataFrame = pd.DataFrame(dataset)


    df_predict = model.predict(X_test) # df

    #print(X_test)

evaluate()