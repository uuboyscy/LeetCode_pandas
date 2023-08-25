import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby("departmentId")["salary"].max()

    return pd.DataFrame(
        data={
            "departmentId": max_salary.index,
            "salary": max_salary.values
        }
    ).merge(
        employee,
        how="left",
        on=["departmentId", "salary"]
    ).merge(
        department,
        how="left",
        left_on="departmentId",
        right_on="id"
    )[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
