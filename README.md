# ExtraCredit

ExtraCredit lets Ontario Tech students buy and sell secondhand items for pickup at North Oshawa or Downtown Oshawa.

## What you need

- Python 3.12 or 3.13
- MySQL 8.4, either installed on your computer or running in Docker
- Internet access for the first install and the live weather button

Unzip the source code. Open a terminal in the `ExtraCredit` folder, where you can see `requirements.txt`.

## 1. Set up Python

On Linux or macOS:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

If you installed Python 3.13 on Windows, use `py -3.13` in the first command.

## 2. Start MySQL

If you use Docker, open Docker first. Run this as one line:

```sh
docker run -d --name extracredit-mysql -p 127.0.0.1:3307:3306 -e MYSQL_ROOT_PASSWORD=ExtraCreditRoot123 -e MYSQL_ROOT_HOST=% -e MYSQL_DATABASE=extra_credit -e MYSQL_USER=extra_credit_app -e MYSQL_PASSWORD=ExtraCreditDB123 mysql:8.4
```

Open `.env` in a text editor and set `DB_PORT=3307` and `DB_PASSWORD=ExtraCreditDB123`. Run `docker logs extracredit-mysql --tail 15` and wait for MySQL to say it is ready on port 3306. The passwords in this command are for the local demo.

If MySQL 8.4 is already installed, start it and run the following in MySQL Workbench or the `mysql` prompt as an administrator:

```sql
CREATE DATABASE IF NOT EXISTS extra_credit CHARACTER SET utf8mb4;
CREATE USER IF NOT EXISTS 'extra_credit_app'@'127.0.0.1' IDENTIFIED BY 'ExtraCreditDB123';
GRANT ALL PRIVILEGES ON extra_credit.* TO 'extra_credit_app'@'127.0.0.1';
```

For installed MySQL, leave `DB_PORT=3306` in `.env` and set `DB_PASSWORD=ExtraCreditDB123`. If the app user already exists, enter its current password instead.

## 3. Load the sample data and run the app

On Linux or macOS:

```sh
python -m flask --app extracredit init-db
python -m flask --app extracredit seed-demo
python -m flask --app extracredit run
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m flask --app extracredit init-db
.\.venv\Scripts\python.exe -m flask --app extracredit seed-demo
.\.venv\Scripts\python.exe -m flask --app extracredit run
```

When `seed-demo` asks for a password twice, enter `ExtraCreditDemo123` both times. It may stay blank while you type. This sets the same password for all three demo accounts:

- `alex@example.com` can post listings and respond to pickup requests.
- `priya@example.com` can browse and make pickup requests.
- `admin@example.com` can open reports and manage categories.

Open http://127.0.0.1:5000 in your browser. Leave the terminal running. After the first setup, start MySQL and run only the final Flask command to reopen the app. If you used Docker, run `docker start extracredit-mysql` to start the existing database.

## What to try

1. **Sign in and register.** Visit `http://127.0.0.1:5000/listings` while signed out. It should take you to Sign in. On Register, try an `@example.com` address and check that it is rejected. Try a made-up `@ontariotechu.net` address, choose an ExtraCredit password of at least 12 characters, and tick the student box. Open the link in the newest `student-*.txt` file in `instance/verification/`. Enter the ExtraCredit password again to confirm the account. The local demo saves the link in that folder.
2. **Search and post.** Sign in as Alex. Search for `textbook` and filter by North Oshawa. Open My listings, choose New listing, and create an item at either campus. Edit its price and save. Both saves stay on the same page. Try uploading a small JPG or PNG and removing it.
3. **Arrange pickup.** Sign in as Priya and open Alex’s new listing. Choose a pickup spot and a future date. In Inquiries, open Outgoing to edit the request. Sign in as Alex and open Incoming to accept it. The listing becomes Reserved. In My listings, try Mark sold and Remove.
4. **Try the account page.** Sign in with the account you registered, open Account, and change the name. If you want to test deactivation, use that new account. Enter its password and check that it signs you out.
5. **Check the weather.** As either demo student, open Pickup weather and choose Get and save Oshawa forecast. Check that it appears in Recent forecasts. Refresh the page to confirm the app saved it.
6. **Check reports and categories.** Sign in as Admin. Open Reports and visit Catalog reports and Activity reports. There are five tables on each page and a chart on Catalog reports. Download a CSV and PDF. Open Categories, add a test category, rename it, and remove it.

## If something goes wrong

- If MySQL is unavailable, check that it is running and that `DB_PORT` and `DB_PASSWORD` match the values you used.
- If seeding says the database already has data, it was already set up. Run the app and sign in with the password used the first time.
- If port 5000 is busy, set `PUBLIC_URL=http://127.0.0.1:5050` in `.env`, then add `--port 5050` to the Flask run command. Open http://127.0.0.1:5050 in your browser.
- The live weather button needs an internet connection.

## Run the automated tests (optional)

For the Docker setup above, use the following from the ExtraCredit folder. For installed MySQL, use its port and an administrator account that can create test databases.

Linux or macOS:

```sh
python -m pip install -r requirements-dev.txt
RUN_DB_TESTS=1 TEST_DB_PORT=3307 TEST_DB_PASSWORD=ExtraCreditRoot123 python -m pytest -q
```

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
$env:RUN_DB_TESTS = "1"
$env:TEST_DB_PORT = "3307"
$env:TEST_DB_PASSWORD = "ExtraCreditRoot123"
.\.venv\Scripts\python.exe -m pytest -q
```

The tests use MySQL's `root` account by default. Set `TEST_DB_USER` if your administrator username is different. The tests create and remove their own test databases.
