from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def hellow():
    return {'Post router working!'}