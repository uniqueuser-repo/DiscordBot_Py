import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

input_dataset_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv")
input_dataset_labels_frame = pd.read_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile_labels.csv")

X_train, X_test, y_train, y_test = train_test_split(input_dataset_frame, input_dataset_labels_frame, test_size=0.20, random_state=42)

ML_Obj = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
ML_Obj.fit(X_train, y_train)
ML_Obj.score(X_test, y_test)