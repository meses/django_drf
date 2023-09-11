# Проект по djando-drf

### Инструкция по запуску Docker-контейнера:
- Создаем django проект или заходим в существующий проект.
- Установим Docker: нужно установить Docker на свой компьютер. 
Для этого можно посетить официальный сайт Docker (https://www.docker.com/) и следовать 
инструкциям для установки Docker на свою операционную систему.
- Создаем внутри проекта Dockerfile(обычно он находится в корневой папке проекта).
- Описываем внутри Dockerfile инструкции для построения Docker-образа.
- Сборка Docker-образа: выполняем команду в терминале для сборки Docker-образа на основе 
Dockerfile. В команде указываем путь к директории проекта, где находится Dockerfile. 
Пример команды:
```
docker build -t <image_name> <path_to_project_directory>
```
где `<image_name>` - имя, которое разработчик выбирает для образа, а
`<path_to_project_directory>` - путь к корневой директории проекта.
- Запуск Docker-контейнера: выполняем команду для запуска Docker-контейнера 
на основе образа. Пример команды:
```
docker run -p <host_port>:<container_port> <image_name>
```
где `<host_port>` - порт на хостовой машине, через который будет доступен контейнер, 
`<container_port>` - порт в контейнере, который прослушивается приложением, а 
`<image_name>`- имя ранее созданного Docker-образа.
Например, для запуска веб-приложения на порту 8000 можем выполнить следующую команду:
```
docker run -p 8000:8000 myapp
```
Теперь Docker-контейнер будет запущен и приложение будет доступно по адресу `http://localhost:8000`.