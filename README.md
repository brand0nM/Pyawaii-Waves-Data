# Pyawaii-Waves-Data
## Project Overview
We've been hired to create a mobile app that tracks weather data and filters results locally. 

### Purpose
With a SQLite databases use SQLalchemy to query the local data.

## Analysis
After creating an engine and inspecting the tables/columns, one can use SQLalchemy's query or session function to analyse the data; query allows for standard sql queries and session requires python. In this project we used sesssion to gather data from the measurements table.

## Results
<img width="939" alt="Screen Shot 2022-05-15 at 2 30 11 PM" src="https://user-images.githubusercontent.com/79609464/168492642-6c57d3be-2c78-4070-a6e3-3e22382d9c17.png">
- The average temperature in June is warmer than in December
  - Temperature's in December are less predicatible since the standard deviation is greater
- In both month's the highest temperature is about the same, but the lowest temperature is lower in December
  - Temperature is more volatile in December since the spread is greater

### Station USC00519397's Data
<img width="1306" alt="Screen Shot 2022-05-21 at 8 14 22 AM" src="https://user-images.githubusercontent.com/79609464/169655552-ae29fe15-495b-495b-82ce-88b89c3483bb.png">
- Temperature is more consistent in the Summertime
## Summary
Temperatures are most volatile in December; this can be observed in the standard deviation/spread of high to low temperatures. Looking at a specific station's data confirms this belief.
