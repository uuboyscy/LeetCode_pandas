import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_unique_salary_array = employee.sort_values(
        "salary", ascending=False,
    )["salary"].unique()

    return pd.DataFrame(
        pd.Series(
            pd.NA if len(sorted_unique_salary_array) < N
            else sorted_unique_salary_array[N - 1],
            name="SecondHighestSalary",
        )
    )
