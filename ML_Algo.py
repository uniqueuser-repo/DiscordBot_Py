import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

input_dataset_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv")
input_dataset_labels_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile_labels.csv")

X_train, X_test, y_train, y_test = train_test_split(input_dataset_frame, input_dataset_labels_frame, test_size=0.20, random_state=42)

ML_Obj = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=100000)

model = ML_Obj.fit(X_train, np.ravel(y_train))
print(model.score(X_test, y_test))