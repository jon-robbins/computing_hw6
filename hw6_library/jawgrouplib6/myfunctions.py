import pandas as pd
from sklearn.model_selection import train_test_split


# loads the data and returns two dataframes, one for train and another for test.
class DataLoadUtil:

    def __init__(self):
        pass

    def loadData(self, path, filename):
        df = pd.read_csv(path + filename, sep=',')
        SEED = 0
        features = df.columns.drop('diabetes_mellitus')
        X = df.loc[:, features]
        y = df.loc[:, 'diabetes_mellitus']
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=SEED, train_size=.90)
        X_train['diabetes_mellitus'] = y_train
        X_test['diabetes_mellitus'] = y_test
        self.trainDataSet = X_train
        self.testDataSet = X_test


##removes those rows that contain NaN values in the columns: age,gender, ethnicity.
class NanDropUtil:

    def __init__(self):
        pass

    def dropNan(self, dataFrame):
        dataFrame = dataFrame.dropna(axis=0, subset=['age', 'gender', 'ethnicity'])
        return dataFrame


##fills NaN with the mean value of the column in the columns
class NanFillMeanUtil:

    def __init__(self):
        pass

    def fillNanMean(self, dataFrame):
        dataFrame.loc[dataFrame["height"].isna(), "height"] = dataFrame["height"].mean()
        dataFrame.loc[dataFrame["weight"].isna(), "weight"] = dataFrame["weight"].mean()
        return dataFrame


##two feature classes that transform some of the columns in the data set.
##These feature classes need to have the same structure defined by an abstract parent class
from abc import ABCMeta, abstractmethod


class DataTransUtil(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def dataTrans(self):
        pass


class genderTrans(DataTransUtil):
    def __init__(self):
        pass

    def dataTrans(self, dataFrame):
        dataFrame['gender'] = [0 if x == 'M' else 1 for x in dataFrame['gender']]
        return dataFrame


class icuStayTypeTrans(DataTransUtil):
    def __init__(self):
        pass

    def dataTrans(self, dataFrame):
        dataFrame['icu_stay_type'] = [0 if x == 'admit' else x for x in dataFrame['icu_stay_type']]
        dataFrame['icu_stay_type'] = [1 if x == 'readmit' else x for x in dataFrame['icu_stay_type']]
        dataFrame['icu_stay_type'] = [2 if x == 'transfer' else x for x in dataFrame['icu_stay_type']]
        return dataFrame


from sklearn.linear_model import LogisticRegression
import numpy as np


class modelClass:

    def __init__(self, features, target, hyperparameters):
        self.__features = features
        self.__target = target
        self.__hyperparameters = hyperparameters
        self.model = LogisticRegression()
        pass

    def train(self, dataset):
        X_train = dataset.loc[:, self.__features]
        y_train = dataset.loc[:, self.__features]
        self.model.fit(X_train, y_train)

    def predict(self, dataset):
        X_test = dataset.loc[:, self.__features]
        y_test_pred = np.squeeze(self.model.predict_proba(X_test)[:, 1])
        return y_test_pred


# test
# du = DataLoadUtil()
# du.loadData('','sample_diabetes_mellitus_data.csv')
# dnu = NanDropUtil()
# df = dnu.dropNan(du.trainDataSet)
# nfmu = NanFillMeanUtil()
# df = nfmu.fillNanMean(df)
# ist = icuStayTypeTrans()
# df = ist.dataTrans(df)
# df.icu_stay_type.unique()