from collections import defaultdict
import pandas as pd

allRatings = []
userRatings = defaultdict(list)

data = pd.read_csv('./data/train.csv')

allRatings = data['overall'].to_list()

for index_ in data.index:
    userID = data.loc[index_,'reviewerID']
    rating = data.loc[index_,'overall']
    userRatings[userID].append(rating)

globalAverage = sum(allRatings)/len(allRatings)
userAverage = {}
for u in userRatings:
    userAverage[u] = sum(userRatings[u]) / len(userRatings[u])

predictions = open('rating_predictions.csv', 'w')
for l in open('./data/rating_pairs.csv'):
    if l.startswith('userID'):
        #header
        predictions.write(l)
        continue
    u,p = l.strip().split('-')
    if u in userAverage:
        
        predictions.write(u + '-' + p + ',' + str(round(userAverage[u])) + '\n')
    else:
        predictions.write(u + '-' + p + ',' + str(round(globalAverage)) + '\n')