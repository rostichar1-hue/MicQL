```markdown
# MicroCode (MC) — контекст проекта

## Что это

MicroCode (MC) — это минималистичный язык запросов, созданный как альтернатива SQL для небольших проектов, скриптов и встраиваемых систем.  
Он написан на Python, работает в Termux и обычном Linux, использует JSON для хранения данных.

**Главная идея:** делать 90% типовых запросов в 3-5 раз короче, чем на SQL, без потери читаемости и с сохранением данных в файл.

---

## Синтаксис (кратко)

```

CREATE table (field1 TYPE, field2 TYPE)   — создать таблицу
+table {value1, value2, value3}           — вставить строку
table:field1,field2(condition)limit       — выборка
SAVE                                      — сохранить всё в JSON
LOAD                                      — загрузить из JSON

```

**Пример файла `data.mc`:**

```

CREATE users (id INT, name STRING, age INT)
+users {1, "Alex", 28}
+users {2, "Kate", 22}
users:name(age>20)10
SAVE

```

---

## Почему это не SQL

| SQL | MicroCode |
|-----|-----------|
| `SELECT name FROM users WHERE age > 20 LIMIT 10` | `users:name(age>20)10` |
| `INSERT INTO users VALUES (1, 'Alex', 28)` | `+users {1, "Alex", 28}` |
| Требуется сервер БД | Работает с JSON-файлом |
| Сложный синтаксис | Минимум символов |

---

## Установка (Termux / Linux)

```bash
git clone https://github.com/rostichar1-hue/MicroCode.git
cd MicroCode
chmod +x install.sh
./install.sh
source ~/.bashrc
```

После установки доступна команда:

```bash
micro data.mc
```

---

Структура проекта

```
MicroCode/
├── cli.py          — точка входа
├── parser.py       — парсинг команд
├── executor.py     — выполнение команд, работа с данными
├── micro           — исполняемый файл
├── install.sh      — установочный скрипт
├── data.mc         — пример файла с запросами
├── README.md       — описание для пользователей
├── CONTEXT.md      — этот файл (для AI и разработчиков)
└── microcode_data.json — файл с сохранёнными данными (создаётся при SAVE)
```

---

Текущий статус

· ✅ Создание таблиц (CREATE)
· ✅ Вставка строк (+)
· ✅ Выборка с условиями (=, >, <)
· ✅ Сохранение в JSON (SAVE)
· ✅ Загрузка из JSON (LOAD)
· ✅ Команда micro работает после установки

---

Что в планах (опционально)

· Индексы для ускорения поиска
· JOIN между таблицами
· Асинхронные запросы
· GROUP BY и агрегации (COUNT, SUM, AVG)
· REST API для MicroCode
· Поддержка типов данных (INT, STRING, FLOAT, BOOL)

---

Почему этот файл здесь

CONTEXT.md нужен для:

· Быстрого входа в проект новых разработчиков
· Восстановления контекста в новом чате с AI
· Понимания структуры без чтения всего кода

---

Ссылки

· Репозиторий: https://github.com/rostichar1-hue/MicroCode
· Автор: rostichar1-hue
· Telegram: @darzx3
· Лицензия: MIT

---

Как использовать этот файл в новом чате с AI

Скопируй текст этого файла и отправь его в новый чат. AI сразу поймёт контекст и сможет помочь без уточнений.

---

Ключевые слова для поиска

microcode, mc-lang, query language, minimalistic sql, python database, termux queries, json storage

---

Финальное замечание

Этот файл — живой документ. Если ты добавляешь новую фичу, меняешь синтаксис или структуру — обнови его. Это сэкономит время тебе и тем, кто будет работать с проектом.

---

English version

What is this

MicroCode (MC) is a minimalist query language created as an alternative to SQL for small projects, scripts, and embedded systems.
It is written in Python, runs on Termux and standard Linux, and uses JSON for data storage.

The core idea: make 90% of typical queries 3-5 times shorter than SQL, without losing readability and with persistent file storage.

---

Syntax (short)

```
CREATE table (field1 TYPE, field2 TYPE)   — create table
+table {value1, value2, value3}           — insert row
table:field1,field2(condition)limit       — query
SAVE                                      — save everything to JSON
LOAD                                      — load from JSON
```

Example data.mc file:

```
CREATE users (id INT, name STRING, age INT)
+users {1, "Alex", 28}
+users {2, "Kate", 22}
users:name(age>20)10
SAVE
```

---

Why this is not SQL

SQL MicroCode
SELECT name FROM users WHERE age > 20 LIMIT 10 users:name(age>20)10
INSERT INTO users VALUES (1, 'Alex', 28) +users {1, "Alex", 28}
Requires a database server Works with JSON file
Complex syntax Minimal characters

---

Installation (Termux / Linux)

```bash
git clone https://github.com/rostichar1-hue/MicroCode.git
cd MicroCode
chmod +x install.sh
./install.sh
source ~/.bashrc
```

After installation the command is available:

```bash
micro data.mc
```

---

Project structure

```
MicroCode/
├── cli.py          — entry point
├── parser.py       — command parsing
├── executor.py     — command execution, data handling
├── micro           — executable file
├── install.sh      — installation script
├── data.mc         — example query file
├── README.md       — user documentation
├── CONTEXT.md      — this file (for AI and developers)
└── microcode_data.json — saved data file (created on SAVE)
```

---

Current status

· ✅ Create tables (CREATE)
· ✅ Insert rows (+)
· ✅ Query with conditions (=, >, <)
· ✅ Save to JSON (SAVE)
· ✅ Load from JSON (LOAD)
· ✅ micro command works after installation

---

Planned features (optional)

· Indexes for faster search
· JOIN between tables
· Async queries
· GROUP BY and aggregations (COUNT, SUM, AVG)
· REST API for MicroCode
· Data type support (INT, STRING, FLOAT, BOOL)

---

Why this file exists

CONTEXT.md is for:

· Fast onboarding for new developers
· Restoring context in a new AI chat
· Understanding the structure without reading all the code

---

Links

· Repository: https://github.com/rostichar1-hue/MicroCode
· Author: rostichar1-hue
· Telegram: @darzx3
· License: MIT

---

How to use this file in a new AI chat

Copy the text of this file and send it to a new chat. The AI will immediately understand the context and can help without further clarification.

---

Keywords for search

microcode, mc-lang, query language, minimalistic sql, python database, termux queries, json storage

---

Final note

This is a living document. If you add a new feature, change the syntax, or update the structure — update this file. It will save time for you and anyone working on the project.

```
