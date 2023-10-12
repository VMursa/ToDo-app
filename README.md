
# ToDo Application
The following description provides a guide through the to-do application created in Django for Frameworks classes as the first individual work.
I've designed a data model that represents the relationships between to-do tasks and categories. I used Django’s built-in object-relational mapping tool to automatically generate the database and tables that’ll support this model.

# Requirements
We had to create a TODO app which will consist of **Categories** and **Tasks**

### Rutare și controlori

1. Creați o clasă controlor cu metode pentru gestionarea următoarelor cereri:
    1. `list`: pentru afișarea listei de sarcini
    2. `view`: vizualizarea unei singure sarcini
    3. `create`: crearea unei sarcini
    4. `update`: actualizarea unei sarcini
    5. `delete`: ștergerea unei sarcini

### Crearea entităților

1. Creați entitățile **"Task"** și **"Category"**
    1. Creați entitatea **Category**, care reprezintă o categorie de sarcini.
    2. Adăugați următoarele proprietăți (câmpuri) la entitatea **Category**:
        1. `id`: identificator unic al categoriei
        2. `name`: numele categoriei
    3. Creați entitatea **Task**, care reprezintă o sarcină.
    4. Adăugați următoarele proprietăți (câmpuri) la entitatea **Task**:
        1. `id`: identificator unic al sarcinii
        2. `title`: titlul sarcinii
        3. `description`: descrierea sarcinii
        4. `dueDate`: data limită pentru executarea sarcinii
        5. `createdAt`: data și ora creării sarcinii (completată automat)
    5. Definiți relația între entitățile `Task` și `Category`. O sarcină poate fi asociată cu o singură categorie, iar o categorie poate avea mai multe sarcini.
  


# Get started with Django and run the project
### Setup process
To build this app, you’ll start by creating a virtual environment and setting up a Django project. To create a venv, run the following commands in the terminal:
> $ python -m venv venv 
$ source venv/bin/activate

Your next step is to install the Django library and its dependencies. I created a `requirements.txt` doc for the simplicity. Make sure you are in the right folder. 
`pip install -r requirements.txt`

### Start the server
 Starting the Django development server can be done by running the command: ` python manage.py runserver`


# Code workaround
## Data Models
In `todo_list/todo_app/models.py` define two classes that extend Django’s django.db.models.Model superclass. The Model superclass also defines an id field, which is automatically unique for each object and serves as its identifier. Here I defined two models **Category** and **Task**. To link tasks and categories, i used a foreign key: `todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)`. Adter making migrations and adding some sample data from the admin panel, the first part of dev in done. 

## Create the Views
I created the public interface for your app. In Django, this involves using views and templates. A view is the code that orchestrates web pages, the presentation logic of your web app. The template is the component that more closely resembles an HTML page, as you’ll see. I used CRUD ( create, read, update, delete) as a standard for my app. Templates are equal to Twigs in Symphony. 

## The demo of the application can be seen in the root dir. 


# Questions
1. Care sunt avantajele utilizării framework-ului Django?
   -> Django's built-in features and conventions enable quick and efficient development. Also, it provides robust security features, protecting against common web vulnerabilities.
2. Care sunt metodele de definire a rutelor în Django?
   -> În Django, rutele (URL patterns) pot fi definite folosind mai multe metode, dar cea mai comună abordare este prin intermediul modulului urls.py.
3. Ce relație între tabelele bazei de date ați folosit și cum ați implementat-o?
   -> Entitatile Category și Task definesc două tabele diferite în baza de date. Aceste modele au o relație de tipul "Many-to-One" (sau "One-to-Many"), ceea ce înseamnă că o categorie poate avea mai multe sarcini, dar o sarcină este asociată cu o singură categorie. Această relație este implementată folosind cheia străină în modelul Task pentru a face referire la modelul Category.
4. Ce sunt migrațiile bazei de date și cum sunt folosite în Django?
   -> În Django, migrațiile bazei de date sunt o caracteristică esențială care permite gestionarea modificărilor structurale ale bazei de date în mod eficient și consistent. Migrațiile sunt utilizate pentru a crea, modifica și ține evidența schimbărilor în schema bazei de date într-un mod controlat și reversibil. Acestea asigură că structura bazei de date corespunde cu structura definită în modelele Django.




