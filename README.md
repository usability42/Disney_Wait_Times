# Time Series Analysis of Rides at Disney's Animal Kingdom

### Background
---
Almost every Disney guest looks forward to their vacation, but no one relishes spending their vacation in assorted lines, queues, and waits (oh my!).  As Disney gradually increases park and resort capacities after covid, wait times are likely to increase.

Disney sharply increased their ticket prices and annual passes recently.  In addition, whereas Disney used to include 3 "Fast Passes" with all tickets, now everyone must pay to jump the line.  Worse, there are two different types of passes.  To my understanding, some rides only accept one, some the other, and some accept both.  Disney, I love you, but this is a serious #UXFail that your park employees and guests will despise.  I predict that it will prove especially problematic for guests with limited English.  Add prices that vary based on demand and you devolve to the customer confusion notorious in other industries.

Given increased pricing, guests want to maximize their stays.  Minimizing time in lines is crucial.  However, people hate surprise extra costs added on top of their already expensive vacations.  Some businesses have observed that potential customers from some cultures not to complete online purchases.  Americans are somewhat accustomed to this nickel and diming, although they hate it.  In other countries, everything is included in the quoted rate upfront, including taxes, "fees", etc.  Aside from Disney's meal passes, Disney has an excellent reputation for User Experience and customer service.

### Executive Summary
---
The goal is to listen to the voice of the customer; of course, I am also a potential customer, albeit a local, low-spending one.

The goal of this project is two-fold:
1) Budget-conscious guests: This term is relative.  Disney tickets are not cheap for anyone anymore.  An Annual Pass used to cost under $500.  A similar pass with limited visits per year now costs over $800.  Locals are more likely to eat meals outside of the park and less likely to purchase expensive merchandise.  This group will want to minimize money spent on passes to skip lines, since they're already paying roughly 40% more and getting a lot less.  For this group, I want to be able to recommend when to purchase and not purchase passes to skip lines better than Disney's app predicts.  There have been a lot of complaints online about Disney's app.

2) International and Other Premium Guests: These guests book likely book their trips through Disney Vacations or use timeshare points to book stays at Disney resorts.  In addition to park admission, top customers usually pay for airfare, accommodations, meals, and some ground transportation.  While I don't know how much Disney earns on merchandise sales, the sheer number of shops at the parks indicates that they must be doing pretty well.  These guests are also far more likely to eat at Disney's restaurants, especially if they don't rent cars.  There are restaurant options a few miles from Disney, but getting there requires a rental car, taxi, or rideshare.  In other words, these guests purchase spend most of their vacation expenditures on Disney-owned properties (until they take a cab to a Universal Resort for the remainder of their vacation).  The questions for this group are:
i) Does requiring guests to purchase passes to skip lines negatively impact Disney's sterling customer service reputation for cultural reasons?

ii) Can this process be streamlined so jet-lagged guests needn't figure out this stuff by 7AM the next day?

iii) Is there a better option, such as offering 3 fast passes to everyone booking through Disney Vacations or Disney Cruises?

iv) How confusing is the new system for these guests?  (As a native English speaker who has traveled abroad extensively, I find it very confusing).

**1. Data Source**
My data are neither my data nor Disney data.  Disney keeps most of its data under lock and key.  The data come from https://touringplans.com/walt-disney-world/crowd-calendar#DataSets.  According to information on the web site, a woman somewhere claims to have compiled wait times for over a dozen Disney attractions dating back to at least 2015.  I cannot verify that these data are accurate, but my aim here is to employ time series analysis to analyze wait times and answer the question: to buy a pass or not to buy a pass.

I'm limiting the scope of this project to the rides in highest demand at Animal Kingdom, namely Na'vi River Journey, Flight of Passage, Kilimanjaro Safaris, and Expedition Everest.  The first two are part of Pandora, the world of Avatar.  Expedition Everest is a roller coaster that goes forwards and backwards.  Kilimanjaro Safaris riders ride in a safari vehicle among roaming animals.

**2. Data Dictionary**
The dataset had only a few fields:
- Date
- Datetime
- SPOSTMIN - posted waiting time in minutes at ride entrance
- SACTMIN - actual waiting time in minutes

I calculated myriad fields to handle reindexing, daily average wait times, weekly average wait times, and more.  All of them are derived from the features above.


**3. My Goal & Methodology**
Create a model that predicts ride wait times within a few minutes in either direction.  I used time series models to account for the seasonality inherent with tourism-dependent businesses.  However,   My questions:  Are rides busier at certain times of the day, perhaps after meal times?  Are some days of the week significantly better than others?  Aside from Disney's blockout dates for cast members and lower-level pass holders, should certain weeks be avoided?

**4. Exploratory Data Analysis**
During exploratory data analysis, I discovered that Disney's seasonality is like no other.  Some ride wait times fluctuate wildly, but not predictably, during the day.  Overall, Tuesdays and Wednesdays have lower wait times than Saturdays, but in concrete terms (i.e. in terms of legs standing on concrete), the differences weren't very meaningful.  Under the new pay to skip the line plans, it boils down to whether waiting an extra 5-10 minutes will prompt a guest to purchase a pass.  If a ride wait is 300 minutes, waiting 10 more minutes is likely moot.  But on the other side, would someone pay $15 to wait 10 minutes instead of 20?  I'm sure Disney has crunched those numbers; I'm sure they're betting on them.  But how do guests hack the system?  With everyone booking their rides on the day of their visit, how can visitors plan ahead?  Even annual passholders have to make (free) reservations to visit the park, in addition to purchasing their annual passes.  Reservations are free; they just limit the total number of park guests.  But annual passholders have a limited number of reservations per year.  Gone are the days of dropping by for the afternoon or booking free fast passes ahead of time.  Passholders must plan.

And everyone has to get up early to make those precious reservations, since they've gone Southwest Airlines-style.  Resort guests can begin reserving lane skipping at 7am on the day of park visits.  Everyone else must wait until the park opens.

Oh, the joys of rising early while on vacation.  Another #UXfail, Disney.

**5. Background Information**
I analyzed data for four rides: Na'vi River Journey, Flight of Passage, Kilimanjaro Safaris, and Expedition Everest.  Na'vi River Journey and Flight of Passage opened in Spring, 2017.  The other two opened in 1998 and 2006, respectively.  My data for these rides only dates back to 2015.

Likely because of limited data before the covid epidemic hit, and because ride wait times inevitably are much higher the first year a ride is open, the data for Na'vi River Journey and Flight of Passage are not stationary (see below).

**6. Model Performance**
I mentioned previously that Disney's seasonality is complex.  This likely explains why the models indicate substantial fluctuation and even partial autocorrelation, yet the data for the older rides are stationary.  Data needn't be stable to be stationary; they need only have the rough equivalent of homoskedasticity in short amounts of time.

Unfortunately, the lack of data and the COVID pandemic - during which Disney has limited park attendance to as little as 25% capacity - preclude any analysis of seasonality for Na'vi River Journey and Flight of Passage.  While wait times for all rides was lower on Tuesdays and Wednesdays than on Saturdays, and spikes in wait times were observed every several months for Kilimanjaro Safaris, the spikes were not a consistent number of months apart, even accounting for Spring break shifting as much as 5 weeks.  One issue on Kiliminjaro Safaris is that when an animal wanders into a Safari vehicle's path, all drivers stop until the animal passes.  This can take anywhere from 2 - 45 minutes.  To my knowledge, park staff never interfere unless the animal is showing signs of a medical emergency.

I also looked for hourly seasonality, but that is complicated by Animal Kingdom's varying operating hours.  The park's hours differ based on the day of the week and month / season of the year.

## Performance Metrics
Metric    Na'vi River  Flight     Safari    Everest
p-value   .297         .0805      .00017    .0156
MSE       12,799.44    20,561.44  8,274.73  4,029.73
MAE       7.291        10.71      6.25      4.18

## What This Means in Plain English
It's much easier to predict wait times for Kilimanjaro Safaris and Expedition Everest because there is a lot more data on these two rides.  They've been open much longer.  Na'vi River Journey and Flight of Passage were open less than 2 years before the pandemic closed the parks.  The dataset I analyzed also has some chunks of missing data, which makes predicting wait times even harder.  Analysis indicates that wait times for the 2 newer rides are decreasing over time, but that happens with every new, high profile ride.  It's simply too soon to tell whether wait times have stabilized or if they are shifting over time.  However, since the typical wait time for Flight of passage exceeds 2 hours, most guests interested in riding a Banshee will want to pay to skip the line to do so.  Na'vi River Journey is a little less clear.  There are days when budget-conscious guests could wait in line for 30 minutes or less.  It usually requires riding early in the day on a Tuesday or Wednesday, but exceptions happen.

Expedition Everest and Kilimanjaro Safaris have been open long enough that they're no longer novel, but they remain favorites.  Although their wait times have "stabilized," waits differ substantially at different times of the year.  If budget-conscious travelers are willing to wait up to 45 min and can avoid peak seasons, they can probably avoid paying for fast passes.  Guests traveling during non-peak times can also avoid purchasing fast passes for these rides; usually their wait times hover around 25 min and one can check current waits using Disney's (albeit klunky) app to find shorter wait times.

**7. To Purchase a Pass to Skip the Line or Not?: The Short Version**
Na'vi River Journey: Yes
Flight of Passage: Yes
Kilimanjaro Safaris: Depends on day of the week and time of year
Expedition Everest: Peak days yes, otherwise, you can probably wait less than 30 min for free.


**8. Conclusions and Recommendations for Disney**
1. Frequent UX reviews of new system (guests and cast members)
2. Analyze how wait times have changed for out of town visitors vs. previous system
3. Improve the ride estimator app (it has poor reviews online)

**9. Next Steps for this Project**
1. Finish Streamlit App displaying wait predictions for Autumn, 2021
2. Ponder how on Earth Disney and similar venues predict seasonality
