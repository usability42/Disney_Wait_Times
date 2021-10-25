# Time Series Analysis of Rides at Disney's Animal Kingdom

### Exploratory Statement
---
Almost every Disney guest looks forward to their vacation, but no one relishes spending their vacation in assorted lines, queues, and waits (oh my!).  As Disney gradually increases its capacity after covid, wait times are likely to increase.  Although waits have decreased during covid, due to social distancing measures, they haven't decreased as much as some visitors hoped.

Disney sharply increased their ticket prices and annual passes recently.  In addition, whereas Disney once included 3 "Fast Passes" per day spent at the park to all guests, now everyone must pay to jump the line.  Worse, there are two different types of passes.  To my understanding, some rides only accept one, some the other, and some accept both.  Disney, I love you, but this is a serious #UXFail that your park employees will despise.

### Executive Summary
---
Given increased pricing, guests want to maximize their stays.  Minimizing time in lines is crucial.  People want a strategy without coughing up another $50-$75 per day to eschew lines.

The goal is to listen to the voice of the customer; of course, I am also a potential customer.

Disney guests invest a lot of money in their vacations.  In addition to park admission, our top customers usually are paying for airfare, accommodations, meals, and often some ground transportation.  While I don't personally know how much Disney earns on merchandise sales, the sheer number of shops at the parks indicates that they must be doing pretty well.

**1. Data Source**
My data are not actually my data.  They come from https://touringplans.com/walt-disney-world/crowd-calendar#DataSets.  According to information on the web site, a woman somewhere claims to have compiled wait times for over a dozen Disney attractions dating back to at least 2015.

I'm limiting the scope of this project to the rides in highest demand at Animal Kingdom, namely Na'vi River Journey, Flight of Passage, Kiliminjaro Safaris, and Expedition Everest.  The first two are part of Pandora, the world of Avatar.  Expedition Everest is a roller coaster that goes forwards and backwards.  Kiliminjaro Safaris riders ride in a safari vehicle among free(ish) roaming animals.

**2. Data Dictionary**
The data had only a few fields:
- Date
- Datetime
- SPOSTMIN - posted waiting time in minutes at ride entrance
- SACTMIN - actual waiting time in minutes

Additionally, I calculated myriad fields to handle reindexing, daily average wait times, weekly average wait times, and more.  All of them are derived from the features above.


**3. My Goal & Methodology**
Create a model that predicts a ride's waiting time within a few minutes in either direction.  I will be using time series models, likely SARIMAX to account for the seasonality inherent with tourism-dependent businesses.  My questions:  Are rides busier at certain times of the day, perhaps after meal times?  Are some days of the week significantly better than others?  Aside from Disney's blockout dates for cast members and lower-level pass holders, should certain weeks be avoided?

**4. Exploratory Data Analysis**
During exploratory data analysis, I discovered that Disney's seasonality arguably is like no other.  Some ride wait times fluctuate wildly, but not predictably, during the day.  Overall, Tuesdays and Wednesdays have lower wait times than Saturdays, but in concrete terms (i.e. in terms of legs standing on concrete), the differences weren't very meaningful.  Under the new pay not to stand in line plan, it boils down to whether waiting an extra 5-10 minutes will prompt a guest to purchase a pass.  If a ride wait is 300 minutes, waiting 10 more minutes is likely moot.  But on the other side, would someone pay $15 to wait 10 minutes instead of 20?  I'm sure Disney has crunched those numbers; I'm sure they're betting on them.  But how do guests hack the system?  With everyone booking their rides on the day of their visit, how can visitors plan ahead?  Even annual passholders have to make reservations to visit the park, in addition to their annual passes.  Reservations are free; they just limit the total number of park guests.  But annual passholders have a limited number of reservations per year.  Gone are the days of dropping by for the afternoon or booking free fast passes ahead of time.  Passholders must plan.

And everyone has to get up early to make those precious reservations, since they've gone Southwest-style.  Resort guests can begin reserving lane skipping at 7am on the day of park visits.  Everyone else must wait until the park opens.

Oh, the joys of rising early while on vacation.


**5. Model Performance**
I mentioned previously that Disney's seasonality is complex.  This likely explains why the models indicate substantial fluctuation and even partial autocorrelation, yet they're stationary.  Data needn't be stable to be stationary; they need only have the rough equivalent of homoskedasticity in short amounts of time.  Everest Expeditions was better.  All of them had pretty low error.  But in terms of predicting wait times, most predictors were off by about 10 minutes.

Ultimately, I ran pmdarimas on all three models to establish the ideal hyperparameters for SARIMAX models.  All three datasets are stationary, even though they don't look stationary.  The metrics are as follows:

## Stationarity metrics
Metric    Na'vi River   Safari  Everest
p-value   .0005         .00162  .00000000973
MSE       181.041       58.638  175.738
MAE       8.83          4.791   9.304


**6. Conclusions and Recommendations**
1. Frequent UX reviews of new system (guests and cast members)
2. Analyze how wait times have changed for out of town visitors
3. Finish the app
4. Improve the app
