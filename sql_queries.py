# DROP TABLES FIRST

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE"
dim_user_table_drop = "DROP TABLE IF EXISTS dim_users CASCADE"
dim_song_table_drop = "DROP TABLE IF EXISTS dim_songs CASCADE"
dim_artist_table_drop = "DROP TABLE IF EXISTS dim_artists CASCADE"
dim_time_table_drop = "DROP TABLE IF EXISTS dim_time CASCADE"


# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY,
                         start_time TIME NOT NULL REFERENCES dim_time (start_time),
                         user_id INTEGER NOT NULL REFERENCES dim_users (user_id),
                         level VARCHAR,
                         song_id VARCHAR REFERENCES dim_songs (song_id),
                         artist_id VARCHAR REFERENCES dim_artists (artist_id),
                         session_id VARCHAR ,
                         location VARCHAR,
                         user_agent VARCHAR);""")


dim_user_table_create = ("""CREATE TABLE IF NOT EXISTS dim_users (user_id INTEGER PRIMARY KEY,
                    first_name VARCHAR,
                    last_name VARCHAR,
                    gender VARCHAR,
                    level VARCHAR);""")


dim_song_table_create = ("""CREATE TABLE IF NOT EXISTS dim_songs (song_id VARCHAR PRIMARY KEY,
                         title VARCHAR,
                         artist_id VARCHAR NOT NULL,
                         year INTEGER,
                         duration FLOAT);""")

dim_artist_table_create = ("""CREATE TABLE IF NOT EXISTS dim_artists (artist_id VARCHAR PRIMARY KEY,
                         name VARCHAR,
                         location VARCHAR,
                         lattitude VARCHAR,
                         longitude VARCHAR);""")

dim_time_table_create = ("""CREATE TABLE IF NOT EXISTS dim_time (start_time TIME PRIMARY KEY,
                         hour INTEGER,
                         day INTEGER,
                         week INTEGER,
                         month INTEGER,
                         year INTEGER,
                         weekday INTEGER);""")


# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

dim_user_table_insert = ("""INSERT INTO dim_users (user_id, first_name, last_name, gender, level)  
                    VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level""")

dim_song_table_insert = ("""INSERT INTO dim_songs (song_id, title, artist_id, year, duration)
                    VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

dim_artist_table_insert = ("""INSERT INTO dim_artists (artist_id, name, location, lattitude, longitude)
                    VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

dim_time_table_insert = ("""INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday)
                    VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT s.song_id AS song_id, a.artist_id AS artist_id
                FROM dim_songs s JOIN dim_artists a ON s.artist_id = a.artist_id
                WHERE s.title = (%s) OR a.name = (%s) OR s.duration = (%s)""")

# QUERY LISTS

create_table_queries = [dim_user_table_create, dim_song_table_create, dim_artist_table_create, dim_time_table_create, songplay_table_create]
drop_table_queries = [dim_user_table_drop, dim_song_table_drop, dim_artist_table_drop, dim_time_table_drop, songplay_table_drop]