rm -f db.sqlite3

rm -rf Demo/__pycache__
#rm -rf Demo/migrations
#mkdir  Demo/migrations
touch  Demo/migrations/__init__.py 

rm -rf accounts/__pycache__
#rm -rf accounts/migrations
#mkdir accounts/migrations
#touch accounts/migrations/__init__.py 

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
#python3 populate.py
