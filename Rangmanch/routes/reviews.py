from sqlmodel import Session, select , func
from models import Review, ReviewCreate , ReviewRead, ReviewUpdate
from fastapi import APIRouter , Depends, Query , Path
from database import get_session

router = APIRouter(prefix="/review",tags=["reviews"])

@router.post("/",response_model=ReviewRead)
def create_review(review:ReviewCreate, session : Session = Depends(get_session)):
    db_review = Review(**review.model_dump())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

# pagination with skip and limit
@router.get("/list/",response_model=list[ReviewRead])
def List_review(
    play_name:str | None = Query(None, description="Filter by play name"),
    skip:int = Query(0, ge=0, description="Number of records to skip"),
    limit:int = Query(10, ge=1, description="Number of records to fetch"),
    session: Session = Depends(get_session)
):
    query = select(Review)
    if play_name:
        query = query.where(Review.play_name == play_name)
    query = query.offset(skip).limit(limit)
    reviews = session.exec(query).all()
    return reviews

# average rating for a specific play
@router.get("/average")
def average_rating(play_name:str = Query(..., description="Play name to calculate average rating"), session: Session = Depends(get_session)):
    query = select(func.avg(Review.rating), func.count(Review.id)).where(Review.play_name == play_name)
    result = session.exec(query).first()
    avg_rating , total_reviews = result
    if total_reviews == 0:
        raise ValueError(f"No reviews found for play: {play_name}")
    return {
        "play_name" : play_name,
        "average_rating" : avg_rating,
        "total_reviews" : total_reviews
    }


#get reviews by id
@router.get("/{review_id}", response_model = ReviewRead)
def reviewbyid(review_id:int =Path(..., description="Review ID to fetch"), session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise ValueError(f"Review with ID {review_id} not found")
    return review

#update review by id 
@router.patch("/update/{review_id}", response_model=ReviewRead)
def update_review(review_id:int, review_update:ReviewUpdate, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise ValueError(f"Review with ID {review_id} not found")
    for key, value in review_update.model_dump(exclude_unset=True).items():
        setattr(review, key, value)
    session.add(review)
    session.commit()
    session.refresh(review)
    return review

#delete review by id
@router.delete("/delete/{review_id}")
def delete_review(review_id:int, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise ValueError(f"Review with ID {review_id} not found")
    session.delete(review)
    session.commit()
    return {"message": f"Review with ID {review_id} deleted successfully"}