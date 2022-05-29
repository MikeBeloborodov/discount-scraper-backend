from fastapi import FastAPI, status, Depends
from schemas.message import Message
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database.database_logic import get_db
from schemas.login_user_request import LoginUserRequest
from schemas.login_user_response import LoginUserResponse
from handles.user_handles import handle_login_user

#Base.metadata.create_all(bind=engine)


app = FastAPI()


# if you want only specific servers to be able to talk to your api
# put them in origins, otherwise use "*" to allow everyone
# origins = ["http://www.google.com"]
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main page
@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def root() -> Message:
    return Message(message="Welcome.")


# login
@app.post("/login", status_code=status.HTTP_200_OK, response_model=LoginUserResponse)
def login_user(login_data: LoginUserRequest,
                db: Session = Depends(get_db)):
    return handle_login_user(login_data, db)