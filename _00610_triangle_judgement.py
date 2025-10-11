"""
Can you solve this real interview question? Triangle Judgement - Table: Triangle


+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.


 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

 

Example 1:


Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

"""

### Pandas
import pandas as pd


# Solution 1
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle_max_side_array = triangle.max(axis=1)

    triangle.loc[
        triangle["x"] + triangle["y"] + triangle["z"] - triangle_max_side_array > triangle_max_side_array,
        "triangle"
    ] = "Yes"

    triangle["triangle"] = triangle["triangle"].fillna("No")

    return triangle


# Solution 2
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(
        lambda s: "Yes" if (s.x + s.y + s.z - s.max() > s.max()) else "No", axis=1)

    return triangle


### SQL
"""
select
    *,
    case
        when x + y + z - greatest(x, y, z) > greatest(x, y, z) then 'Yes'
        else 'No'
    end  as triangle
from Triangle;
"""
