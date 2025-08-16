from fastapi import APIRouter

router = APIRouter(
    prefix='/data-service',
    tags=['data-service']
)

@router.get('/')
def test_data_service_api():
    return {'response' : 'data service api success'}