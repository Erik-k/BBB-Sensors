#{ 
Plots the data from the cosmic ray detector as a histogram
Cosmic ray hit data must be saved as YYYYMMDD.mat, and inside
that file is a column of number of hits per hour for 24 hours.
Created 2 March 2016 by Erik Knechtel
#}

clear all;

# We are actually always going to graph YESTERDAYS data
today=datestr(now-1, 'yyyymmdd');
# strcat doesnt preserve trailing white spaces so have to use []
todaysgraphtitle = ['Cosmic Ray Hits on ', datestr(now-1, 'dd-mmm-yyyy')];
todaysfilename = strcat(today,'.mat');
todaysimagename = strcat(today,'.jpg');

todays_hits = load(todaysfilename);
bar(todays_hits)
title(todaysgraphtitle);
ylabel('Number of hits');
xlabel('Hour in the day');
print(todaysimagename);
