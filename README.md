<html>
	<body>
		<img src="https://otus.ru/static/img/favicons/android-chrome-537x240.jpg" class="img" style="margin: -70px -50px -123px 500px;">
	</body>
</html>

# README

## This is wsgi compatible application.

Which you can run by lauching uwsgi server or another app server 

It just servs files from lib/template folder and show parametrs you provide via address bar.

## Requirements

 - uwsgi

## How to

just run like that `uwsgi --http :8000 --wsgi-file wsgi_app.py`


### Todo list

Task manager [link](https://trello.com/b/sHgUMU33/написать-свой-wsgi-веб-фреймворк-otusru)