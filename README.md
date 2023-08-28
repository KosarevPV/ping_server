# Тестовое задание на позицию программист/разработчик Python в ООО Смарт Закупки
### Косарев Павел
___
Для запуска проекта в ОС должен быть установлен Git, Docker, Docker Compose.

Далее необходимо выполнить следующие команды:
+ git clone https://github.com/KosarevPV/ping_server.git
+ cd ping_server
+ sudo docker-compose -f docker-compose.yml up -d --build

___
### Технологический стек
+ Python 3.11.5 
+ Django 4.2
+ DRF 3.14.0
+ PostgreSQL 15.4
+ JS-фреймворк: React
+ Docker

___

### Краткое описание работы с системой
Раз в N секунд список доменов пингуется. N определяется в django.settings. Значение по умолчанию – 600.

Домены пингуются, с помощью периодических задач celery.

Отклики складываются в БД. По данным из БД строиться таблица откликов в
миллисекундах. Таблица доступна по URL /chart/. Отдача данных реализована через API на DRF. Таблица
обновляется автоматически раз в 30 секунд без полной перегрузки страницы.

#### Не удалось реализовать
+ Иметь возможность сохранять список доменов в БД через админпанель Django (при переходе по URL /admin/ и попытке 
  авторизации в ответ получаю ошибку 403, скорее всего нужно правильно настроить nginx)
+ Не удалось построить диаграмму, пытался построить диаграмму с помощью react-chartjs-2, но из-за изменения данных 
  во время передачи в диаграмму, не получилось добиться стабильной работы диаграммы.

