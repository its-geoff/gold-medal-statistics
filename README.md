# Gold Medal Statistics

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<div align="center">
  <a href="https://github.com/its-geoff/gold-medal-statistics">
    <img src="assets/gms_white.png" alt="Gold Medal Statistics Logo" width="150">
  </a>

  <h3 align="center">Gold Medal Statistics</h3>

  <p align="center">
    A standardized scoring platform for track & field coaches to measure and compare athlete performance.
    <br />
    <a href="https://gold-medal-statistics-e113a752d5f0.herokuapp.com"><strong>View Live Demo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/its-geoff/gold-medal-statistics/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/its-geoff/gold-medal-statistics/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#supported-events">Supported Events</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#release-schedule">Release Schedule</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

[![Product Screenshot][product-screenshot]](https://gold-medal-statistics-e113a752d5f0.herokuapp.com)

**Gold Medal Statistics** is an innovative web application for track & field coaches and athletes. Using data from the **World Athletics Scoring Tables**, it converts raw event marks into a standardized point score — allowing you to compare performance across completely different events on a level playing field.

Whether your sprinter runs a 11.5 in the 100m or your distance runner clocks a 4:30 mile, Gold Medal Statistics gives you a single number to evaluate, rank, and track them side by side.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Features

- **Standardized scoring** — Converts marks from any event into World Athletics points
- **Leaderboard** — Ranks all athletes' entries by points in a single view
- **Athlete profiles** — Tracks personal records (PRs) across all events for each athlete
- **Men's & Women's stats** — Separate roster pages with individual athlete profiles
- **User accounts** — Each coach has a private account with their own athletes and leaderboard
- **Mark management** — Add, view, and delete leaderboard entries
- **Flexible input** — Accepts time in `MM:SS.ms` format and distance in meters; handles many event abbreviations

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Built With

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]
* [![MySQL][MySQL-badge]][MySQL-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Heroku][Heroku-badge]][Heroku-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

Follow these steps to run Gold Medal Statistics locally.

### Prerequisites

- Python 3.9+
- MySQL 8.0+
- A [RapidAPI](https://rapidapi.com) key for the [Scoring Tables API](https://rapidapi.com/search/scoring-tables)

Install Python dependencies:

```sh
pip install -r requirements.txt
```

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/its-geoff/gold-medal-statistics.git
   cd gold-medal-statistics
   ```

2. **Set up your MySQL databases**

   Create two databases in MySQL:
   ```sql
   CREATE DATABASE marks;
   CREATE DATABASE users;
   ```

   Import the provided schema dumps:
   ```sh
   mysql -u root -p marks < marks.sql
   mysql -u root -p users < users.sql
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   API-TOKEN=your_rapidapi_key_here
   API-HOST=scoring-tables-api.p.rapidapi.com
   SECRET_KEY=your_django_secret_key_here
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   python manage.py migrate --database=marks
   python manage.py migrate --database=users
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/home/` in your browser.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

1. **Create an account** at `/signup/` or log in at `/login/`
2. **Add entries** via the form at the top of the Scores page — enter athlete name, gender, grade, team, event, and mark
3. **View the leaderboard** — all entries are ranked by points, highest first
4. **Browse athlete profiles** on the Stats page — view each athlete's PRs across all events
5. **Manage entries** — delete any entry directly from the leaderboard

### Accepted Mark Formats

| Event Type | Format | Example |
|---|---|---|
| Sprints / Short hurdles | Seconds (decimal) | `11.54` |
| Middle / Long distance | `MM:SS.ms` | `4:32.10` |
| Field events (jumps/throws) | Meters (decimal) | `6.75` |

### Accepted Event Abbreviations

Events can be entered in a variety of shorthand formats, for example:

- `100`, `100m` → 100m
- `1600`, `1600m` → 1600m
- `hj`, `high`, `high jump` → High Jump
- `sp`, `shot`, `shot put` → Shot Put

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Supported Events

| Sprints & Hurdles | Distance | Relays | Field |
|---|---|---|---|
| 100m | 800m | 4x100m | High Jump |
| 200m | 1600m | 4x400m | Pole Vault |
| 400m | 3200m | | Long Jump |
| 100mH / 110mH | | | Triple Jump |
| 400mH | | | Shot Put |
| | | | Discus Throw |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [ ] Edit existing leaderboard entries in-place
- [ ] Grade-level filtering on the leaderboard
- [ ] Team comparison view across multiple users
- [ ] Export leaderboard to CSV
- [ ] Password reset via email
- [ ] Athlete photo uploads

See the [open issues](https://github.com/its-geoff/gold-medal-statistics/issues) for the full list of proposed features and known bugs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Release Schedule

| Version | Cadence | Description |
|---|---|---|
| `x.0.0` Major | As needed | New major features |
| `0.x.0` Minor | Monthly | New minor features |
| `0.0.x` Patch | Every 2 weeks | Bug fixes |

All major changes are documented in [Releases](https://github.com/its-geoff/gold-medal-statistics/releases). For granular history, see the Issues and Projects tabs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Geoffrey Agustin, geoffrey.agustin04@gmail.com

Project Link: [https://github.com/its-geoff/gold-medal-statistics](https://github.com/its-geoff/gold-medal-statistics)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/its-geoff/gold-medal-statistics.svg?style=for-the-badge
[contributors-url]: https://github.com/its-geoff/gold-medal-statistics/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/its-geoff/gold-medal-statistics.svg?style=for-the-badge
[forks-url]: https://github.com/its-geoff/gold-medal-statistics/network/members
[stars-shield]: https://img.shields.io/github/stars/its-geoff/gold-medal-statistics.svg?style=for-the-badge
[stars-url]: https://github.com/its-geoff/gold-medal-statistics/stargazers
[issues-shield]: https://img.shields.io/github/issues/its-geoff/gold-medal-statistics.svg?style=for-the-badge
[issues-url]: https://github.com/its-geoff/gold-medal-statistics/issues
[license-shield]: https://img.shields.io/github/license/its-geoff/gold-medal-statistics.svg?style=for-the-badge
[license-url]: https://github.com/its-geoff/gold-medal-statistics/blob/master/LICENSE
[product-screenshot]: assets/home.png

[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[MySQL-badge]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://mysql.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Heroku-badge]: https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white
[Heroku-url]: https://heroku.com
