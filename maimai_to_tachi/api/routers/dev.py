from fastapi import APIRouter, HTTPException
from maimai_to_tachi.api.models.dan_rank import DanRank, dan_ranks
from maimai_to_tachi.api.models.score import Judgements, Score

router = APIRouter(prefix="/dev", tags=["dev"])


@router.get("/score/{identifier}")
def get_score(identifier: int) -> Score:
    if identifier == 712:
        return Score(
            identifier="712",
            matchType="inGameID",
            lamp="CLEAR",
            difficulty="Master",
            percent=89.15,
            judgements=Judgements(perfect=528, great=49, good=46, miss=18),
            timeAchieved=1740088260000
        )
    raise HTTPException(
        status_code=404,
        detail="Unable to find score with identifier of %d" % identifier
    )


@router.get("/dan_rank/{name}")
def get_dan_rank(name: str) -> DanRank:
    if name in dan_ranks.keys():
        return dan_ranks[name]
    raise HTTPException(
        status_code=404,
        detail="Unable to find dan rank with identifier of %s" % name
    )
