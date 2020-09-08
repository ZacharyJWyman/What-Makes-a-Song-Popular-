# Spotify Song Popularity
In this project we help artists follow music trends and form a predictive algorithm that can accurately predict song popularity. 
### To view notebook code:
Data Visualization: https://github.com/ZacharyJWyman/Spotify-API/blob/master/notebooks/Spotify_song_analysis%20(2).ipynb    
Machine Learning: https://github.com/ZacharyJWyman/Spotify-API/blob/master/notebooks/Spotify%20Machine%20Learning%20.ipynb  

## Table of Contents
* [About](#About)
* [Libraries](#Libraries)
* [Conclusion](#Conclusion)
* [Authors](#Authors)

## About
Music preferences change every year. Artists need to follow these trends to ensure that their next song will be popular with listeners. This project can help artists follow these music trends with ease and give them an insight into creating their next big hit. ***  Using the spotify API and spotipy, we were able to retrieve data on the current top 50 songs and found a dataset from **insert dataset here** for years 2010 - 2019. This data unfortunately did not come with all the desired factors and so some further steps had to be taken. Using the spotify API we were able to retrieve missing factors and clean up the dataset to proceed with analytics. This data allowed us to take an inside look at what factors were associated with song popularity in more recent years. To take the project a step further, we developed a model that predicts expected song popularity using data from **source**. A series of regression models were used to gain an initial estimate of the accuracy. Hypertuning each model using GridSearchCV helped eliminate some error and then both stacking and blending techniques were implemented. The purpose of this project is to identify factors that are associated with an increase in popularity. Having an idea of the music preference for each year can help artists increase the popularity of their songs to reach a wider audience. 

## Libraries
- Pandas, NumPy, sklearn, matplotlib, seaborn, spotipy, scipy.

## Findings
After gathering and cleaning the data:
** Austin write up analytics here** 

Initially our dataset had a skewed distribution for popularity. There were a fair distribution of songs that had 0 popularity and this caused a left-ward skew. To fix this, we only looked at data that had greater than 0 popularity and performed a log(1+X) transformation on popularity. Doing so gave us a fairly normal distribution which will be help the accuracy of our model. We can still see that there exists a high distribution of songs to the left, but we want to keep as much data as possible and already have a more normal looking bell curve after the transformation.  
  
![normalized_plot](https://user-images.githubusercontent.com/64059855/92413398-d42b6b80-f104-11ea-91ef-a8f9d381d2bf.png)
  
After normalizing the response variable we must take a look at the predictors To get the most accurate model we want to ensure that the skewness of numerical features are in the range -0.5 - 0.5. If not we will use a Box-Cox transformation to normalize, allowing more flexibility and increased accuracy. For our model, we perform Box-Cox transformations on speechiness, liveness, and instrumentalness.     
  
![skewness](https://user-images.githubusercontent.com/64059855/92413878-ea3a2b80-f106-11ea-9676-93043a1474a8.PNG)
  
A machine learning algorith does not take well to classifiers. Using One Hot Encoder, we categorized each categorical value into numericals, taking on the value 1 if it is true. This transformation adds a lot of columns to our dataframe, but it is a necessary step to ensure that we are achieving accurate outcomes. To proceed, we took a random sample (80%) from the data. Linear, Gradient Boosting, XGB, Ridge, and Random Rorest regressions were then used on this sample. The Random Forest regressor performed the best and so we initialized it as our meta regressor to be used in stacking, but first we needed to hypertune the parameters of each model. To do this, GridSearchCV was used on all of the models and determined the best estimator for each algorithm. We could now go ahead in stacking the models which reduced the RMSE by 0.05, a significant improvement over each base model. Additionally, blending was used to create a more robust model on top of stacking. This technique helped improve performance and increased accuracy, reducing RMSE over 0.1, making it the best performing model to predict song popularity. The figure below is a side-by-side illustration of model performance.      

![spotify_rmse](https://user-images.githubusercontent.com/64059855/92412702-bdcfe080-f101-11ea-802b-f7928ba9875b.png)

## Conclusion
* Achievements 

### What we learned:
In this project we gained familiarity working with a variety of regression and ensemble techniques. Originally, we wanted to paint it as a classification problem and while the model performed decently (considering 100 different classes), there were some issues on the tail ends. Using regression, we were able to gain a much better initial approximation. A common practice when considering the best parameters is ot use GridSearchCV and RandomizedSearchCV and this project gave us expertise in both. It also gave an opportunity to apply techniques commonly used in winning kaggle submissions. This being utilizing stacking and blending ensemble techniques. The RMSE of our model dropped significantly when applying blending. 

## Authors
Created by *Zachary Wyman & Austin Eaton*.  
Contact: zack.wyman1@gmail.com & 
