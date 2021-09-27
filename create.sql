create table Genre(
	id serial primary key,
	name varchar (20) not null
);

create table Artist(
	id serial primary key,
	name varchar(30) not null
);


create table Album(
	id serial primary key,
	album_title varchar(40) not null,
	release_year date
);

create table track(
	id serial primary key,
	albumid integer references Album(id),
	track_title varchar(40) not null,
	len integer check(len < 9999) check(len > 0)
);

create table artistgenre(
	artist_id integer references artist(id),
	genre_id integer references genre(id),
	constraint pk_artistgenre primary key(artist_id, genre_id)
	);

create table artistalbum(
	artist_id integer references artist(id),
	album_id integer references album(id),
	constraint pk_artistalbum primary key(artist_id, album_id)
	);

create table collection(
	collection_id serial primary key,
	name varchar(40) not null,
	release_year integer check(release_year > 0) check(release_year < 2021)
	);
	
create table trackcollection(
	track_id integer references track(id),
	collection_id integer references collection(collection_id),
	constraint pk_trackcollection primary key(track_id, collection_id)
	);
	
alter table collection add column release_year integer check(release_year > 0) check(release_year <= 2021);

delete from track where id = 61;