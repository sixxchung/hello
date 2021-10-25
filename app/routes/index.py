from datetime import datetime

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

#from inspect import currentframe as frame
from datetime import datetime

router = APIRouter()

@router.get("/")
async def index(req: Request):
    """
    ELB 상태 체크용 API
    :return:
    """
    return JSONResponse({
        'hello':'world'
    })