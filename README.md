# Amazon Music Recommendation Kaggle Competition

## Background

For this project, we are responsible to complete a Kaggle competition. Each team will build a recommender system model to make predictions related to Amazon Music Reviews. eACH team will be required to complete a project report on their work in the form of a consulting report, as well as a final presentation.

[link to Kaggle](https://www.kaggle.com/c/mie1624winter2021/)

## Dataset:

**train.csv.zip** 150,000 reviews to be used for training. It is not necessary to use all ratings for training, for example, if doing so proves too computationally intensive.

- **reviewerID** The ID of the user. This is a hashed user identifier from Amazon.

- **itemID** The ID of the item. This is a hashed product identifier from Amazon.

- **reviewText** The text of the review.

- **summary** A short summary of the review.

- **overall** The star rating of the user’s review from 1 to 5.

- **reviewHash** Hash of the review (essentially a unique identifier for the review).

- **unixReviewTime** Time of the review in seconds since 1970.

- **reviewTime** Plain-text representation of the review time.

- **category** Category labels of the product being reviewed.

**test.csv.zip** 20,000 reviews to be used for generating the final Kaggle submission. All fields are the same as in train.csv.zip with the exception of the overall rating removed.

**rating_pairs.csv** Pairs (reviewerIDs and itemIDs) on which you are to predict ratings.

**baseline.py** A simple baseline that computes a user average and global average on training data then uses this to make predictions on test data. This code is given to demonstrate how to properly format predictions for uploading to Kaggle. A submission made with this code corresponds to the ‘naive baseline‘ submission on the leaderboard.

[link to Kaggle](https://www.kaggle.com/c/mie1624winter2021/)

## Dataset Overview:

1. Number of Ratings by Category
   ![Number of Ratings by Music Category](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/rating_vs_category.png)

   ![Image category by star rating](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/category_vs_star.png)

2. Word Cloud

![High Star Word Cloud](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/high_star_wordcloud.png)

![Low Star Word Cloud](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/low_star_wordcloud.png)

3. Word Frequency
   ![Word Frequency](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/most_frequent.png)

## Result

We tested differenet data engineering methods and used various traditional machine learning algorithms, below is a sample result. More details please check jupyter notebook.

TF vs IDF vs N-gram
![Result](https://raw.githubusercontent.com/jackychencw/Amazon-Music-Recommendation-System/main/src/imgs/train_result_by_cate.png)
