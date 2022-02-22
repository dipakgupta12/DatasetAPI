# DatasetAPI

You need to develop a RESTful API to return a simple data set. The data consists of:
-   Image
-   Title;
-   Description (optional).
- 
## Setup
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate --sync-db
```
## Run
```
python manage.py runserver
```
Upload CSV:
```
curl --location --request POST 'http://localhost:8000/data/upload_csv/' --form 'file=@"Downloads/test_application_data - Sheet 1.csv"'
```
Get Data:
```
curl --location --request GET 'http://localhost:8000/data/'
```