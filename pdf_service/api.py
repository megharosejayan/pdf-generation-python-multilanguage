from fastapi import APIRouter
from starlette.responses import FileResponse


from typing import List, Optional
from . import schemas, services,models

from pdf_service.models import Doc


pdf = APIRouter()


@pdf.post('/', response_model=schemas.DocOut)
async def doc_create(doc: schemas.Doc):
    return await services.create_doc(doc)


@pdf.get('/{pk}')
async def create_pdf(pk: int):
    return FileResponse(await services.create_pdf(pk))

@pdf.get('/',response_model=List[schemas.Doc])
async def get_all():
    data = await Doc.objects.filter().all()
    return data







