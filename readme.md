# Установка и запуск
Для работы необходимо наличие установленных и запущенных программ docker и docker compose.
В файле .env указываются параметры конфигурации приложения.
Для запуска в терминале из корневой папки проекта вызываем команду:
```shell
docker compose up
```
При первом запуске необходимо выполнить миграции в терминале контейнера
```shell
alembic upgrade head
```

# Примеры
Пример регистрации пользователя:
```shell
curl --location --request POST 'http://127.0.0.1:8000/register?username=dyada'
```
Пример вывода:
```json
{
    "user_id": 1,
    "token": "b251424a-104b-419e-9d4b-b65553e32dd9"
}
```

Пример добавления аудиозаписи. Выполняется из корневой папки проекта:
```shell
curl --location --request POST 'http://127.0.0.1:8000/record?user=1&token=b251424a-104b-419e-9d4b-b65553e32dd9' \
--form 'audio=@"./example/77-bpm-drum-loop.wav"'
```
Пример вывода:
```json
{
    "audio_url": "http://localhost:8000/record?id=cac64766-c33c-4d6d-884d-f72e751ad0d9&user=1"
}
```

Пример скачивания аудиозаписи:
```shell
curl --location --request GET 'http://localhost:8000/record?id=cac64766-c33c-4d6d-884d-f72e751ad0d9&user=1'
```

# База данных
Для подключения к базе данных необходимо использовать параметры .env из файла. 
Для подключения через клиент psql открываем bash в контейнере:
```shell
docker exec -it <container_id> bash
```
пример:
```shell
docker exec -it e583ee429f81169cd4fd92a5776243ac650ba7cd1ab734db387baf0860a28b3f bash
```
Затем подключаемся к postgres:
```shell
psql --no-readline -U <POSTGRES_USER> -h <HOST> -p <POSTGRES_PORT> -d <POSTGRES_DB_NAME> -W
```
пример:
```shell
psql --no-readline -U postgres -h localhost -p 5432 -d postgres -W
```
Вводим пароль <POSTGRES_PASSWORD> например 'postgres'
