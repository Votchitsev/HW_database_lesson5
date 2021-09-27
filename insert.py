import sqlalchemy
print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql://votchitsev:55555@localhost:5432/Music_Platform')
connection = engine.connect()

artist = [
    'Kaiser_Chiefs', 'Franz_Ferdinand', 'Led_Zeppelin', 'Nirvana',
    'FKJ', 'Jose_James', 'Blink-182', 'Massive_Attack'
]

genre = [
    'Indie', 'Hard_Rock', 'Grunge', 'Electronics',
    'Punk-rock', 'Jazz', 'Trip-Hop'
]

album = {
    'Duck': 2019,
    'Always_Acsending': 2018,
    'Led_Zeppelin_IV': 1971,
    'Nevermind': 1991,
    'Just_Piano': 2021,
    'Lean_On_Me': 2018,
    'California': 2016,
    'Helogoland': 2010,
}

for artist in artist:
    print(artist)
    connection.execute(f"INSERT INTO Artist(name)"
                       f"   VALUES ('{artist}');")

for genre in genre:
    print(artist)
    connection.execute(f"INSERT INTO Genre(name)"
                       f"   VALUES ('{genre}');")

artist_list = connection.execute("SELECT * FROM artist").fetchall()
print(artist_list)
genre_list = connection.execute("SELECT * FROM genre").fetchall()
print(genre_list)

artist_genre = {
    'Kaiser_Chiefs': 'Indie', 'Franz_Ferdinand': 'Indie', 'Led_Zeppelin': 'Hard_Rock', 'Nirvana': 'Grunge',
    'FKJ': 'Electronics', 'Jose_James': 'Jazz', 'Blink-182': 'Punk-rock', 'Massive_Attack': 'Trip-Hop'
}

for i in artist_genre.items():
    artist_id_select = connection.execute(f"SELECT id FROM artist WHERE name = '{i[0]}';").fetchone()
    artist_id = int(artist_id_select[0])
    genre_id_select = connection.execute(f"SELECT id FROM genre WHERE name = '{i[1]}';").fetchone()
    genre_id = int(genre_id_select[0])
    insert = connection.execute(f"INSERT INTO artistgenre VALUES({artist_id}, {genre_id});")
    print(insert)

for i in album.items():
    connection.execute(f"INSERT INTO album(album_title, release_year) VALUES('{i[0]}', {i[1]});")

artist_album = {
    'Kaiser_Chiefs': ['Duck'], 'Franz_Ferdinand': ['Always_Acsending'], 'Led_Zeppelin': ['Led_Zeppelin_IV'],
    'Nirvana': ['Nevermind'], 'FKJ': ['Just_Piano'], 'Jose_James': ['Lean_On_Me'], 'Blink-182': ['California'],
    'Massive_Attack': ['Helogoland']
}

for i in artist_album.items():
    artist_id = connection.execute(f"SELECT id FROM artist WHERE name = '{i[0]}';").fetchone()
    for j in i[1]:
        album_id = connection.execute(f"SELECT id FROM album WHERE album_title = '{j}';").fetchone()
        connection.execute(f"INSERT INTO artistalbum(artist_id, album_id) VALUES({artist_id[0]}, {album_id[0]});")


track = [
    {'track_name': 'People_Know_How_To_Love_One_Another',
     'album': 'Duck',
     'len': 216},
    {'track_name': 'Golden_Oldies',
     'album': 'Duck',
     'len': 244},
    {'track_name': 'Wait',
     'album': 'Duck',
     'len': 230},
    {'track_name': 'Always_Acsending',
     'album': 'Always_Acsending',
     'len': 321},
    {'track_name': 'Lazy_Boy',
     'album': 'Always_Acsending',
     'len': 179},
    {'track_name': 'Paper_Cages',
     'album': 'Always_Acsending',
     'len': 220},
    {'track_name': 'Black_Dog',
     'album': 'Led_Zeppelin_IV',
     'len': 296},
    {'track_name': 'Rock_And_Roll',
     'album': 'Led_Zeppelin_IV',
     'len': 221},
    {'track_name': 'The_Battle_of_Evermore',
     'album': 'Led_Zeppelin_IV',
     'len': 352},
    {'track_name': 'Smells_Like_Teen_Spirit',
     'album': 'Nevermind',
     'len': 301},
    {'track_name': 'In_Bloom',
     'album': 'Nevermind',
     'len': 255},
    {'track_name': 'Come_As_You_Are',
     'album': 'Nevermind',
     'len': 219},
    {'track_name': 'Sundays',
     'album': 'Just_Piano',
     'len': 213},
    {'track_name': 'Anthem',
     'album': 'Just_Piano',
     'len': 157},
    {'track_name': 'Last_Hour',
     'album': 'Just_Piano',
     'len': 163},
    {'track_name': 'Lean_On_Me',
     'album': 'Lean_On_Me',
     'len': 297},
    {'track_name': 'Cynical',
     'album': 'California',
     'len': 116},
    {'track_name': "She_is_out_Of_Her_Mind",
     'album': 'California',
     'len': 163},
    {'track_name': 'Bored_to_Death',
     'album': 'California',
     'len': 236},
    {'track_name': 'Prey_For_Rain',
     'album': 'Helogoland',
     'len': 404},
    {'track_name': 'Babel',
     'album': 'Helogoland',
     'len': 320},
    {'track_name': 'Splitting_The_Atom',
     'album': 'Helogoland',
     'len': 317}
]

for i in track:
    track_name = i['track_name']
    album_name = i['album']
    track_len = i['len']
    album_id = connection.execute(f"SELECT id FROM album WHERE album_title = '{album_name}';").fetchone()[0]
    print(album_id, track_name, track_len)
    connection.execute(f"INSERT INTO track(albumid, track_title, len) VALUES({album_id}, '{track_name}', {track_len})")


collection = [
    {'name': 'Chill',
     'year': 2019,
     'tracks': ['Sundays', 'Prey_For_Rain']},
    {'name': 'Rock',
     'year': 2020,
     'tracks': ['Bored_to_Death', 'Smells_Like_Teen_Spirit']},
    {'name': 'Electro',
     'year': 2019,
     'tracks': ['Babel', 'Anthem']},
    {'name': 'Indie',
     'year': 2018,
     'tracks': ['Golden_Oldies', 'Lazy_Boy']},
    {'name': 'Just_Hard',
     'year': 2017,
     'tracks': ['In_Bloom', 'Black_Dog', 'She_is_out_Of_Her_Mind']},
    {'name': 'New',
     'year': 2020,
     'tracks': ['Lean_On_Me', 'Sundays']},
    {'name': 'Under_Stars',
     'year': 2021,
     'tracks': ['Always_Acsending', 'Wait']},
    {'name': 'Ctrl_Alt',
     'year': 2021,
     'tracks': ['Splitting_The_Atom', 'Anthem']}
]

for i in collection:
    collection_name = i['name']
    collection_release = i['year']
    connection.execute(f"INSERT INTO collection(name, release_year) VALUES('{collection_name}', {collection_release})")

track_collection = []
for i in collection:
    collection_name = i['name']
    track = i['tracks']
    collection_id = connection.execute(f"SELECT collection_id FROM collection WHERE name = '{collection_name}'").\
        fetchone()[0]
    for j in track:
        track_id = connection.execute(f"SELECT id FROM track WHERE track_title = '{j}'").fetchone()[0]
        tc = (track_id, collection_id)
        track_collection.append(tc)

for i in track_collection:
    track_id = i[0]
    collection_id = i[1]
    connection.execute(f"INSERT INTO trackcollection VALUES({track_id}, {collection_id})")


connection.execute("""
            INSERT INTO artistgenre(artist_id, genre_id)
            VALUES(2, 5);
            """)
