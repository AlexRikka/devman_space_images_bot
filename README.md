# Собираем фотографии на космическую тематику
Данный репозиторий представляет из себя набор python скриптов для скачивания фотографий космоса с различных ресурсов в локальную папку.

## Как установить
Скачайте репозиторий и установите Python пакеты из `requirements.txt`:
```bash
git clone https://github.com/AlexRikka/devman_space_images_bot.git
cd devman_space_images_bot
pip install -r requirements.txt
```
Для взаимодействия с API сервисов необходимо получить их API токены. Создайте в папке с проектом файл `.env` и добавляйте токены в него, вот так:
```
NASA_ACCESS_KEY=<ваш токен>
```
Все скрипты запускаются в командной строке. 
```
python <название скрипта.py> 
```

## Основные скрипты

**fetch_spacex_images.py**  
Скачивает фото запуска ракет SpaceX с помощью [SpaceX API](https://github.com/r-spacex/SpaceX-API). При запуске скрипта принимает в качестве аргумента в командной строке id запуска. Если id не указать, то скачаются фото последнего запуска, если они есть.
Например:
```
python fetch_spacex_images.py 5eb87ce4ffd86e000604b337 
```

**fetch_nasa_apod_images.py**  
Скачивает фото на космическую тематику с сайта [NASA API APOD](https://api.nasa.gov/#apod). Чтобы воспользоваться NASA API необходимо получить API токен на этом же сайте.

**fetch_nasa_epic_images.py**  
Скачивает фото планеты Земля с сайта [NASA API EPIC](https://api.nasa.gov/#epic). Чтобы воспользоваться NASA API необходимо получить API токен на этом же сайте.

