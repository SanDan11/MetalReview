from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Album

router = APIRouter(prefix="/albums", tags=["Albums"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("")
def get_albums(
        db: Session = Depends(get_db),
        search: str = Query(None),
        genre: str = Query(None),
        min_rating:float = Query(None)
):
    query = db.query(Album)
    
    if search:
        query = query.filter(
            Album.title.ilike(f"%{search}") |
            Album.artist.ilike(f"%{search}")
        )
    if genre:
        query = query.filter(Album.genre.ilike(f"%{genre}"))
    if min_rating:
        query = query.filter(Album.rating >= min_rating)
        
    return query.all()

@router.get("/{album_id}")
def get_album(album_id: int, db:Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, details="Album not found")
    return album

@router.post("/")
def create_album(data: dict, db: Session = Depends(get_db)):
    new_album = Album(
        title=data.get("title"),
        artist=data.get("artist"),
        genre=data.get("genre"),
        rating=data.get("rating", 0.0) 
    )
    
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album

@router.put("{album_id}")
def update_album(album_id: int, data: dict, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="album not found")
    
    album.title = data.get("title", album.title)
    album.artist = data.get("artist", album.artist)
    album.genre = data.get("genre", album.genre)
    
    db.commit()
    db.refresh(album)
    return album

@router.delete("/{album_id}")
def delete_album(album_id: int, db:Session = Depends(get_db)):
    album = db.query(album).filter(Album.id == album_id).frst()
    if not album:
        return HTTPException(status_code=404, detail="album not found")
    
    db.delete(album)
    db.commit()
    return {"message": f"Album '{album.title}' deleted successfully"}