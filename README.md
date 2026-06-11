# libary_api

## projekt description
````
המערכת צריכה ליצור אפשרות לניהול ספריה
מטפלת בניהול של ספרים ומנויים עדכון והוספה 
הבקשות יקרו דרך בקשות http בלבד 
דרך חיבור למסד sql 
## docker code run
````
docker run --name libary-mysql
-e MYSQL_DATABASE=libary_db 
-p 3306:3306 
-d mysql:8
## folder structure
````
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
````
## Table structure
## table books
````
id,title,author,gener,is_available,borrowed_by_member_id
````
## table members
````
id,name,email,is_active,total_borrows
````
## role system
````
1.יצירת ספר המשתמש שולח enre/author/title המערכת מוסיפה
is_available=True, borrowed_by=NULL
2.כל ערך חייב להיות Fiction / Non-Fiction / Science / History / Other
אחר מחזיר שגיאה ערך  
יש לוודא הן בהוספה או בעידכון
3.יצירת מנוי המשתמש שולח name/email המערכת מוסיפה is_active=True
total_borrows=0
4.email חייב להיות ייחודי אם קיים מחזיר שגיאה
5.מנוי ל א פעיל אם is_active=False אי אפשר להשאיל ספר
6. ספר לא זמין אם is_available=False אי אפשר להשאיל
7. מנוי לא יכול להחזיק יותר מ3 ספרים
8. החזרת ספר מתאפשרת רק אם הוא מושאל לאותו חבר שמחזיק בו
````
##  endpoint list
````
post | /books
get | /books
get | /books {id}
put | /books {id}
put | /books {id} borrow/ {member_id}
put | /books/{id}/return/ {member_id}
post | /members
get | /members
get | /members / {id}
put | /members /{id}
put | /members {id}/deactivate
put | /members /{id}/activate
get | reports/summary
get | / reports/book_by_gener
get | /reports/top_member
````
## flow system
````
המערכת צריכה ליצור חבר על ידי בקשת post עם השדות המתאימים
מערכת צריכה ליצור ספר על ידי בקשת post עם השדות המתאימים
המערכת עושה פעולת השאלה על ידי בקשת put לפי פרטי ספר וחבר 
המערכת מוודאת is_available = False
borrowed_by_member_id = member_id
total_borrows + 1
המערכת מחזירה ספר בבקשת put על ידי שדות של חבר וספר
המערכת מוודאת  is_available = True
borrowed_by_member_id = NULL
total borrows נשאר ללא שינוי
````
## requirment run
````
תעשה clone לקובץ
תעלה את הdocker 
תריץ את הפקודות
docker run --name libary-mysql\
-e MYSQL_ROOT_PASSWORD=user \
-e MYSQL_DATABASE=libary_db \
-p 3306:3306 \
-d mysql:8
תבדוק שהdocker רץ
docker ps
תריץ חיבור 
docker exec -it libary-mysql mysql -uroot -user
docker start 
uvicorn run main.app app --relode
