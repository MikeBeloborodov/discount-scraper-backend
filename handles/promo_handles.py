from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.utils import time_stamp
from database.models import Promo
from schemas.register_promo_request import RegisterPromoRequest
from typing import Optional


def handle_register_new_promo(register_promo_data: RegisterPromoRequest, user_id: int, db: Session):
    # save item to db
    try:
        promo_to_save = Promo(**register_promo_data.dict())
        db.add(promo_to_save)
        db.commit()
        db.refresh(promo_to_save)
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return promo_to_save


def handle_get_all_promos(db: Session):
    try:
        all_promos_query = db.query(Promo)
        all_promos = all_promos_query.all()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    if not all_promos:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Database is empty")

    return all_promos


def handle_get_limited_promos(db: Session, limit: int, skip: int, website: str):
    try:
        limited_query = db.query(Promo)
        if website:
            limited_query_promos = limited_query.filter(Promo.website_title == website).offset(skip).limit(limit).all()
        else:
            limited_query_promos = limited_query.offset(skip).limit(limit).all()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    
    return limited_query_promos


def handle_get_count_promos(db: Session, search: Optional[str]):
    try:
        if search != "":
            count_query = db.query(Promo).filter(Promo.website_title == search)
        else:
            count_query = db.query(Promo)
        count = count_query.count()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    
    return count


def handle_delete_all_promos(user_id: str, db: Session):
    try:
        all_promos_query = db.query(Promo)
        all_promos_query.delete()
        db.commit()
        return True
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
        