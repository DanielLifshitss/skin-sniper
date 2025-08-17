from fastapi import APIRouter

"""
 Microservice Integration: Data services API's 
"""
router = APIRouter(
    prefix='/data-service',
    tags=['data-service']
)


#Data Services API endpoints:
@router.get('/')
def test_data_service_api():
    return {'response' : 'data service api success'}