"""
Can you solve this real interview question? Classes With at Least 5 Students - Table: Courses


+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.


 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.

The result format is in the following example.

 

Example 1:


Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation: 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.

"""

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby("class", as_index=False).size().query("size >= 5")[["class"]]


"""
PostgreSQL:

select
    class
from courses
group by class
having count(1) >= 5;
"""
