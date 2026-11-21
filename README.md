# Movies Store

Movies Store is a Django web app that simulates shopping for movies. Browse the catalog, search by title, read and write reviews, and place a demo order.

## Features

- Browse movie details, including posters, descriptions, prices, and reviews.
- Sign up, sign in, and manage your own reviews.
- Choose quantities, add movies to a session-based cart, and see the order total.
- Place a demo order and view past purchases. Checkout records orders in SQLite without processing payments.
- Manage movies and reviews through Django admin.

## Run locally

Use Python 3.12 and Git. Clone the repository and create a virtual environment.

```bash
git clone https://github.com/IshaMadanu/moviesstore.git
cd moviesstore
python -m venv .venv
```

Activate the environment for your shell.

| Shell | Command |
| --- | --- |
| macOS or Linux | `source .venv/bin/activate` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |

Install the dependencies, apply migrations, and start the development server.

```bash
python -m pip install "Django>=5.0,<5.1" Pillow PyMySQL
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The repository includes a SQLite database with sample movies and their poster images. PyMySQL is required by the project's startup import. The default setup uses SQLite and works without a MySQL server.

## Add movies through Django admin

```bash
python manage.py createsuperuser
```

Sign in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to add or edit movies and upload posters.

## Project structure

| Path | Purpose |
| --- | --- |
| `home/` | Home and About pages |
| `movies/` | Catalog, title search, movie details, and reviews |
| `accounts/` | Registration, authentication, and order history |
| `cart/` | Session cart, checkout, and order items |
| `moviesstore/` | Django settings, URL routing, shared templates, and static assets |
| `media/movie_images/` | Movie posters |

The interface uses Django templates, Bootstrap 5, and custom CSS.
