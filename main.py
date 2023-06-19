from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
base_api = "/v1/api"

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['db_wilayah']  # replace 'your_database' with the name of your database

class Provinces(BaseModel):
    _id: Optional[str]
    province_id: str
    province: str
    status: int

class Regencies(BaseModel):
    _id: Optional[str]
    province_id: str
    regency_id: str
    regency: str
    status: int

class Districts(BaseModel):
    _id: Optional[str]
    regency_id: str
    district_id: str
    district: str
    status: int

class Villages(BaseModel):
    _id: Optional[str]
    district_id: str
    village_id: str
    village: str
    status: int

@app.get(base_api+"/provinces/", response_model=List[Provinces])
async def read_provinces():
    collection = db['provinces']  # replace 'your_collection' with the name of your collection
    filter_query = {}  # Initialize an empty filter query
    filter_query['status'] = 1

    items = []
    for item in collection.find(filter_query):
        items.append(Provinces(**item))
    
    return items

@app.get(base_api+"/regencies/", response_model=List[Regencies])
async def read_regencies(province_id: Optional[str] = None):
    collection = db['regencies']  # replace 'regencies' with the name of your regencies collection
    filter_query = {}  # Initialize an empty filter query
    filter_query['status'] = 1

    if province_id is not None:
        filter_query['province_id'] = int(province_id)    

    items = []
    for item in collection.find(filter_query):
        items.append(Regencies(**item))
    
    return items

@app.get(base_api+"/districts/", response_model=List[Districts])
async def read_districts(regency_id: Optional[str] = None):
    collection = db['districts']  # replace 'regencies' with the name of your regencies collection
    filter_query = {}  # Initialize an empty filter query
    filter_query['status'] = 1

    if regency_id is not None:
        filter_query['regency_id'] = int(regency_id)

    items = []
    for item in collection.find(filter_query):
        items.append(Districts(**item))
    
    return items

@app.get(base_api+"/villages/", response_model=List[Villages])
async def read_villages(district_id: Optional[str] = None):
    collection = db['villages']  # replace 'regencies' with the name of your regencies collection
    filter_query = {}  # Initialize an empty filter query
    filter_query['status'] = 1

    if district_id is not None:
        filter_query['district_id'] = int(district_id)

    items = []
    for item in collection.find(filter_query):
        items.append(Villages(**item))
    
    return items