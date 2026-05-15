import sqlite3
import csv

# Создание и подключение к БД
connection = sqlite3.connect('games.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Удаление старых таблиц
cursor.execute("DROP TABLE IF EXISTS platforms")
cursor.execute("DROP TABLE IF EXISTS progress")
cursor.execute("DROP TABLE IF EXISTS games")

# Таблица 1: Платформы
cursor.execute("""CREATE TABLE platforms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT NOT NULL
    )
    """)

# Таблица 2: Прогресс (с добавленными полями username, age, password)
cursor.execute("""CREATE TABLE progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    hours_played INTEGER,
    rating INTEGER,
    username TEXT NOT NULL,
    age INTEGER,
    password TEXT NOT NULL
    )
    """)

# Таблица 3: Игры
cursor.execute("""CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    platform_id INTEGER NOT NULL,
    genre TEXT NOT NULL,
    year INTEGER NOT NULL,
    progress_id INTEGER,
    FOREIGN KEY (platform_id) REFERENCES platforms(id),
    FOREIGN KEY (progress_id) REFERENCES progress(id)
    )
    """)

#Через случайные комбинации
progress_array = [
    ('Completed', 45.5, 9, 'alice123', 25, 'pass1234'),
    ('In Progress', 12.0, 8, 'bob_gamer', 19, 'gaming456'),
    ('Dropped', 3.0, 4, 'charlie7', 31, 'charlie789'),
    ('In Progress', 15.8, 8, 'diana_cool', 22, 'diana321'),
    ('On Hold', 8.5, 7, 'eve_win', 28, 'eve2024'),
    ('In Progress', 56.0, 7, 'frank_o', 35, 'frank123'),
    ('Completed', 25.0, 9, 'grace_lee', 18, 'grace555'),
    ('In Progress', 15.5, 8, 'hank_hank', 42, 'hank777'),
    ('Completed', 60.0, 9, 'iris_sky', 27, 'iris888'),
    ('Dropped', 5.5, 5, 'jack_black', 33, 'jack999'),
    ('Not Started', 0.0, 8, 'kate_win', 21, 'kate111'),
    ('Completed', 30.0, 10, 'leo_messi', 29, 'leo222'),
    ('In Progress', 20.0, 7, 'mia_wong', 24, 'mia333'),
    ('On Hold', 2.5, 6, 'nick_young', 37, 'nick444'),
    ('Completed', 55.0, 8, 'olivia_p', 26, 'olivia555'),
    ('In Progress', 17.0, 4, 'paul_art', 41, 'paul666'),
    ('In Progress', 10.0, 9, 'quincy_q', 20, 'quincy777'),
    ('Completed', 40.0, 8, 'rose_garden', 30, 'rose888'),
    ('Dropped', 1.0, 3, 'sam_smith', 45, 'sam999'),
    ('Completed', 70.5, 10, 'tina_fey', 32, 'tina000'),
    ('In Progress', 18.0, 7, 'ursula_k', 23, 'ursula111'),
    ('Completed', 22.5, 9, 'victor_h', 38, 'victor222'),
    ('On Hold', 6.0, 8, 'wendy_b', 34, 'wendy333'),
    ('In Progress', 14.0, 5, 'xavier_x', 39, 'xavier444'),
    ('In Progress', 19.0, 8, 'yara_z', 36, 'yara555'),
    ('In Progress', 45.0, 9, 'zack_lee', 40, 'zack666'),
    ('Completed', 35.0, 7, 'amy_adams', 17, 'amy777'),
    ('Dropped', 2.0, 5, 'brian_cox', 44, 'brian888'),
    ('Completed', 90.0, 9, 'chris_evans', 43, 'chris999'),
    ('In Progress', 8.0, 6, 'david_ten', 46, 'david000')
]

cursor.executemany(""" 
    INSERT INTO progress (status, hours_played, rating, username, age, password) 
    VALUES (?, ?, ?, ?, ?, ?)
""", progress_array)

platform_array = [
    ('PlayStation 5', 'Sony'),
    ('Xbox Series X', 'Microsoft'),
    ('Nintendo Switch', 'Nintendo'),
    ('PC', 'Various'),
    ('PlayStation 4', 'Sony'),
    ('Xbox One', 'Microsoft'),
    ('Nintendo 3DS', 'Nintendo'),
    ('Steam Deck', 'Valve'),
    ('PlayStation 3', 'Sony'),
    ('Xbox 360', 'Microsoft'),
    ('Wii U', 'Nintendo'),
    ('Mobile (iOS)', 'Apple'),
    ('Mobile (Android)', 'Google'),
    ('PlayStation Vita', 'Sony'),
    ('Nintendo Wii', 'Nintendo'),
    ('Sega Genesis', 'Sega'),
    ('Super Nintendo', 'Nintendo'),
    ('Game Boy Advance', 'Nintendo'),
    ('Dreamcast', 'Sega'),
    ('Nintendo 64', 'Nintendo'),
    ('PlayStation 2', 'Sony'),
    ('Xbox', 'Microsoft'),
    ('GameCube', 'Nintendo'),
    ('Atari 2600', 'Atari'),
    ('Commodore 64', 'Commodore'),
    ('Sega Saturn', 'Sega'),
    ('Neo Geo', 'SNK'),
    ('PlayStation Portable', 'Sony'),
    ('Nintendo DS', 'Nintendo')
]

cursor.executemany(""" 
    INSERT INTO platforms (name, company) VALUES (?, ?)
""", platform_array)

games_array = [
    ('Elden Ring', 1, 'RPG', 2022, 1),
    ('Halo Infinite', 2, 'FPS', 2021, 2),
    ('Zelda: Breath of the Wild', 3, 'Adventure', 2017, 4),
    ('Cyberpunk 2077', 4, 'RPG', 2020, 3),
    ('God of War Ragnarök', 5, 'Action', 2022, 5),
    ('Forza Horizon 5', 6, 'Racing', 2021, 6),
    ('Pokémon X', 7, 'RPG', 2013, 7),
    ('Vampire Survivors', 8, 'Action', 2022, 8),
    ('The Last of Us', 9, 'Action-Adventure', 2013, 9),
    ('Gears of War 3', 10, 'TPS', 2011, 10),
    ('Mario Kart 8', 11, 'Racing', 2014, 11),
    ('Genshin Impact', 12, 'RPG', 2020, 12),
    ('PUBG Mobile', 13, 'Battle Royale', 2018, 13),
    ('Persona 4 Golden', 14, 'RPG', 2012, 14),
    ('Super Mario Galaxy', 15, 'Platformer', 2007, 15),
    ('Sonic the Hedgehog 2', 16, 'Platformer', 1992, 16),
    ('Chrono Trigger', 17, 'RPG', 1995, 17),
    ('Metroid Fusion', 18, 'Metroidvania', 2002, 18),
    ('Shenmue', 19, 'Adventure', 1999, 19),
    ('Super Mario 64', 20, 'Platformer', 1996, 20),
    ('Final Fantasy X', 21, 'RPG', 2001, 21),
    ('Fable', 22, 'RPG', 2004, 22),
    ('Resident Evil 4', 23, 'Horror', 2005, 23),
    ('Pitfall!', 24, 'Platformer', 1982, 24),
    ('Maniac Mansion', 25, 'Adventure', 1987, 25),
    ('Panzer Dragoon Saga', 26, 'RPG', 1998, 26),
    ('Metal Slug 3', 27, 'Run and Gun', 2000, 27),
    ('God of War: Chains of Olympus', 28, 'Action', 2008, 28),
    ('Castlevania: Dawn of Sorrow', 29, 'Metroidvania', 2005, 29)
]

cursor.executemany(""" 
    INSERT INTO games (title, platform_id, genre, year, progress_id) 
    VALUES (?, ?, ?, ?, ?)
""", games_array)


# Закрытие соединения
connection.commit()
connection.close()