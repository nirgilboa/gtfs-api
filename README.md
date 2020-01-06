# gtfs-api
Public transportantion REST API over [django-multi-gtfs](https://github.com/tulsawebdevs/django-multi-gtfs)

# Setting up
1. Create a virtualenv and do a`pip install -r requirements.txt`
2. Create local_settings.py file

    `touch gtfs_api/local_settings.py`
    
    `echo DEBUG=Yrue > local_settings.py`

3. Create the database
    ```
    python manage.py sqlcreate | sudo -u postgres psql
    # might be convenient to make the user superuser
    sudo -u postgres psql
    psql% alter user gtfs_admin with superuser;
    ```
4. Create extensions (for PostGIS)
    ```
    python manage.py dbshell
    %sql create extension postgis;
    %sql create extension postgis_topology;
    ```
Note: This might require installation of postgis


