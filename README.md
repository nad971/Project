 Проект по основам работы с базой данных "Игровая коллекция"

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

Утечка скрытых данных

Цель: получить игры, которые не должны отображаться (например, удалённые или скрытые).





