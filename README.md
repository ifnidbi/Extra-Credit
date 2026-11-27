# ExtraCredit

A secondhand marketplace for Ontario Tech University students, with pickup at North Oshawa and Downtown Oshawa.

## Run locally

You need Python 3.12 or 3.13 and MySQL 8.4. Unzip the project and open a terminal in the `ExtraCredit` folder.

### 1. Set up Python

**Linux or macOS**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

For Python 3.13 on Windows, use `py -3.13` in the first command.

### 2. Start MySQL

If you use Docker, start it and run this line.

```sh
docker run -d --name extracredit-mysql -p 127.0.0.1:3307:3306 -e MYSQL_ROOT_PASSWORD=ExtraCreditRoot123 -e MYSQL_ROOT_HOST=% -e MYSQL_DATABASE=extra_credit -e MYSQL_USER=extra_credit_app -e MYSQL_PASSWORD=ExtraCreditDB123 mysql:8.4
```

Run `docker logs extracredit-mysql --tail 15` and wait for MySQL to be ready on port 3306. Set `DB_PORT=3307` and `DB_PASSWORD=ExtraCreditDB123` in `.env`.

If MySQL is already installed, start it and run this in Workbench as an administrator.

```sql
CREATE DATABASE IF NOT EXISTS extra_credit CHARACTER SET utf8mb4;
CREATE USER IF NOT EXISTS 'extra_credit_app'@'127.0.0.1' IDENTIFIED BY 'ExtraCreditDB123';
GRANT ALL PRIVILEGES ON extra_credit.* TO 'extra_credit_app'@'127.0.0.1';
```

Set `DB_PASSWORD=ExtraCreditDB123` in `.env`, or use the user's current password if the MySQL user already exists. The default port is 3306.

### 3. Run the app

On Windows, use `.\.venv\Scripts\python.exe` in place of `python` in these three commands.

```sh
python -m flask --app extracredit init-db
python -m flask --app extracredit seed-demo
python -m flask --app extracredit run
```

Enter `ExtraCreditDemo123` twice when asked to set the demo password. Open http://127.0.0.1:5000 and leave the terminal running.

Use that password with `alex@example.com` (seller), `priya@example.com` (buyer), or `admin@example.com` (admin).

## What to try

1. **Registration.** Try an outside email, then a made-up `@ontariotechu.net` address with a password of at least 12 characters. Open the link in the newest file in `instance/verification/` and enter that password again.
2. **Listings.** As Alex, search for a textbook at North Oshawa. Add a listing, edit its price, and upload or remove a photo.
3. **Pickup.** As Priya, open Alex’s listing and request a campus pickup for a future date. Edit the request in Outgoing. As Alex, accept it in Incoming, then mark the listing sold or remove it.
4. **Account and weather.** Edit your name in Account. Try deactivation with the account you registered. On Pickup weather, save the Oshawa forecast. Weather needs internet access.
5. **Reports.** As Admin, open Catalog reports and Activity reports to see the ten tables. The chart is under Catalog reports. Download a CSV and PDF. Try adding, renaming, and removing a test category.

## Restart or fix setup

- To reopen the app, start MySQL and run the last Flask command again. Docker users can run `docker start extracredit-mysql`.
- If MySQL gives an error, check the port and password in `.env`. Run `seed-demo` once per empty database.
- If port 5000 is busy, set `PUBLIC_URL=http://127.0.0.1:5050` in `.env` and add `--port 5050` to the Flask run command.
