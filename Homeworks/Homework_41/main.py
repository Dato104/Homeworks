from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select

from models.trips import Trip
from schemas import TripCreate, TripResponse
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/trips", response_model=TripResponse)
def create_trip(trip: TripCreate, db: Session = Depends(get_db)):

    new_trip = Trip(**trip.model_dump())
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip

@app.get("/trips", response_model=TripResponse)
def read_trips(db: Session = Depends(get_db)):
    stmt = select(Trip).order_by(Trip.id)
    result = db.scalars(stmt).all()
    response = TripResponse(trips=result)
    return response

@app.get("/trips/{trip_id}", response_model=TripResponse)
def read_trip_or_404(trip_id: int, db: Session = Depends(get_db)) -> Trip:
    stmt = select(Trip).where(Trip.id == trip_id)
    result = db.scalars(stmt).first()

    if result is None:
        raise HTTPException(status_code=404, detail="404 Not Found")
    return result


@app.put("/trips/{trip_id}", response_model=TripResponse)
def update_trip(trip_id: int, trip: TripCreate, db: Session = Depends(get_db)):
    existing_trip = db.get(Trip, trip_id)

    if existing_trip is None:
        raise HTTPException(status_code=404, detail="404 Not Found")

    for field, value in trip.model_dump().items():
        setattr(existing_trip, field, value)

    db.commit()
    db.refresh(existing_trip)
    return existing_trip


@app.delete("/trips/{trip_id}")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    existing_trip = db.get(Trip, trip_id)
    if existing_trip is None:
        raise HTTPException(status_code=404, detail="404 Not Found")
    db.delete(existing_trip)
    db.commit()
    return {'message': 'Trip deleted successfully'}




























