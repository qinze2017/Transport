Welcome to the ...

Order to execute programs:
1.getDataWithAPI.py -- automatic get Google API JSON data
2.searchData.py -- collection JSON useful data
3.findFileInfo.py -- build the file with keys
4.findCondition.py -- filter the data with conditions
5.marchineLearning.py -- Test with machine learning methods

File existed: 
bus_stops.txt -- 30 bus stations
bus_stops_test.txt -- 40 bus stations

File created:
TRAINNING folder -- it contains all training files
TESTING folder -- it contains all testing files
FileTrain.label -- exported by the program findFileInfo.py
FileTest.label -- exported by the program findFileInfo.py
------------------------------------------------------
Pertinent points

bus_stops.txt and bus_stops_test.txt, These files has been collected from the google map pages

------------------------------------------------------
The corpus description
The dataset:

-- JSON file

-- list, set and dict, vector

------------------------------------------------------
The result:

show the table :

With Naive Bayes Classifier:
0.5641025641025641
|Multinomial NB | GOOD | BAD | 
|     GOOD      | 379  | 52  |
|      BAD      | 288  | 61  |
0.5192307692307693
|  Gaussian  NB | GOOD | BAD | 
|     GOOD      | 379  | 52  |
|      BAD      | 288  | 61  |
0.5717948717948718
|  Bernoulli NB | GOOD | BAD | 
|     GOOD      | 379  | 52  |
|      BAD      | 288  | 61  |

With SVM:
0.5679487179487179
| SVM  | GOOD | BAD  | 
| GOOD | 361  | 70   |
| BAD  | 267  | 82   |

We have not got a good accuracy score here (perhaps the reason due to the number of TRAINNING files), 
A good document to understand the accuracy score, we could not say the accuracy is the higher, so the one is better. 
http://www.dataminingblog.com/what-is-a-good-classification-accuracy-in-data-mining/

We will understand better then do the improvement 

