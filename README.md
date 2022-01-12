# API Создания опросов
API для платформы создания опросов и вопросов к ним. Платформа позволяет администратору создавать опросы и с точки
зрения архитектуры это будет выглядеть так:
```
Опрос <- Вопрос <- Вариант ответа
```
Таким образом, Вопросы связываются с Опросами, а Варианты ответов с Вопросами.
Обычные пользователи могут получать список активных опросов и проходить их.
## Оглавление
* [Перед началом работы](#Перед-началом-работы)
    * [Установка](#Установка)
* [Документация к API](#Документация-к-API)
    * [Авторизация в системе](#Авторизация-в-системе)
    * [Функционал администратора](#Функционал-администратора)
        * [API Опросов](#API-Опросов)
            * [Получение списка всех опросов](#Получение-списка-всех-опросов)
            * [Создание опроса](#Создание-опроса)
            * [Обновление опроса](#Обновление-опроса)
            * [Удаление опроса](#Удаление-опроса)
        * [API Вопросов](#API-Вопросов)
            * [Создание вопроса](#Создание-вопроса)
            * [Обновление вопроса](#Обновление-вопроса)
            * [Удаление вопроса](#Удаление-вопроса)
        * [API Вариантов ответа](#API-Вариантов-ответа)
            * [Создание варианта ответа](#Создание-варианта-ответа)
            * [Обновление варианта ответа](#Обновление-варианта-ответа)
            * [Удаление варианта ответа](#Удаление-варианта-ответа)
    * [Функционал пользователя](#Функционал-пользователя)
        * [Получение всех активных опросов](#Получение-всех-активных-опросов)
        * [Прохождение опроса](#Прохождение-опроса)
        * [Просмотр всех ответов пользователей](#Просмотр-всех-ответов-пользователей)

## Окружение проекта:
  * python 3.10
  * Django 3.2
  * djangorestframework

## Перед началом работы

### Установка

Шаг 1. Клонируйте этот репозиторий

Шаг 2. Установите зависимости:
```
pip install -r requirements.txt
```

Шаг 3. Перейдите в папку `poll_api`:
```
cd poll_api
```

Шаг 4. Сделайте миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Шаг 5. Создайте суперпользователя:
```
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя и пароль, напр. admin, testing321
```
Username (leave blank to use 'admin'): admin
Email address: 
Password: ********
Password (again): ********
Superuser created successfully.
```

Шаг 6. Запустите сервер:
```
python manage.py runserver
```
## Документация к API
### Авторизация в системе
Перед авторизацией убедитесь, что авторизируемый пользователь присутствует в базе Users

Метод: POST

URL: http://localhost:8000/api-auth/login

Тело запроса:
* username: логин
* password: пароль

### Функционал администратора
Администратор может:
* Создавать, удалять и изменять опросы
* Получать список всех опросов (активных и неактивных)
* Создавать, удалять и изменять вопросы
* Создавать, удалять и изменять варианты ответов
* Возможности обычного пользователя
#### API Опросов
##### Получение списка всех опросов
Метод: GET

URL: http://localhost:8000/polls/


##### Создание опроса
Метод: POST

URL: http://localhost:8000/polls/

Тело запроса:
* name: название опроса
* description: описание опроса
* start_date: дата начала опроса, формат записи: YYYY-MM-DD HH:MM
* end_date: дата конца опроса, формат записи: YYYY-MM-DD HH:MM


##### Обновление опроса
Метод: PATCH

URL: http://localhost:8000/polls/%poll_id%/


Тело запроса:
* name: название опроса
* description: описание опроса
* end-date: дата конца опроса, формат записи: YYYY-MM-DD HH:MM

Примечание: дату начала опроса поменять нельзя!


##### Удаление опроса
Метод: DELETE

URL: http://localhost:8000/polls/%poll_id%/


#### API Вопросов
##### Создание вопроса
Метод: POST

URL: http://localhost:8000/questions/

Тело запроса:
* text: текст вопроса
* type: тип вопроса (`SING` - один вариант ответа, `MULT` - несколько вариантов, `FREE` - ответ на вопрос даётся текстом)
* poll: id опроса, к которому нужно прикрепить создаваемый вопрос


##### Обновление вопроса
Метод: PATCH

URL: http://localhost:8000/questions/%question_id%/

Тело запроса:
* text: текст вопроса
* type: тип вопроса (`SING` - один вариант ответа, `MULT` - несколько вариантов, `FREE` - ответ на вопрос даётся текстом)
* poll: id опроса, к которому нужно прикрепить создаваемый вопрос


##### Удаление вопроса
Метод: DELETE

URL: http://localhost:8000/questions/%question_id%/


#### API Вариантов ответа
##### Создание варианта ответа
Метод: POST

URL: http://localhost:8000/options/

Тело запроса:
* text: текст варианта ответа
* question: id вопроса, к которому нужно прикрепить создаваемый вариант ответа


##### Обновление варианта ответа
Метод: PATCH

URL: http://localhost:8000/options/%option_id%/

Тело запроса:
* text: текст варианта ответа
* question: id вопроса, к которому нужно прикрепить создаваемый вариант ответа


##### Удаление варианта ответа
Метод: DELETE

URL: http://localhost:8000/options/%option_id%/


### Функционал пользователя
Пользователь может:
* Получить список активных опросов
* Пройти опрос
* Посмотреть на ответы всех пользователей


#### Получение всех активных опросов
Метод: GET

URL: http://localhost:8000/active-polls/


#### Прохождение опроса
Метод: POST

URL: http://localhost:8000/answers/

Тело запроса:
* user_id: id пользователя
* poll: id опроса
* question: id вопроса
* choice: id ответа на вопрос
* text: для текста на вопрос, если ответ должен быть текстовым


#### Просмотр всех ответов пользователей
Метод: GET

URL: http://localhost:8000/answers/%user_id%/