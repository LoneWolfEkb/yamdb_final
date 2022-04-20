![workflow](https://github.com/LoneWolfEkb/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Сайт - база отзывов о фильмах, книгах и музыке. Пользователи могут оставлять рецензии на произведения, а также комментировать эти рецензии. Администрация добавляет новые произведения и категории (книга, фильм, музыка и т.д.) Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

Адрес сайта
---------------
http://178.154.199.71/redoc/

Пример запроса
---------------
http://178.154.199.71/api/v1/titles/

Как запустить
---------------
Необходимое ПО
Docker: https://www.docker.com/get-started
Docker-compose: https://docs.docker.com/compose/install/

Инструкция по запуску
---------------
Для запуска необходимо из корневой папки проекта ввести в консоль(bash или zsh) команду:

docker-compose up --build

Затем узнать id контейнера, для этого вводим

docker container ls

В ответ получаем

CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                    NAMES

<...>   nginx:1.21.3              "/docker-entrypoint.…"   5 minutes ago   Up 4 minutes   0.0.0.0:80->80/tcp       infra_nginx_1

<...>    LWE57/infra_web:latest   "/bin/sh -c 'gunicor…"   5 minutes ago   Up 4 minutes   0.0.0.0:8000->8000/tcp   infra_web_1

<...>    postgres:13.0             "docker-entrypoint.s…"   5 minutes ago   Up 4 minutes   5432/tcp                 infra_db_1

Нас интересует контейнер infra_web_1, заходим в него командой

docker exec -it <CONTAINER ID> sh

Делаем миграцию БД, и сбор статики

python manage.py migrate
python manage.py collectstatic

При желании можно загрузить тестовую бд с контентом

python manage.py loaddata fixtures.json

После запуска проекта, инструкцию можно будет посмотреть по адресу http://0.0.0.0/redoc/

Автор
---------------
Михаил Турхан - https://github.com/LoneWolfEkb

