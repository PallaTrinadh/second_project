from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from crud_app02.database import Base,engine,SessionLocal
from crud_app02 import models,schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/",response_model= schemas.UserResponse)
def create_user(user:schemas.UserCreate,db : Session=Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def getusers(db: Session=Depends(get_db)):
    return db.query(models.User).all()

@app.get("/users/{user_id}",response_model=schemas.UserResponse)
def getuser(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user


@app.put("/users/{user_id}",response_model=schemas.UserResponse)
def update_user(user_id:int,user_data:schemas.UserCreate,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not updated")
    for key,value in user_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"msg":"user deleted successfully"}
    
    

    



