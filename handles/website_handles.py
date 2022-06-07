from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.utils import time_stamp
from database.models import Website
from schemas.register_website_request import RegisterWebsiteRequest


def handle_register_new_website(register_website_data: RegisterWebsiteRequest, user_id: int, db: Session):
    # save item to db
    try:
        website_to_save = Website(**register_website_data.dict())
        db.add(website_to_save)
        db.commit()
        db.refresh(website_to_save)
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred while saving website to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return website_to_save


def handle_get_websites(db: Session, category: str):
    try:
        websites_query = db.query(Website)
        if category:
            websites_query = websites_query.filter(Website.category == category)
        websites = websites_query.all()
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occurred while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    if not websites:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Database is empty")

    return websites


def handle_delete_all_websites(user_id: int, db: Session):
    try:
        all_websites_query = db.query(Website)
        all_websites_query.delete()
        db.commit()
        return True
    except Exception as error:
        print(f"An error occurred while deleting all websites - {error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
