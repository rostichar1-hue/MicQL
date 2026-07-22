# MicroCode (MC)

**Самый короткий и безопасный язык запросов**

---

## Примеры

```mc
u.n,a(>18)50          # SELECT name, age FROM users WHERE age>18 LIMIT 50
+u{1,"John",30}       # INSERT INTO users VALUES(1,'John',30)
u.a=31(i=1)           # UPDATE users SET age=31 WHERE id=1
-u(i=4)!              # DELETE FROM users WHERE id=4
u#                    # SELECT COUNT(*) FROM users
