import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_first_login = activity.groupby("player_id")["event_date"].min()

    return pd.DataFrame(
        data={
            "player_id": activity_first_login.index,
            "first_login": activity_first_login.values
        }
    )
