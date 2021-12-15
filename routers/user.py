from fastapi import APIRouter

router = APIRouter()

@router.get('/users')
def hellow():
    return {'User router working!'}