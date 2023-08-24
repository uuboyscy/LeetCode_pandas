import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_unique_salary_list = employee.sort_values(
        "salary", ascending=False,
    )["salary"].unique().tolist()

    sorted_unique_salary_list.append(pd.NA)

    return pd.DataFrame(
        pd.Series(
            sorted_unique_salary_list[1],
            name="SecondHighestSalary",
        )
    )
