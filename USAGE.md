## Usage

```bash
git clone https://github.com/sendgrid/open-source-library-data-collector.git
cd open-source-library-data-collector
virtualenv venv
cp .env_sample .env
```

**Environment Variables**

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

Update your settings in `.env`

```bash
mysql -u USERNAME -p -e "CREATE DATABASE IF NOT EXISTS open_source_external_library_data";
mysql -u USERNAME -p open_source_external_library_data < db/data_schema.sql
cp config_sample.yml config.yml
```

Update the settings in `config.yml`

```bash
source venv/bin/activate
pip install -r requirements.txt
```

Update the code in `package_managers.py`. The functions `update_package_manager_data` and `update_db` were customized for our particular needs. You will want to either subclass those functions in your own application or modify it to suit your needs. We will remove these customizations in a future release. [Here is the GitHub issue](https://github.com/sendgrid/open-source-library-data-collector/issues/5) for reference.

**To run:**

```
source venv/bin/activate
python app.py
```