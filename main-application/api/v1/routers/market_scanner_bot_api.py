from fastapi import APIRouter

router = APIRouter(
    prefix='/market-scanner-bot',
    tags=['market-scanner-bot']
)

@router.get('/')
def test_market_scanner_bot_api():
    return {'response': ' market scanner bot api success'}


