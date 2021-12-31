# BDS-library

## Autor:   Vojtěch Vaculík
## Předmět: BDS - Bezpečnost Databázových Systémů
## Ročník : BPC-IBE 2
------------------------------------
1. Download and setup PostgreSQL 
[https://www.enterprisedb.com/downloads/postgres-postgresql-downloads]
   and pgAdmin
[https://www.pgadmin.org/download/]

# ------------------------------------
2. Add pgAdmin to *Paths*

File -> Preferences -> Binary paths -> Add pgAdmin paths

Set:
- Serv. n.: (pref.: library)
- Host    : localhost
- Username: postgres
- Password: postgres

Create a database named library and restore it from the file named 'library'

# ------------------------------------
3. Install used python libs.
**psycopg2** 
=> pip install -U psycopg2

**bcrypt**
=> pip install -U bcrypt

**pillow**
=> pip install -U pillow

# ------------------------------------
4. Start the application and Log in

You can choose from 3 different types.

Admin     - Username: Kibi
            Password: password
            
Employee  - Username: Walker
            Password: password

Customer  - Username: Brunchie
            Password: password

Each one of them have different tools at their disposal.

# ------------------------------------
5. Back-up script

- Location of PostgreSQL folders must be set in *Path*
=> C:\Program Files\PostgreSQL\14\bin
=> C:\Program Files\PostgreSQL\14\lib

- Script (located in ExternalDocuments), needs to be added to task scheduler
  and se to midnight. Pictures have been added for demonstration.

Script contents
=> ```bat
=> set PGPASSWORD=postgres
=> pg_dump -h "localhost" -U "postgres" -f "C:\Windows\Temp\library" "librarydb"
=> ```

# ------------------------------------
6. Licenses can be found either in [Licence] or [licenses_generated.html]

------------------------------------

© 2021 Vojtěch Vaculík
Licensed under the [MIT License] -> (LICENCE)

