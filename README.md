# Welcome to Joke Trainer!

## Things you can do in Joke Trainer-

- Browse the built-in library of animated jokes by keyword search or category 
- Register an account
- Add jokes to your collection of favorites
- Use the Joke Trainer feature to commit your favorite jokes to memory with hints and flashcards
- Add and integrate your own jokes with the existing library


Joke Trainer ERD:
![Joke Trainer ERD](jt/static/jt/images/joke_trainer_erd.jpeg)

## To access Joke Trainer in your terminal:

SET UP A VIRTUAL ENVIRONMENT

1. Create a folder for the project named JokeTrainer (or whatever you'd like) and navigate into the folder
2. Initialize a virtual environment from within your new folder
a. virtualenv env<br />
b. source env/bin/activate<br />
c. (To end your virtual environment: deactivate)

INSTALL DJANGO

3. Within your new folder (but outside of the virtual environment folder) install Django by typing:<br />
a. pip install django

CLONE DOWN JOKE TRAINER

4. Clone down the Joke Trainer project:<br />
a. git clone https://github.com/robbyhecht/joke-trainer.git

5. There should now be a folder called joke_trainer-- navigate into this folder

MAKE A DATABASE

6. Create your database by typing-- 
python manage.py makemigrations

7. Then to activate migrations, enter-- python manage.py migrate

8. You can access the SQLite database now by opening the file inside your project called db.sqlite3 in DB Browser.

POPULATE THE DATABASE

9. You can populate the database with the existing file db.json by typing-- pyman loaddata db.json

FIND JOKE TRAINER IN YOUR BROWSER

10. Start up your local server by typing: python manage.py runserver

11. In your browser, you should now see the Joke Trainer homepage at localhost:8000

## Sections in Joke Trainer

### Navigation Bar

- Links to home page, favorites page, trainer page, registration and login/logout
- Search bar

### Home Page

- Left column contains links to descriptions of the various site functionalities
- Center column has a random "Joke of the Moment"
- Right column contains links to the various joke categories. Once you are logged in, the top category contains your personal jokes

![Joke Trainer ERD](jt/static/jt/images/joketrainer_home.jpg)

### Favorites

- Once you're logged into an account, each joke will have a blue button that lets you add the joke to your list of favorites, which appear on the favorites page

![Joke Trainer ERD](jt/static/jt/images/joketrainer_favorites.jpg)

### Trainer

- The coolest part of the site. The Trainer page is where you can use Joke Trainer to help yourself memorize your favorite jokes. You'll find only a hint on the front of the card, with the entire joke on the back. Use these flashcards to build your repertoire as a master joke teller.

![Joke Trainer ERD](jt/static/jt/images/joketrainer_trainer.jpg)

### Add Your Own Jokes

- Once you're logged into an account, you can add as many jokes as you want to the database. Your jokes will integrate into the existing library, but will only be visible to you when you're logged in.