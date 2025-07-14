"""
Can you solve this real interview question? Rising Temperature - Table: Weather


+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.


 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:


Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

"""

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate_minus_1"] = weather["recordDate"].add(pd.Timedelta(days=-1))

    weather = weather.merge(
        weather[
            ["recordDate", "temperature"]
        ],
        how="left",
        left_on="recordDate_minus_1",
        right_on="recordDate",
        suffixes=("_today", "_yesterday")
    )[
        ["id", "recordDate_today", "temperature_today", "temperature_yesterday"]
    ]

    return weather[
        weather["temperature_today"] - weather["temperature_yesterday"] > 0
    ][
        ["id"]
    ]
