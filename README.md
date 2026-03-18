# Gold Medal Statistics

Gold Medal Statistics is a web app for track and field coaches and athletes to input marks, 
calculate scores using the World Athletics Scoring Tables, and compare performance across 
events and athletes on a team.

<!-- Add screenshots here -->

## Features

- Score any track and field mark using the World Athletics Scoring Tables
- Leaderboard sorted by points to compare athletes across different event types
- Athlete profiles tracking personal records in every event
- Separate men's and women's stats pages
- User accounts with personal leaderboards and athlete rosters

## Tech Stack

- **Backend:** Python, Django 4.1
- **Database:** MySQL (JawsDB on Heroku)
- **Frontend:** HTML, CSS
- **Deployment:** Heroku

## Live Demo

[gold-medal-statistics-e113a752d5f0.herokuapp.com](https://gold-medal-statistics-e113a752d5f0.herokuapp.com)

## Local Setup

1. Clone the repository and navigate to the project root.

2. Create a virtual environment and install dependencies:
```bash
   pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:
```
   API-TOKEN=your_rapidapi_key
   API-HOST=scoring-tables-api.p.rapidapi.com
```

4. Set up a local MySQL database and update the `DATABASES` config in `settings.py` 
   with your credentials.

5. Run migrations:
```bash
   python manage.py migrate
   python manage.py migrate --database=marks
   python manage.py migrate --database=users
```

6. Start the development server:
```bash
   python manage.py runserver
```

## Running Tests
```bash
python manage.py test
```

To run a specific test:
```bash
python manage.py test marks.tests.ModelName.test_name
```

## License

MIT License — see [LICENSE](LICENSE) for details.