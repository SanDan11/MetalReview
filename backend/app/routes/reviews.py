from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Review, Album

router = APIRouter(prefix="/reviews", tags=["Reviews"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/{album_id}")
def add_or_update_review(album_id: int, data:dict, db:Session = Depends(get_db)):
    album = db.query(Album).filter(album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    review = db.query(Review).filter(Review.album_id == album_id).first()
    if review:
        review.content = data("content", review.content)
        review.score = data.get("score", review.score)
    else:
        review = Review(album_id=album_id, content=data.get("content"), score=data.get("score"))
        db.add(review) 
        
    db.commit()
    db.refresh(review)
    return review

@router.get("/{album_id}")
def get_review(album_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).flter(Review.album_id == album_id).first()
    if not review:
        raise HTTPException(status_code=404, details="No review found for this album")
    return review   
        