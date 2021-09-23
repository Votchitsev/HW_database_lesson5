import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://votchitsev:55555@localhost:5432/Music_Platform')
connection = engine.connect()

# Запрос № 1  "Количество исполнителей в каждом жанре"

select_one = connection.execute("""
            SELECT g.name, COUNT(a.id) FROM genre g
            JOIN artistgenre ag ON g.id = ag.genre_id
            JOIN artist a ON ag.artist_id = a.id
            GROUP BY g.name;""").fetchall()
print('Запрос № 1 - ', select_one)


# Запрос № 2 "Количество треков, вошедших в альбомы 2019-2020 годов"

select_two = connection.execute("""
            SELECT COUNT(t.id) FROM track t
            JOIN album a ON t.albumid = a.id
            WHERE a.release_year = 2019 OR a.release_year = 2020;
            """).fetchone()
print('Запрос № 2 - ', select_two)


# Запрос № 3 "Средняя продолжительность треков по каждому альбому"

select_three = connection.execute("""
             SELECT a.album_title, ROUND(AVG(t.len), 0) FROM album a
             JOIN track t ON a.id = t.albumid
             GROUP BY a.album_title""").fetchall()
print('Запрос № 3 - ', select_three)


# Запрос № 4 "Все исполнители, которые не выпустили альбомы в 2020 году"

select_four = connection.execute("""
            SELECT a.name FROM artist a
            JOIN artistalbum aa ON a.id = aa.artist_id
            JOIN album al ON aa.album_id = al.id
            WHERE al.release_year != 2021
            GROUP BY a.name;
            """).fetchall()
print('Запрос № 4 - ', select_four)

# Запрос № 5 "Названия сборников, в которых присутствует конкретный исполнитель (выберите сами)"

select_five = connection.execute("""
            SELECT c.name FROM collection c
            JOIN trackcollection tc ON c.collection_id = tc.collection_id
            JOIN track t ON tc.track_id = t.id
            JOIN album a ON a.id = t.albumid
            JOIN artistalbum aa ON a.id = aa.album_id
            JOIN artist ar ON aa.artist_id = ar.id
            WHERE ar.name = 'Nirvana'
            GROUP BY c.name""").fetchall()
print('Запрос № 5 - ', select_five)
