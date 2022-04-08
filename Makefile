run: 
	gunicorn -c gunicorn.py run:app

debug:
	sh debugserver
