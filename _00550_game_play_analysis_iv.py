"""
Can you solve this real interview question? Game Play Analysis IV - Table: Activity


+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.




Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

The result format is in the following example.

 

Example 1:


Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation: 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

"""

import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity[
        ["player_id", "event_date"]
    ]
    activity["event_date_add_1_day"] = activity["event_date"] + pd.Timedelta(days=1)
    ids_logged_in_following_day = activity.merge(
        activity.groupby("player_id", as_index=False)["event_date_add_1_day"].min(),
        how="left",
        left_on=["player_id", "event_date"],
        right_on=["player_id", "event_date_add_1_day"],
    ).dropna()["player_id"].unique()

    return pd.DataFrame(
        data=[
            [len(ids_logged_in_following_day) / len(activity["player_id"].unique())]
        ],
        columns=["fraction"]
    ).round(2)


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    fraction_id_set = set()
    activity = activity.sort_values(["player_id", "event_date"], ascending=True)
    activity["rn"] = activity.groupby("player_id").cumcount()

    previous_date = None
    for _, row in activity.iterrows():
        if (row["rn"] == 1) and (previous_date + pd.Timedelta(days=1) == row["event_date"]):
            fraction_id_set.add(row["player_id"])

        previous_date = row["event_date"]

    return pd.DataFrame(
        {
            "fraction": [len(fraction_id_set) /  len(activity["player_id"].unique())],
        }
    ).round(2)

