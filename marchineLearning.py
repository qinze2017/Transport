import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from findCondition import faltList,getData
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

##Combine two dictionaries
def compare():
    frenquent_B = dict()
    frenquent_C = dict()
    
    fout1 = open("FileTrainWithR.label", "wt")
    fin1 = "FileTrain.label"
    
    dict1=getData(fin1,fout1,frenquent_B)
    
    fout2 = open("FileTestWithR.label", "wt")
    fin2 = "FileTest.label"
    dict2=getData(fin2,fout2,frenquent_C)
    
    return dict1,dict2,set([item for sublist in dict1.values() for item in sublist]) | set([item for sublist in dict2.values() for item in sublist])

##Return the train vector and test vector
def getResult(val):

    df_train = pd.DataFrame(faltList(val[0],val[2])).fillna(0).T
    ##print(df_train)
    ##print(df_train.shape)
    
    df_test = pd.DataFrame(faltList(val[1],val[2])).fillna(0).T
    ##print(df_test)
    ##print(df_test.shape)
    
    return df_train,df_test

def main():
    
    v,t = getResult(compare())
    
    ##Traing vectors
    traning_v = np.zeros(435)
    traning_v[249:435] = 1
    
    ##Use the Python Machine Learning Methodes
    ##Naive Bayes Classifier
    mod1 = MultinomialNB()
    mod2 = GaussianNB()
    mod3 = BernoulliNB()
    ##Training SVM 
    mod4 = LinearSVC()
    
    mod1.fit(v,traning_v)
    mod2.fit(v,traning_v)
    mod3.fit(v,traning_v)
    mod4.fit(v,traning_v)
    ##Testing vectors
    test_v = np.zeros(780)
    test_v[431:780] = 1
    
    ##Test with the Traing models
    res1 = mod1.predict(t)
    res2 = mod2.predict(t)
    res3 = mod3.predict(t)
    res4 = mod4.predict(t)
    ##print(train_matrix)
    ##print(test_matrix)
    print("MultinomialNB :")
    print("Multinomial NB | GOOD | BAD ")
    print(confusion_matrix(test_v,res1))
    ##Calculate the accuracy score
    print(accuracy_score(test_v, res1))
    
    print("GaussianNB :")
    print("Gaussian NB | GOOD | BAD ")
    print(confusion_matrix(test_v,res2))
    ##Calculate the accuracy score
    print(accuracy_score(test_v, res2))

    print("BernoulliNB :")
    print("Bernoulli NB | GOOD | BAD ")
    print(confusion_matrix(test_v,res3))
    ##Calculate the accuracy score
    print(accuracy_score(test_v, res3))
    
    print("SVM :")
    print("SVM | GOOD | BAD ")
    print(confusion_matrix(test_v,res4))
    ##Calculate the accuracy score
    print(accuracy_score(test_v, res4))

main()