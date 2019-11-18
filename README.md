# gtfs-api
Public transportantion REST API over django-multi-gtfs

# create local settings
touch gtfs_api/local_settings.py
# write there DEBUG=True

# CREATE DB

```
python manage.py sqlcreate | sudo -u postgres psql
# might be convenient to make the user superuser
sudo -u postgres psql
psql% alter user gtfs_admin with superuser;
```

# create extensions
```
python manage.py dbshell
%sql create extension postgis;
%sql create extension postgis_topology;
```
might require installation of postgis



