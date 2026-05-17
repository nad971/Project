 Проект "Исследование кибербезопасности"

Структура базы данных

База данных состоит из следующих таблиц:

1.Таблица платформ :

· id

· название

· компания-производитель

2.Таблица прогресса :

· id

· статус игры

· сыграно часов

· оценка

3.Таблица игр

· id

· название игры

· id платформы

· жанр

· год выпуска

· id прогресса

4.Таблица пользователей

· id

· логин

· пароль

Отображение в интерфейсе SQL

Таблица platforms 
<img width="1044" height="851" alt="Снимок экрана (6)" src="https://github.com/user-attachments/assets/6fbef4bc-c799-436c-a8f9-6167c67ac2e6" />

Таблица progress 
<img width="1056" height="858" alt="Снимок экрана (7)" src="https://github.com/user-attachments/assets/7a4b8a19-a2f5-42a3-9423-8c4aa7df8c08" />

Таблица games 
<img width="1048" height="857" alt="Снимок экрана (8)" src="https://github.com/user-attachments/assets/773c0a3b-3e22-4c90-9ad0-295bd21ed42d" />

Таблица users
<img width="1061" height="856" alt="Снимок экрана (9)" src="https://github.com/user-attachments/assets/4cb42c72-7026-4327-9f2d-fddd1e9780d5" />

ВИДЫ SQL-ИНЪЕКЦИЙ 

1. UNION-атака

Цель: получить данные из другой таблицы, которую не должны видеть.
<img width="770" height="107" alt="Снимок экрана (10)" src="https://github.com/user-attachments/assets/44f015ea-69f5-4642-9596-8b65829c7708" />

Выполнится:

<img width="1046" height="856" alt="Снимок экрана (11)" src="https://github.com/user-attachments/assets/83b497ac-7d0f-4471-bcc9-22169db50300" />

Результат: злоумышленник получил все логины и пароли из таблицы users

2.Утечка скрытых данных

Цель: получить игры, которые не должны отображаться (например, удалённые или скрытые).

<img width="608" height="219" alt="Снимок экрана (12)" src="https://github.com/user-attachments/assets/721bd4c3-6973-4f00-9d20-d54163dc8e6c" />

Выполнится:

<img width="1034" height="771" alt="Снимок экрана (13)" src="https://github.com/user-attachments/assets/9678c766-feb1-4ef5-a087-b2d20cec20bb" />

Результат: покажутся все игры, включая Dropped и On Hold, которые обычно скрыты в интерфейсе.

3. Обход логики (авторизация без пароля)

Цель: войти в систему, не зная пароля.

<img width="823" height="137" alt="Снимок экрана (14)" src="https://github.com/user-attachments/assets/f6be7d2e-3457-41b6-b97e-7a5d8b336e6c" />

Выполнится:

<img width="676" height="45" alt="Снимок экрана (15)" src="https://github.com/user-attachments/assets/05b98763-a27c-4df9-980d-3fd8313153dd" />

<img width="741" height="227" alt="Снимок экрана (16)" src="https://github.com/user-attachments/assets/5183f16f-8c6e-4ea5-95e6-fec2ca9f43ab" />

Результат: вход под admin без пароля.

4. Разведка БД

Цель: узнать структуру базы данных (названия таблиц, колонок).

<img width="666" height="69" alt="Снимок экрана (17)" src="https://github.com/user-attachments/assets/2144c4dd-739a-444d-8465-a464d9d267f1" />

Выполнится:

<img width="859" height="201" alt="Снимок экрана (18)" src="https://github.com/user-attachments/assets/7e6e1d29-c131-4c8a-98bd-5e58ea58fe63" />

<img width="1050" height="782" alt="Снимок экрана (19)" src="https://github.com/user-attachments/assets/9e9f0dfa-7eeb-4a81-8468-8a039933c103" />

Злоумышленник узнал:

· Есть колонки login и password
· Пароли хранятся в открытом виде

МЕТОДЫ ЗАЩИТЫ 

1. Параметризованные запросы

![Uploading Снимок экрана (20).png…]()













