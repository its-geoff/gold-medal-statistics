# Gold Medal Scoring

This app allows the user to input track marks and compare athletes on their team
across different event types.

# Start-Up Instructions

-  Open a new terminal and use "cd django" to change the current directory.
-  Use "python manage.py runserver" to start the server.
   -  Use "Ctrl + C" to close the server.

# Testing Instructions

-  Ensure the terminal is in the correct directory ("GMS/website (django)/django").
   -  If not, use "cd django" to switch the directory.
-  Use "python manage.py test" to run all tests.
   -  Use "python manage.py test marks.tests.model_name.test_name" to run only the "test_name" test.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog] (https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning] (https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 01/12/2023

### Added

-  App logic that uses a binary search to return the number of points for a given mark.
-  Full functionality that requires a user to input the specified gender, event, and target time.
