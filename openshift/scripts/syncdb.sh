oc get pods
oc rsh $1 python manage.py migrate --run-syncdb
