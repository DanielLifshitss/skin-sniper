from fastapi import APIRouter

"""
 Microservice Integration: Scanner Bot API's 
"""
router = APIRouter(
    prefix='/market-scanner-bot',
    tags=['market-scanner-bot']
)


#Scanner Bot API endpoints:
@router.get('/')
def test_market_scanner_bot_api():
    return {'response': ' market scanner bot api success'}


