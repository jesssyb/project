# Grocery App
#### Video Demo:  <URL HERE>
#### Description:

I made this app as a concept of something I would find useful in my own life as an app I would develop for my own personal use - despite there being plenty of grocery app out there, I have always thought of this as a fun side project I could do someday and used this final project as an 
opportunity to mock up a concept of a personal iOS app I would make myself. However for the sake of time - I just used Python to mock this up rather than Swift.

Since I created this app in Python rather than Swift, I used Beeware. Beeware is a Python library that allows for cross platform (Andriod, iOS, etc) deployment of apps so there is no need to write the same app in different languages. With command line prompts, it is super simple to create a project that contains a Python file for you to write your code. Beeware also comes with the Toga library for a GUI. However, the Toga libary isn't very robust which limits the interface capabilies an app can have when built with Beeware. Luckily since my app is so simple, this wasn't much of an issue for me.

Upon execution of the app, a user will see an input for a grocery item and an input for the quantity of the item, along with a table of any exisitng items in the grocery list. The user will be propmted to add any items they want to the grocery list. Upon submition of items to the list, the table will be updated with the item and respective quantity. To delete an item from the table once a user theorectially "obtains" that item, the user will have to double click the table row that contains that item. The table of items uses a local sqlite3 database. The database is updated upon addition/deletion of items to accurately reflect the contents of the grocery list.

