"""
Can you solve this real interview question? Biggest Single Number - Table: MyNumbers


+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.


 

A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

The result format is in the following example.

 

Example 1:


Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output: 
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.


Example 2:


Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
Output: 
+------+
| num  |
+------+
| null |
+------+
Explanation: There are no single numbers in the input table so we return null.

"""

# Pandas
import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers = (
        my_numbers
            .groupby("num", as_index=False)
            .filter(lambda x: x.size == 1)
            .sort_values("num", ascending=False, ignore_index=True)
            .loc[0:0]
    )
    return my_numbers if my_numbers.shape[0] > 0 else pd.DataFrame({"num": [None]})


# SQL
"""
with mynumbers_with_null as (
    select num from MyNumbers
    union all
    select null as num
)
select
    num
from mynumbers_with_null
group by num
having count(1) = 1
order by num desc
limit 1;
"""