# Rutabaga
In-memory NoSQL база данных ключ-значение

*Выполнено для практической работы по дисциплине 
"Тестирование и верификация программного обеспечения"*

Содержит в себе много преднамеренных ошибок

Следуя идее микросервисной архитектуры, работает в отдельной контейнере
и общается с внешним миром через RESTful API

## Запуск

Для запуска приложения выполните следующую команду в корне проекта

```shell
docker-compose up --build
```

Приложение будет доступно по адресу [localhost:8080](localhost:8080)

Подробное описание методов и интерфейс взаимодействия
представлено в [спецификации](specification.md)

После запуска сервиса с его OpenAPI спецификацией
можно ознакомиться по ссылке: [localhost:8080/docs](localhost:8080/docs) 