#! /bin/sh
#if ["$DB_NAME" = "postgres"]
#then
#    echo 'waiting postgres'
#
#    while ! nc -z $DB_HOST $DB_PORT; do 
#        sleep 0.1
#    done 
#    echo "Postgres Started"
#fi
echo $DB_NAME
python manage.py migrate
#python manage.py collectstatic --no-input --clear
exec "$@"