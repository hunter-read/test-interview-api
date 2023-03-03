# Development Guide
* Requirements: python3
* DB initialization: Create Database gm.db with database/alter1.sql then execute `python3 initialize_db.py`

#### Setup Server:
1. Install flask: `python3 -m pip install -r requirements.txt`
2. Run the server: `python3 -m flask run `
3. Server will be running on http://127.0.0.1:5000

# API user guide
### GET /gm
Get a GM's information  
```
http://127.0.0.1:5000/gm?username=dm-nate
```
#### Params: 
username = dm-nate
#### Example Response:
```
{
"image": "https://spg-images.s3.us-west-1.amazonaws.com/f1585628190434x179357296649197400/0.jpeg",
"lookup_count": 1,
"number_reviews": 1,
"username": "dm-nate"
}
```

### GET /popularity
Return a list of GM's sorted by popularity (most popular first).
```
http://127.0.0.1:5000/popularity
```
#### Params: 
None
#### Example Response:
```
[
"darnorvos",
"dm-nate",
"startplaying-team",
"robert-adducci",
...
]
```