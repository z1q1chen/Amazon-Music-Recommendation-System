# MIE1624_Course_Project_Group19
## Background
For this project, we are responsible to complete a Kaggle competition. Each team will build a recommender system model to make predictions related to Amazon Music Reviews. eACH team will be required to complete a project report on their work in the form of a consulting report, as well as a final presentation.

## Deadline
Submission deadline: April 4, 2021. Presentations are on April 6, 6:00-9:00pm during lecture time via Bb Collaborate.

## Submission:
You will need to submit a Jupyter notebook with your code, a report and your presentation slides through Quercus. Kaggle submissions will be made through the provided link. You will also be required to provide the code used.

[Kaggle Dataset](https://www.kaggle.com/c/mie1624winter2021/)

## Dataset:
**train.csv.zip** 150,000 reviews to be used for training. It is not necessary to use all ratings for training, for example, if doing so proves too computationally intensive.
   **reviewerID** The ID of the user. This is a hashed user identifier from Amazon.
   **itemID** The ID of the item. This is a hashed product identifier from Amazon.
   **reviewText** The text of the review.
   **summary** A short summary of the review.
   **overall** The star rating of the user’s review from 1 to 5.
   **reviewHash** Hash of the review (essentially a unique identifier for the review).
   **unixReviewTime** Time of the review in seconds since 1970.
   **reviewTime** Plain-text representation of the review time.
   **category** Category labels of the product being reviewed.
**test.csv.zip** 20,000 reviews to be used for generating the final Kaggle submission. All fields are the same as in train.csv.zip with the exception of the overall rating removed.
**rating_pairs.csv** Pairs (reviewerIDs and itemIDs) on which you are to predict ratings.
baseline.py A simple baseline that computes a user average and global average on training data then uses this to make predictions on test data. This code is given to demonstrate how to properly format predictions for uploading to Kaggle. A submission made with this code corresponds to the ‘naive baseline‘ submission on the leaderboard.

Please do not try to collect these reviews from Amazon, or to reverse-engineer the hashing function we used to anonymize the data. Doing so will not make it easier to successfully complete the project. **We will require a working code for all submissions to ensure no violation of the competition rules.**

[Kaggle Dataset](https://www.kaggle.com/c/mie1624winter2021/)
