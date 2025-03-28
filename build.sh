#1 /usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage collectstatic --noinput
python manage migrate --noinput
if [[ $create_superuser ]];
 then
    python manage createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL"
fi