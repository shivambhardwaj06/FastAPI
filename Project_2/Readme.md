// A D2C brand needs to auto-fill city and state fields when a customer types their pincode during checkout.  This reduces friction and typos in the address form.

Key Implementation steps :
Pydantic `field_validator` for input validation
Custom exception classes and exception handlers
POST requests with JSON body
Difference between path parameters and request bodies
Clean error response patterns 