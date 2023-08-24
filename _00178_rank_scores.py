import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values("score", ascending=False)
    sorted_unique_score_array = sorted_scores["score"].unique()

    return sorted_scores.merge(
        pd.DataFrame(
            data={
                "score": sorted_unique_score_array,
                "rank": pd.RangeIndex(
                    start=1, stop=sorted_unique_score_array.size + 1
                )
            }
        ),
        how="left",
        on="score"
    )[["score", "rank"]]
