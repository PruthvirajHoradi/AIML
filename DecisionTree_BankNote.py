
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn import tree


def loadDataSet():
  Ir =pd.read_csv("BankNote_Authentication.csv")
  return Ir

def trainModel(Ir):
  clf = tree.DecisionTreeClassifier()
  clf = clf.fit(Ir.drop('class',axis = 'columns'), Ir['class'])
  return clf

def display(clf, Ir):
  plt.figure(figsize = (40,40))
  tree.plot_tree(clf, filled = True)
  plt.show()

Ir1 = loadDataSet()

#print (Ir1.feature_names)
#print (Ir1.target_names)


M = trainModel(Ir1)

display(M,Ir1)

