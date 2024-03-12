from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PageDataSchema, Request, Response, RequestPageData
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_book_service(request: RequestPageData, db: Session = Depends(get_db)):
    crud.create_page_data(db, page_data=request.parameter)
    return Response()


@router.get("/")
async def get_pages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_page_data(db, skip, limit)
    return Response()


@router.patch("/update")
async def update_page_data(request: RequestPageData, db: Session = Depends(get_db)):
    _book = crud.update_page_data(db, route=request.parameter.route,
                                  title=request.parameter.title, page_data=request.parameter.page_data)
    return Response()


@router.delete("/delete")
async def delete_page_data(request: RequestPageData, db: Session = Depends(get_db)):
    crud.remove_page_data(db, route=request.parameter.route)
    return Response()
