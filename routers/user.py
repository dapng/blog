import schemas, models, database

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from typing import List
from repository import user



router = APIRouter(
    prefix="/user",
    tags=["User"]
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

# @router.get('/user', response_model=List[schemas.ShowUser], tags=["for test!"])
# def all(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @router.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["for test!"])
# def destroy(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     user.delete(synchronize_session=False)
#     db.commit()
#     return 'done'