from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.utils import time_stamp
from database.models import Promo
from schemas.register_promo_request import RegisterPromoRequest


def handle_register_new_promo(register_promo_data: RegisterPromoRequest, user_id: int, db: Session):
    # save item to db
    try:
        promo_to_save = Promo(**register_promo_data.dict())
        db.add(promo_to_save)
        db.commit()
        db.refresh(promo_to_save)
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return promo_to_save


def handle_get_all_promos(db: Session):
    try:
        all_promos_query = db.query(Promo)
        all_promos = all_promos_query.all()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    if not all_promos:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Database is empty")

    return all_promos


def handle_get_limited_promos(limit: int, db: Session, skip: int, category: str, website: str, order_by: str):
    try:
        limited_query = db.query(Promo)
        if category:
            limited_query = limited_query.filter(Promo.cathegory == category)
        if website:
            limited_query = limited_query.filter(Promo.website_title == website)
        if order_by == "price_up":
            limited_query = limited_query.order_by(Promo.new_price.asc(), Promo.title)
        if order_by == "price_down":
            limited_query = limited_query.order_by(Promo.new_price.desc(), Promo.title)

        limited_query = limited_query.offset(skip).limit(limit)

        limited_query_promos = limited_query.all()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    
    return limited_query_promos


def handle_get_count_promos(db: Session, category: str, website: str):
    try:
        count_query = db.query(Promo)
        if category:
            count_query = count_query.filter(Promo.cathegory == category)
        if website:
            count_query = count_query.filter(Promo.website_title == website)
        count = count_query.count()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    
    return count


def handle_delete_all_promos(user_id: int, db: Session):
    try:
        all_promos_query = db.query(Promo)
        all_promos_query.delete()
        db.commit()
        return True
    except Exception as error:
        print(f"Error occurred during deleting all promos - {error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
        