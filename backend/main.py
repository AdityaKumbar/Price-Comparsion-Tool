from fastapi import FastAPI
from scraper.amazon import fetch_amazon_price
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Price Comparison Backend is Running!"}

@app.get("/search")
def search(product_name: str):
    # Scrape from Amazon
    amazon_data = fetch_amazon_price(product_name)
    
    return {"results": amazon_data}
