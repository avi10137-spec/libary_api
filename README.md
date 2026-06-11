# libary_api

## projekt description
````
The system should create a library management option
Handles the management of books and subscriptions, updating and adding 
Requests will be made via http requests only 
Through a connection to a sql database
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
.yetzirat sper hameshtamesh shulch enre/author/title hama'arkat musifa
is_available=True, borrowed_by=NULL
2.kel arech hayev lehayot Fiction / Non-Fiction / Science / History / Other
achar mechzir shgi'a arech  
yesh levade hen behosfa o be'idkun
3.yetzirat menuy hameshtamesh shulch name/email hama'arkat musifa is_active=True
total_borrows=0
4.email hayev lehayot yihudi am kiyim mechzir shgi'a
5.menuy le a pa'il am is_active=False i efsher lehish'il sper
6. sper le zmin am is_available=False i efsher lehish'il
7. menuy le yechul lehachzik yoter me3 sifrim
8. hachzeret sper mitafshret rek am hu mushe'el le'uto haver shmachzik bo
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
The system should create a member by requesting a post with the appropriate fields
The system should create a book by requesting a post with the appropriate fields
The system performs a query by requesting a put with the details of the book and member
The system verifies is_available = False
borrowed_by_member_id = member_id
total_borrows + 1
The system returns a book by requesting a put with the fields of the member and book
The system verifies is_available = True
borrowed_by_member_id = NULL
total borrows remains unchanged
````
## requirment run
````
Clone the file
Upload the docker 
Run the commands
docker run --name libary-mysql\
-e MYSQL_ROOT_PASSWORD=user \
-e MYSQL_DATABASE=libary_db \
-p 3306:3306 \
-d mysql:8
Check that docker is running
docker ps
Run a connection 
docker exec -it libary-mysql mysql -uroot -user
docker start 
uvicorn run main.app app --relode
run the server :
http:/127.0.0.1:8000/docs
````