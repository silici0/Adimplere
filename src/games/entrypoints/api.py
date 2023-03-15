from fastapi import APIRouter
from src.games.entrypoints.schemas import output
from src.games import service
from typing import List, Any

router = APIRouter()

@router.get(
    "/games",
    summary="Retorna a lista de games",
    response_model=List[output.GameShortDescription]
)
def game_short_description() -> List[output.GameShortDescription]:
    return service.short_description()

@router.get(
    "/games/{name}",
    summary="Retorna um game de acordo com nome enviado",
    response_model=List[output.GameLongDescription]
)
def game_long_description(name: str) -> List[output.GameLongDescription]:
    if not name:
        raise HTTPException(status_code=404, detail="Name field is required")
    return service.long_description(name)