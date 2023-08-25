import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated_email_person = person.groupby("email").filter(
        lambda x: x["email"].count() > 1
    )

    return pd.DataFrame(
        {
            "Email": duplicated_email_person["email"].unique()
        }
    )
