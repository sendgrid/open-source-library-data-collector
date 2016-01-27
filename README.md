# Install and run locally #
For the first time only:
```
virtualenv venv
```

```
cp .env_sample .env
```
Update your settings in `.env`
```
mysql -u USERNAME -p DBNAME < db/data_schema.sql
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

