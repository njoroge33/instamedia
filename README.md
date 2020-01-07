# Instamedia

 A clone of the website for the popular photo app Instagram .thats enable users to post images and also view others images

## As users you can :
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

### Usage example

1. signup then login.
2. Open the website and browse the images.
3. If you see an image that interests you you can click on it to view it.***


## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/njoroge33/instamedia
  ```
2. Move to the folder and install requirements
  ```bash
  cd instamedia
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE insta;
  ```
4. Migrate the database and run the application
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

## Technologies Used
- Python3.6
- Django

## License
MIT &copy;2020 [John Gichuhi](https://github.com/njoroge33/instamedia/blob/master/LICENSE)
Instamedia

