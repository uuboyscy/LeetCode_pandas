"""
Can you solve this real interview question? Tree Node - Table: Tree


+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the column with unique values for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure is always a valid tree.


 

Each node in the tree can be one of three types:

 * "Leaf": if the node is a leaf node.
 * "Root": if the node is the root of the tree.
 * "Inner": If the node is neither a leaf node nor a root node.

Write a solution to report the type of each node in the tree.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

[https://assets.leetcode.com/uploads/2021/10/22/tree1.jpg]


Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
Explanation: 
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.


Example 2:

[https://assets.leetcode.com/uploads/2021/10/22/tree2.jpg]


Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
+----+-------+
Explanation: If there is only one node on the tree, you only need to output its root attributes.


 

Note: This question is the same as 3054: Binary Tree Nodes. [https://leetcode.com/problems/binary-tree-nodes/description/]
"""
import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree_with_p_and_n = tree.merge(
        tree,
        how="left",
        left_on="id",
        right_on="p_id",
        suffixes=["", "_r"]
    )[["id", "p_id", "id_r"]]

    tree_with_p_and_n["type"] = "Inner"
    tree_with_p_and_n.loc[tree_with_p_and_n["id_r"].isna(), "type"] = "Leaf"
    tree_with_p_and_n.loc[tree_with_p_and_n["p_id"].isna(), "type"] = "Root"

    return tree_with_p_and_n[["id", "type"]].drop_duplicates()


###############################

import numpy as np
import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree_with_p_and_n = tree.merge(
        tree,
        how="left",
        left_on="id",
        right_on="p_id",
        suffixes=["", "_r"]
    )[["id", "p_id", "id_r"]]

    tree_with_p_and_n["type"] = np.where(
        tree_with_p_and_n["p_id"].isna(),
        "Root",
        np.where(
            tree_with_p_and_n["id_r"].isna(),
            "Leaf",
            "Inner",
        )
    )

    return tree_with_p_and_n[["id", "type"]].drop_duplicates()


################

import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:

    parents_set = [x for x in tree.p_id.to_list() if type(x) == int]

    def category_assign(row):
        if pd.isna(row["p_id"]):
            return "Root"
        elif row["id"] in parents_set:
            return "Inner"
        else:
            return "Leaf"

    tree["type"] = tree.apply(category_assign, axis = 1)
    return tree[["id","type"]]


"""
with next_id_table as (
    select
        tl.id,
        tl.p_id,
        tr.id as next_id,
        case
            when tl.p_id is null then 'Root'
            when tr.id is null then 'Leaf'
            else 'Inner'
        end as type
    from Tree tl
    left join Tree tr
    on tl.id = tr.p_id
)
select
    distinct id, type
from next_id_table;
"""