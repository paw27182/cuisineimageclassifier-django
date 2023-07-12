# cuisine-image-classifier

# 1. What you can do

* To predict which class an image belong to by using the pre-trained model.<br>
  The classification classes consist of "salad", "sushi" and "tofu".

* (CAUTION) This repository is for beginners' learning.  The precision of the model is not so good.

<br>

# 2. How to use

* Program start
  * cd cuisineimageclassifierproject
  * python.exe manage.py runserver 8000

<br>

* Open browser
  * http://localhost:8000/
  * Submit an image:<BR>
   ./cuisineimageclassifier-flask/tests/salad.jpg


<br>

# 3. System
* OS: Windows 10
* Web Framework: Django
* Python 3.10.11
* Python Libraries: See the requirements.txt file
* Bootstrap 5.2.3
* jQuery 3.7.0

<br>

# 4. Directories and Files Overview

| Directory/File |D/F| description |
| :------------- | :-| :---------- |
| cicapp | Dir | Django application directory |
| cicapp/model | Dir | Machine learning model |
| cicapp/command.py | File | Machine learning predict program |
| cicapp | Dir | application directory |
| cicproject | Dir | Django project directory |
| static | Dir | css, html, javascript files |
| templates | Dir | html files |
| tests | Dir | test image files |
| manage.py | File | Django management module |
| READMD.md | File ||
| requirements.txt | File | prerequisite libraries |
