# Spotify Song Popularity
In this project we identify factors that are more likely to make a song popular and develop a model to predict popularity.
## Table of Contents
* [About](#About)
* [Libraries](#Libraries)
* [Conclusion](#Conclusion)
* [Authors](#Authors)

## About
Song preferences are changing every year. ***  Using the spotify API and spotipy, we were able to retrieve data on the current top 50 songs and found a dataset from **insert dataset here** for years 2010 - 2019. This data unfortunately did not come with all the desired factors and so some further steps had to be taken. Using the spotify API we were able to retrieve missing factors and clean up the dataset to proceed with analytics. This data allowed us to take an inside look at what factors were associated with song popularity in more recent years. To take the project a step further, we developed a model that predicts expected song popularity using data from **source**. A series of regression models were used to gain an initial estimate of the accuracy. Hypertuning each model using GridSearchCV helped eliminate some error and then both stacking and blending techniques were implemented. The purpose of this project is to identify factors that are associated with an increase in popularity. Having an idea of the music preference for each year can help artists increase the popularity of their songs to reach a wider audience. 

## Libraries
- Pandas, NumPy, sklearn, matplotlib, seaborn, spotipy, scipy.

## Findings
After gathering and cleaning the data:
** Austin write up analytics here** 

Initially our dataset had a skewed distribution for popularity. There were a fair distribution of songs that had 0 popularity and this caused a left-ward skew. To fix this, we only looked at data that had greater than 0 popularity and performed a log(1+X) transformation on popularity. Doing so gave us a fairly normal distribution which will be help the accuracy of our model. We can still see that there exists a high distribution of songs to the left, but we want to keep as much data as possible and have a more normal looking bell curve after the transformation is done.    
  
![normalized_plot](https://user-images.githubusercontent.com/64059855/92413398-d42b6b80-f104-11ea-91ef-a8f9d381d2bf.png)
  
After normalizing the repsonse variable we must take a look at the predictors To get the most accurate model we want to ensure that the skewness of numerical features are in the range -0.5 - 0.5. If not we will use a Box-Cox transformation to normalize, allowing more flexibility and increased accuracy. For our model, we perform Box-Cox transformations on speechiness, liveness, and instrumentalness.     
  
![skewness](https://user-images.githubusercontent.com/64059855/92413878-ea3a2b80-f106-11ea-9676-93043a1474a8.PNG)
  
After normalizing the data, we took a random sample (80%) from the data. To get an initial estimate, Linear, Gradient Boosting, XGB, Ridge, and Random Rorest regressions were used. The Random Forest regressor performed the best and so we initialized it as our meta regressor when stacking. Before stacking, GridSearchCV was used on all of the models to hypertune and determine the best estimators for each algortihm. Stacking the models reduced the RMSE by 0.05 which is a significant improvement over our base models. 





![spotify_rmse](https://user-images.githubusercontent.com/64059855/92412702-bdcfe080-f101-11ea-802b-f7928ba9875b.png)

## Conclusion

## Authors
Created by *Zachary Wyman & Austin Eaton*.  
Contact: zack.wyman1@gmail.com & 
