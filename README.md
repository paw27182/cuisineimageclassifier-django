# cuisine-image-classifier

# 1. What you can do

* To predict which class an image belong to by using the pre-trained model.<br>
  The classification class consist of "salad", "sushi" and "tofu".

* (CAUTION) This repository is for beginners' learning.  The precision of the model is not so good.

<br>

# 2. How to use

* Program start
  * cd cuisineimageclassifierproject
  * python.exe manage.py runserver 8000

<br>

* Open browser
  * http://localhost:8000/
  * Submit an image: ./cuisineimageclassifier-flask/tests/salad.jpg


<br>

# 3. System
* OS: Windows 10
* Web Framework: Django
* Python 3.10.11
* Python Libraries: Django matplotlib numpy Pillow requests tensorflow
* Bootstrap 5.2.3
* jQuery 3.7.0

<br>

# 4. Directories and Files Overview

| Directory/File |D/F| description |
| :------------- | :-| :---------- |
| cuisineimageclassifierapp | Dir | Django application directory |
| cuisineimageclassifierapp/model | Dir | Machine learning model |
| cuisineimageclassifierapp/command.py | File | Machine learning predict program |
| cuisineimageclassifierapp/urls.py | File ||
| cuisineimageclassifierapp/views.py | File ||
| cuisineimageclassifierproject | Dir | Django project directory |
| cuisineimageclassifierproject/settings.py | File ||
| cuisineimageclassifierproject/urls.py | File ||
| static | Dir | css, html, javascript files |
| templates | Dir | html files |
| tests | Dir | test image files |
| manage.py | File | Django management module |
| READMD.md | File ||
| requirements.txt | File | prerequisite libraries |
