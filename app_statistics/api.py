from fastapi import APIRouter, Depends, status

from .schemas import VisitGetterSchema
from .services import statistics_service


statistics_router = APIRouter()


@statistics_router.post('/visit/', status_code=status.HTTP_204_NO_CONTENT, summary='New Visit')
def new_visit(visit_getter: VisitGetterSchema = Depends()):
    statistics_service.new_visit(visit_getter)
