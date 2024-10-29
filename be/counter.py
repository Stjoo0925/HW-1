# pip install "fastapi[standard]"

from fastapi import APIRouter, HTTPException
from database import DatabaseConnection

router = APIRouter()

@router.post("/counter/increment")
def increment_count():
    try:
        with DatabaseConnection() as db:
            result = db.execute(
                "UPDATE counter SET count = count + 1, updated_at = NOW() WHERE id = 1 RETURNING count;"
            )
            db.commit()
            updated_count = result[0][0]
        return {"count": updated_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error incrementing count: {str(e)}")

@router.post("/counter/decrement")
def decrement_count():
    try:
        with DatabaseConnection() as db:
            result = db.execute(
                "UPDATE counter SET count = count - 1, updated_at = NOW() WHERE id = 1 RETURNING count;"
            )
            db.commit()
            updated_count = result[0][0]
        return {"count": updated_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decrementing count: {str(e)}")

@router.get("/counter")
def get_count():
    try:
        with DatabaseConnection() as db:
            result = db.execute("SELECT count, updated_at FROM counter WHERE id = 1;")
            current_count, last_updated = result[0]
        return {"count": current_count, "updated_at": last_updated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching count: {str(e)}")

