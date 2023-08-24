import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    tmp_df = employee.merge(
        employee,
        how="left",
        left_on="managerId",
        right_on="id"
    )

    return pd.DataFrame(
        {
            "Employee": tmp_df[tmp_df["salary_x"] > tmp_df["salary_y"]]["name_x"]
        }
    )
