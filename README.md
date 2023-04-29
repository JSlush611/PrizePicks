# PrizePicks

Bot I created that scrapes the uses Reverse Engineering to scrape the PrizePicks website, 
and then cleanse and format this data to be analyzed. After this I continue to utilize Reverse
Engineering to scrape ESPN's large dataset and gather a wegihted average of a statistic for 
each player that has a statistic line made for them. This average in cludes the average of that player for the 
season, the average of that player in their last 7 games, and the average of that player over the 
last 3 games against the specific team that they are playing. It then calculates the difference between
the predicted value, and the PrizePicks statistic line and returns the values with the biggest differences
(the statistically most likely lines to hit). 
