## Rangmanch , a Pune-based theatre booking startup, needs a reviews API so audiences can rate and review plays. The API powers their app's review section and average rating displays.

## we need to create a full CRUD API  beckend by SQLite -- create , read , update and delete reviews, plus get average ratings per play with pagination support.

learning objectives:
1) SQL Model for database models
2) SQLite as a zero-configuration database
3) FastApi lifespan events for startup and shutdown logic
4) CRUD operations with FastAPI
5) Pagination with skip/limit
6) Aggregation queries for average ratings

sqlmodel is library that provides a simple way to define SQL database models using Python classes. It is built on top of SQLAlchemy and Pydantic, making it easy to work with databases in FastAPI applications.