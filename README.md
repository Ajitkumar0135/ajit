**A.	Instruction to set up and Installation the Flask Application :**

1. Install Python 3.x on your machine.
2. Install Flask using pip:
   	pip install flask
3. Install MySQL and set up a local database(ex : xampp).
4. Create a virtual environment (optional but recommended):
  	python3 -m venv venv
   	source venv/bin/activate
5. Run the Flask application:
   	flask run
The application should now be running locally on `http://localhost:5000`.

**API Endpoints(route) :** 

The following routes are available:

•	`/hello` :    Returns the string "Hello, World!".

•	`/users` :    Retrieves a list of users from the "users" table in the database and displays them as a list in an HTML table.

•	`/new_user` :   Renders an HTML page to accept input from the user and store the information in the "users" table.

•	`/user` :   Retrieves details of a specific user from the "users" table based on their ID.

**B.	Database Interaction :**

To interact with the MySQL database:

1. Create a MySQL database named "users".
3. Design a table "users" with the following columns:
   - id (int, primary key, Auto_increment)
   - name (varchar)
   - email (varchar)
   - role (varchar)
4. SQL queries to interact with the database:
    Insert sample data into the "users" table - INSERT INTO users (name, email, role) VALUES ('Ajit', 'ajajit315@gmail.com', 'software developer');

   - Retrieve all users from the "users" table.   -   SELECT * FROM users;

   - Retrieve a specific user by their ID.   -    SELECT * FROM users WHERE id = <user_id>;

**C.	Document any additional dependencies or setup requirements :**

-  Make sure to update the database configuration in the config.py file to match your MySQL database credentials and settings.
-  Make sure that the ‘id’ initialize to 1 and it’s set as AUTO_INCREMENT.

**D.	Git workflow :**

-	It describes git workflow that should be used when contributing to open source projects on GitHub. It assumes a very basic understanding of git (commits, branches, etc.) using the command line.
-	Before you make any changes, you should make a branch. Remember to never commit to master. The command git status will tell you what branch you are on. 
-	Must add $ git config --global user.name 'your name'$ and user.email 'your email'.
1.	Update master   :   Before you make any changes, first checkout master
2.	git checkout master and pull in the latest changes git pull   :   
This will make it so that your changes are against the very latest master, which will reduce the likelihood of merge conflicts due to your changes conflicting with changes made by someone else.
3.	Create a branch   :    Once you have done this, create a new branch. You should make a branch name that is short, descriptive, and unique.
To create the branch, run - git checkout -b branch-name 
4.	Make your changes and commit them   :   Once you have created your branch, make your changes and commit them. Remember to keep your commits atomic, that is, each commit should represent a single unit of change. Also, remember to write helpful commit messages, so that someone can understand what the commit does just from reading the message without having to read the diff.
this might look like - git add filename [filename ...]
			git commit
This will open an editor where you can write your commit message.
5.	Push up your changes   :    Push your changes to your fork.
6.	Make a pull request   :    If you then go to your fork on GitHub, you should see a button to create a pull request from your branch.
Once the pull request has been reviewed successfully, someone with push access to the main repository will merge it in. At this point you are done. You can checkout master and pull as described in step 1 and your changes should be there.

  **contribute** :      

Support questions :-

Please don't use the issue tracker for this. The issue tracker is a tool to address bugs and feature requests in Flask itself. Use one of the following resources for questions about using Flask or issues with your own code:
-	Ask on Stack Overflow: stackoverflow.com
-	Ask on our Discord or GitHub Discussions for long term discussion or larger questions.

Reporting issues :-

Include the following information in your post:
1.	Describe what you expected to happen.
2.	Describe what actually happened. Include the full traceback if there was an exception.
3.	List your Python and Flask versions. If possible, check if this issue is already fixed in the latest releases or the latest code in the repository.

Submitting patches :-

If there is not an open issue for what you want to submit, prefer opening one for discussion before working on a Project. You can work on any issue that doesn't have an open Project linked to it. These show up in the sidebar. No need to ask if you can work on an issue that interests you.
Include the following in your patch:
1.	Use Black to format your code. This and other tools will run automatically if you install pre-commit using the instructions below.
2.	Include tests if your patch adds or changes code. Make sure the test fails without your patch.
3.	Update any relevant docs pages and docstrings. Docs pages and docstrings should be wrapped at 72 characters.
