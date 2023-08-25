import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    return employee[
        employee["id"].isin(
            employee.groupby("managerId").filter(
                lambda x: x["managerId"].count() >= 5
            )["managerId"].unique()
        )
    ][["name"]]
