## 1/25/2023

### completed

-  formatted parameters as html table
-  created tests for marks model and scores view

### to-do next

-  brainstorm and create more tests
   -  think of tests for new_entry view specifically
-  start css using django tutorial

## 1/26/2023

### completed

-  started css for website
-  created navbar
-  created templates for each webpage
-  started navbar css

### to-do next

-  finish navbar
-  make logo responsive and auto center navbar text
-  figure out how to make indicator bars

## 1/27/2023

### completed

-  added leaderboard css
-  started button css

### to-do next

-  finish button css and start new entry css
-  make logo responsive and auto center navbar text
-  figure out how to make indicator bars

## 1/28/2023

### completed

-  added indicator bar css
-  added new entry css
-  started making website responsive (viewport height/width)

### to-do next

-  fix missing value error message
-  animate new entry so that it only shows up when prompted
-  processing entry overlay
-  finish making website responsive

## 2/2/2023

### completed

-  added favicon
-  clicking logo now leads to homepage
-  added team field to marks and athletes

### to-do next

-  look into font sizing on larger screens
-  fix test_multiple_marks
-  only have marks of a certain team show up on the leaderboard

## 2/3/2023

### completed

-  edited athlete model
-  created athlete validation function

### to-do next

-  connect marks and athlete models
-  look into font sizing on larger screens
-  fix test_multiple_marks
-  only have marks of a certain team show up on the leaderboard

## 2/13/2023

### completed

-  changed athlete model to separate marks and points
-  edited admin dashboard so user could change marks manually

### to-do next

-  conceptualize and implement athlete to mark integration

## 2/19/2023

### completed

-  conceptualized athlete to mark integration
-  started creation of model integration function

### to-do next

-  finish model integration
-  finish athlete validation test
-  fix other tests

## 2/24/2023

### completed

-  working on athlete validation test

### to-do next

-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/13/2023

### completed

-  started Figma layout recreation
   -  finished nav bar and home screen

### to-do next

-  finish recreating XD layout in Figma
-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/15/2023

### completed

-  worked on recreating XD layout in Figma
   -  finished about and scores screens

### to-do next

-  finish recreating XD layout in Figma
   -  figure out how to add hover functionality
   -  figure out component states
-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/17/2023

### completed

-  worked on recreating XD layout in Figma
   -  finished buttons, hover animations, and stats list page

### to-do next

-  finish recreating XD layout in Figma
   -  create stats opened athlete page
-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/18/2023

### completed

-  finished recreating XD layout in Figma

### to-do next

-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/19/2023

### completed

-  fixed test_multiple_marks

### to-do next

-  fix test_full_mark_output
-  fix bug in validation function: empty Athlete queryset
-  finish model integration
-  fix other broken tests

## 6/21/2023

### completed

-  fixed test_full_mark_output
-  finished test_gender_validation
-  created and finished test_athlete_check
-  created and finished test_pr_update
-  fixed test_athlete validation
-  all tests pass (9 total)
-  fixed font: use SemiBold instead of Bold for headers
-  finished implementing new entry feature in web app
-  automatically creates athlete profile when their first mark is input
-  started customizing stats page in web app
   -  created basic layout

### to-do next

-  finish customizing stats page in web app
   -  fine tune layout and complete html and css
-  fix men/women page not working
   -  works as /#men/ instead of /men/

## 6/22/2023

### completed

-  fixed men/women page not working
   -  deleted cache to see changes
-  fixed navbar on men/women page
   -  updated navbar.html to include men and women page
-  added profile page route and basic view

### to-do next

-  finish view for men_profile and women_profile
-  create athlete profile on right
-  finish customizing stats page in web app
   -  fine tune layout and complete html and css

## 6/23/2023

### completed

-  pushed files to GitHub and added issues
-  learned how to fix issues and execute pull request
-  created athlete profile frame
-  finished dynamic layout

### to-do next

-  finish creating issues for v1 on GitHub
-  finish athlete list and scrolling feature
-  full athlete profiles and stats
-  finish customizing stats page in web app
   -  fine tune layout and complete html and css

## 6/24/2023

### completed

-  fixed profile frame formatting
-  added event input validation
-  fixed list spacing for multiple athletes
-  finished athlete list layout
-  fixed duplicate athlete entries bug
   -  edited new_entry function to check for athlete existence in QuerySet
-  minor change to check_for_athlete function to reduce loop iterations
-  changed marks to show two decimal places, even if it ends in 0
-  made leaderboard scrolling

### to-do next

-  full athlete profiles and stats
-  finish customizing stats page for web

## 6/25/2023

### completed

-  created new HTML pages for profiles
-  made stats display and only included marks with points greater than 0
-  added and formatted placeholder image
-  edited profile page to include team
-  finished animating athlete list
-  made page margins uniform

### to-do next

-  make profile and models code more efficient (where events are manually listed)
-  ability to upload images for athletes
-  fix margin-top error on new_entry; not responsive - button gets disconnected
   as height shrinks

## 6/26/2023

### completed

-  finished home page based on layout
-  finished about page based on layout

### to-do next

-  make images responsive through entire site

## 6/27/2023

### completed

-  added functionality for jumps and throwing events

### to-do next

-  add login page

## 6/28/2023

### completed

-  edited code to prep for second database creation
-  created model for 'users' database
-  added 'users' database to admin and fixed migrations
-  created url paths and templates for new pages

### to-do next

-  fix bug: template does not exist at login

## 6/29/2023

### completed

-  ensured all templates worked
-  added email address to users model
-  finished login page html and css
-  edited marks/views to be more efficient
   -  removed template variable and used context variable

### to-do

-  customize leaderboard by team
-  sign up/login validation
-  email verification
-  logged out vs. logged in on site
-  hash passwords
-  fix django authentication not working

## 6/30/2023

### completed

-  fixed login bugs
-  converted to custom user class
-  working on custom backend

### to-do

-  fix no such table "users_user" error

## 7/1/2023

### completed

-  fixed admin login system
-  switched from sqlite to mysql
-  fixed bug where leaderboard wouldn't appear
-  fixed problem with router

### to-do

-  fix sign-up and login views

## 7/2/2023

### completed

-  fixed sign-up and login views
-  created logout page and basic profile
-  changed color of username and animation
-  edited logged out vs. logged in site
-  leaderboard and athlete separation by user
-  simple profile block instead of "login"
-  require all fields
-  error message for incorrect username/password combo
-  unique username validation
-  basic password change page

### to-do

-  logged in vs. logged out site
   -  "you must be logged in" error
-  make password reset and password change pages
-  make profile page

## 7/5/2023

### completed

-  worked on profile page

### to-do

-  finalize profile page and make it dynamic

<!-- keep on bottom -->

### to-do later (minor changes)

-  add grade field
-  animate new entry so that it only shows up when prompted
-  processing entry overlay
-  finish making website responsive
-  add loading bar
-  make searches more efficient
-  redirect logged-in page to profile (not home)
-  validate email + username
-  complete reset password options
-  require old password validation to change password
-  create users tests? (optional)
