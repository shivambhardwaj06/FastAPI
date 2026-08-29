from fastapi import FastAPI
from Project_2.exceptions import (
    PincodeNotFoundError,
    pincode_not_found_handler,
    InvalidPinCodeError,
    invalid_pincode_handler
)
from Project_2.modals import LocationResponse,BulkRequest,BulkResponse

from Project_2.data import pincode_db
app = FastAPI(
    title="Pincode lookup API",
    description="Auto fill city and state from Indian Pincode during Checkout"
)


# register your custom exception handler
app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError,invalid_pincode_handler)

@app.get("/")
def root():
    return {"message":"Pincode Lookup API is working "}

@app.get("/pincode/{id}",response_model=LocationResponse)
def lookup_pincode(id:str):
    if len(id) != 6 or not id.isdigit() :
        raise InvalidPinCodeError(id,"Must be exactly 6 digit")
    if id not in pincode_db:
        raise PincodeNotFoundError(id)
    return pincode_db[id]

@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request:BulkRequest):
    results = []
    missing = []
    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)
    return BulkResponse(
        found= len(results),
        not_found=len(missing),
        results=results,
        missing=missing
    )


