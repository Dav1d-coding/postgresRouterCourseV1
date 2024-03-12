from sqlalchemy.orm import Session
from models import PageData
from schemas import PageDataSchema


def get_page_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PageData).offset(skip).limit(limit).all()


def get_page_data_by_route(db: Session, route: str):
    return db.query(PageData).filter(PageData.route == route).first()


def create_page_data(db: Session, page_data: PageDataSchema):
    _page = PageData(title=page_data.title, page_data=page_data.page_data, description=page_data.description)
    db.add(_page)
    db.commit()
    db.refresh(_page)
    return _page


def remove_page_data(db: Session, route: str):
    _page_data = get_page_data_by_route(db=db, route=route)
    db.delete(_page_data)
    db.commit()


def update_page_data(db: Session, route: str, title: str, page_data: str):
    _page_data = get_page_data_by_route(db=db, route=route)

    _page_data.title = title
    _page_data.page_data = page_data

    db.commit()
    db.refresh(page_data)
    return page_data
