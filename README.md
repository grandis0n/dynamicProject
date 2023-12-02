# Blog Project
Сайт для размещения постов с изображением и описанием
## Требования
Django==4.2.7<br>
django-allauth==0.58.2<br>
Pillow==10.1.0<br>
requests==2.31.0<br>
## Установка
1. Склонируйте репозиторий
2. Создайте виртуальное окружение
```
python -m venv venv
```
3. Активируйте виртуальное окружение
```
.\venv\Scripts\activate
```
4. Установите зависимости
5. Примените миграции
```
python manage.py migrate
```
6. Запустите сервер разработки
```
python manage.py runserver
```
По умолчанию, приложение будет доступно по адресу http://127.0.0.1:8000/