# Player Types From Box Score Production

In this simple script I used the KMeans clustering algorithm to assign players to groups based on the rate at which they accumulate Fantasy Points in 5 separate categories. 

The underlying theory was that teams vary in their ability to depress output in each category. I later built a model to predict a player's expected Fantasy Points that incorporated their opponent's "Defense Against Player Type" that was computed using the KMeans labels assigned using this model.

As it turns out, a Gaussian Mixture Model did a better job of clustering players due to the nature of the variance of production within each category. In other words, this model turned out to be useful, but it was a first try. It has been improved upon.

