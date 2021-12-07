# postgres-python-test
A repo to test concurrent row updates . This is basically to performance test on  what happens if we want to update different rows concurrently in postgres. 
This will use python.

# steps to install pgAdmin, postgres and create db in macOS

1. install pgadmin4 from https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.2/macos/

2. check if u have postgres. if not, install with following

`brew update`
`brew install postgresql`

3. follow steps from here https://www.robinwieruch.de/postgres-sql-macos-setup/


4. create a db called somedb
`createdb somedb`

5. start pgadmin4 and it will ask master password as in the screen.

6. Right click servers -> create-> server, enter name in General for the server as local

7. Go to connection -- enter localhost in hostname, maintenance database to be somedb, username change it to ur macos username, password can be empty by default.

8. create a table-- Run the following query that creates `users` table in public schema. 

You can select Query tool icon ( first icon below File and run the query)

```
CREATE TABLE public.users
(
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL
);

ALTER TABLE IF EXISTS public.users
    OWNER to ur_username;
