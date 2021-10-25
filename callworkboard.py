from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hii!!! World"}


@app.get("/cms/tovo/v1/getUserCallWorkBook.do")
async def getUserCallWorkBook():
    return {
        "overview": {
            "totalCustomerCount": 45,
            "processedCustomerCount": 10,
            "completedCallingMinutes": 25,
            "totalPastDueProcessed": 10,
            "totalPastDueAmount": 1718,
        },
        "workbookItems": [
            {
                "totalCurrentOpenAmount": 2500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
            {
                "totalCurrentOpenAmount": 3500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
            {
                "totalCurrentOpenAmount": 2500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
            {
                "totalCurrentOpenAmount": 2500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
            {
                "totalCurrentOpenAmount": 2500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
            {
                "totalCurrentOpenAmount": 2500,
                "pastDueBucketDocumentAmount": [100, 400, 600, 800, 1000],
                "totalBrokenPromises": 2,
                "customerName": "Pushkar",
                "customerNumber": 20,
                "bucketNames": ["1st", "2nd", "3rd", "4th", "5th"],
            },
        ],
    }
