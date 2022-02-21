# Welcome to my ePortfolio

My name is Mason Voorhees, I am 22 years old and living in San Diego, CA. I have recently graduated from Southern New Hampshire University and looking to showcase my software development skills to obtain a role as a full-stack software developer.

This ePortfolio contains work from previous classes that I have improved on to showcase the skills I have obtained while studying at SNHU.

In my ePortfolio, I will go over two artifacts, one from my CS310 class, and one from my CS340 class. The artifact from my CS310 class focuses on creating objects, and the usage of different data structures. I chose this artifact for two reasons. Reason one was because I struggled with understanding how object-oriented programming worked. This made the class very hard for me. So, after taking many more computer science classes and exploring object-oriented programming in my free time, I felt more confident in my object-oriented programming skills. This motivated me to come back to this Juke-Box application so I could showcase how much I have improved over a few years. Reason two was because I did not understand why we would want to use different types of data structures. This wasn't something I struggled with in CS310 but was something I didn't understand. So, after this class ended, I explored the differences in the usage of different data structures. Understanding how I could improve the efficiency of the Juke-Box application by using other data structures such as linked-lists and arrayLists, motivated me, even more, to come back to this Juke-Box application to improve its functionality.

The reason I chose CS340 for my other artifact, was because of my lack of understanding of databases. Before taking CS340 I always thought of databases as something I would want to stay away from in my computer science career. For some reason, they always looked difficult to understand to me. After taking CS340, I liked databases. I understood how important they are when trying to store information. I created this animal shelter application in the class but never completed the application. I had a lot of missing functionality which left me feeling like I failed the class. After the class ended, I worked on a messaging application in my free time where a Mongo database was used. This allowed me to refine my skills with databases and motivated me to come back to this animal shelter application and showcase my new knowledge. Completing the enhancements outlined in this ePortfolio, verifies that I have what it takes to be a full-stack software developer.

My time at SNHU has allowed me to learn very valuable lessons. I have learned the discipline of working on assignments ahead of schedule and submitting quality work. These lessons have helped form me into who I am today. Working on a capstone assignment while in school has prepared me for the professionalism I will need to bring to my future career. The capstone and computer science program are focused on training me to perform tasks at the level a future employer would like to see along with granting me the knowledge and expertise of a full-stack software developer. Although I might have run into many struggles during my time at SNHU, I always told myself to push through it. This is no different than the mindset I will take in while working in my future career.

## Code Review

This code review will go over two artifacts I have chosen from previous courses. I will outline the flaws and enhancements that will be made to these artifacts.

Click [here](https://www.youtube.com/watch?v=Md9IJjylD60) to view the code review video.

## Artifacts (before enhancements)

### Databases
For this artifact enhancement, I will use an old assignment from CS340 using python and MongoDB which accesses information stored regarding an animal shelter. I will enhance this project by creating more refined tools to run queries on the database. Right now, this project only has predefined CRUD functionality in the python code. This means for me to CRUD anything, I need to go into my python code and change the hard-coded values. I will be creating a way for the user to choose if they want to create, read, update, or delete something and write to the database in real-time. This will make my database work with the python project in a more standalone fashion. I will also add more data that can be entered into my database. Right now, my database takes two fields, an animal species, and an animal name. I will be adding more fields such as age, gender, color, and weight. I will also refine this application to meet coding standards along beautifying the user interface.

Here are two links in order to access the files for this project:

Click [here](https://github.com/masonvoorhees/ePortfolio/blob/main/Voorhees-Mason-Jun%2021%2C%202021%20440%20AM%20(1)%20(1).ipynb) to access the first original database artifact.

Click [here](https://github.com/masonvoorhees/ePortfolio/blob/main/Voorhees-Mason-Jun%2021%2C%202021%20440%20AM%20(1).py) to access the second original database artifact.

### Software Design / Engineering 
For this artifact enhancement, I will be improving on a project I worked on in CS310 where I created an object with a playlist that had strings for each song in a playlist. I will be improving on this application by making the object I created more detailed and even implementing a link that will redirect to YouTube to play songs in each playlist. I will use coding standards to comment on what each function and line of code does for future use. When I first started programming, I never really documented what all my code did. After that, I will be showcasing my skills in creating objects. I will create new objects that will work with the playlists. I will call these albums. I will create an album that contains a list of songs by a certain artist. I will then modify the playlist object to take that new album object I created. This will mean the playlist object will no longer contain the object of a song but instead an object of an album. I never completed this project fully either so I will be completing this project to its full extent.

### Algorithms and Data Structures 
For Algorithms and data structures I will be using the same project I used in CS310. I will be improving on the overall function of the application by incorporating arrays, linked lists, and functions to better sort my data. Right now, the assignment simply prints a list of songs in the console, I will be making this application far more of a standalone experience where YouTube will launch and play the selected song. By completing these tasks, I will showcase my skills in algorithms and data structures.

Here is a link in order to access the file for this project:

Click [here](https://github.com/masonvoorhees/ePortfolio/blob/main/JukeBox_NoEnhancements.zip) to access the original Juke-Box application.

_Note: Software Design / Engineering & Algorithms and Data Structures share the same artifact._

## Artifacts (after enhancements)

### Databases

**What is the chosen artifact for this enhancement?**

The artifact I chose for this enhancement is a database application that I made in my CS 340 class. This application allows us to connect to a Mongo database where we take data from a collection and store it into a table. The user would then be able to view all data on the table and filter each column based on the values in that column. Such as if we are looking at a database of doge breeds, we could filter the dog breeds by typing “golden retriever” into the filter text box. 
	
**Why did I choose this artifact?**

I chose this artifact because databases are something that I have always struggled to understand. After taking CS 340, I was able to finally understand databases enough and had the potential to create something with my newly learned skills. Unfortunately, the class ended soon after I fully understood how a database works so I am using this artifact as an opportunity to improve on an old application and show off my skills.

**Did you meet the course objectives planned out in milestone one?**

The objectives set in milestone one have been completed. In milestone one, I outlined 3 changes to the database application  

1.	Add a username and password to the database for security.
2.	Organize and comment code for readability.
3.	Enhance the overall application to have more functionality.

For the first change in this application, I needed to add a username and password. Although I am using a local server for this application, I still wanted to keep the application secure for scalability. This means if I decide to make the application cloud-based, I will need the correct credentials to manipulate the database’s data. To implement username and password functionality to the database, I needed to add a user with read and write permissions through Mongo. The below image is how we add a user to the Mongo database:

![image](https://user-images.githubusercontent.com/62579003/154877317-055c2fb7-f569-41c5-88cb-0a647259d140.png)

For the python application, I also needed to add this username and password to the client URL field. This is a simple change:

![image](https://user-images.githubusercontent.com/62579003/154877354-717eadac-afcb-4f32-8a45-8f8fc7d9f470.png)

What this does is pass the username and password through to the Mongo server, so it knows which credentials to use.

For the second change, I went through all my code and changed everything to make the code a lot more readable:

![image](https://user-images.githubusercontent.com/62579003/154877381-d5656c8d-26de-4496-8ac9-427b2ccab86f.png)
![image](https://user-images.githubusercontent.com/62579003/154877397-d3248b2c-c628-4be2-85c5-64223cf48860.png)

My strategy for the organization and comments I wrote for this application are based on the block of code each comment is associated with. Each block of code has a summary of what is going on. This makes it easy to dial into one block of code if there is a problem that might pertain to a certain type of issue. This could be if there is an issue with the creation of a data table, we can look at the block of code related to creating a data table. Anytime time there is any type of data manipulation or customization, there is a comment to better describe that action if any future changes are necessary. This will ensure that there will be no confusion on where to add those changes.

For change three, I added a decent amount more functionality to the application.

![image](https://user-images.githubusercontent.com/62579003/154877450-2e3ced73-390e-4f59-b622-6199433b70f1.png)

Based on the image above you can see the added functionality of graphs. These graphs take many different data from the table which is then used to create the graph. These fields can easily be changed because they are just a string that is changed in the python script. 

![image](https://user-images.githubusercontent.com/62579003/154877471-59c40188-36f7-4fa3-8a8b-2093a20a268e.png)

For the histogram "shields", The min and max shield range for the x and y-axis, we are using the number of users with the same shield amount as the max and zero as the min. For the other histogram, both rank and armor columns are used to create the graph. The rank is a type string and is used as the x-axis. The max number of users with the same rank is used as the max y-axis. The column armor is used for the color of each different type of armor. For instance, if a user was a chief, but had the same armor as a commander, an extra addition to the chief bar would be added but red like shown below:

![image](https://user-images.githubusercontent.com/62579003/154877501-4eab93db-c56e-4541-8677-30d00c3e7dd2.png)

Other functionality that was added, relates to manipulation of the database collection.
A user can click on any field in the data table and then in real-time see the graphs update. This can be checked in the mongo database.

If a user clicks the “add row” button, a new row will be created where I can add new data like below:

![image](https://user-images.githubusercontent.com/62579003/154877557-22d42a24-572f-4dfd-a4be-31f69f86e6ca.png)

After filling out this blank table with valid information, the  “save to database” button, is clicked, and then the graphs update to show new relevant information regarding Will. This information is verifiable through Mongo:

![image](https://user-images.githubusercontent.com/62579003/154877577-f93790f0-ab17-476a-8583-70c7f082d19a.png)

With all these changes being successfully implemented into my third artifact, I am confident in my skills regarding databases.

**Reflect on the process of enhancing/modifying your artifact.**

When enhancing my artifact, the biggest obstacle I had to face was how this application was written on a Linux virtual machine. This meant that the whole database that I had created on that Linux virtual machine, would no longer be available to me on my windows PC. This meant that I needed to start from scratch on making the database. I went on google and found out there were tools like MongoDB Compass that allows me to fully import and create a database by uploading a text document written in the correct format (JSON). I created a text document of all data I needed for my application and was on my way to start on the enhancements. When starting the enhancements, I also had issues with packages not being downloaded, so I went online to find those packages I needed. After getting all those packages fully installed, my enhancement process started. I ran into the same obstacles as I did with the Jukebox application, my code was written messy and no comments were made. I needed to slowly work my way through each block of code and wrote comments as I went. Once I finished re-organizing all the code, working on the other two changes was a piece of cake.

Click [here](https://github.com/masonvoorhees/ePortfolio/blob/main/DataBase_Enhanced.py) to access the enhanced database artifact.

### Software Design / Engineering & Algorithms and Data Structures

**What is the chosen artifact for this enhancement?**

The artifact I chose for these two enhancements is the Jukebox application. I made this project in CS 310 which was an application where students would create a class called playlist which accessed other classes with objects called songs. These songs would be added to the student’s created playlist. Once the application was running, the user would need to type in the playlist name. When the playlist name was typed into the console, the app would print out “now playing” with the title of the song and artist.

**Why did I choose this artifact?**

I chose this artifact because this artifact has many different features that feel necessary to know as a future developer. This Jukebox application has many different data structures, so I feel it is important to understand which data structure should be used in each situation. The Jukebox application also has many different classes and objects that were used by one another and none of these classes had any documentation of what that class or object was doing. This gave me the opportunity to enhance the application so that I could improve on my coding standards along with documentation. I also noticed that this application could be improved functionality-wise. I noticed the only functionality of the application was to print out the song name and artist that was hard coded in user’s playlist. I thought it would be better for the actual song to play. This would lead me to add more functionality relating to customization for the user. So, I created a whole new class called “CreateUser” which allows the user to create a playlist of their own custom songs of any length with error checking. I also was able to enhance the song object to also take in a URL so that the user could add a link to the song that would open when the song was playing. In short, the reason why I chose this artifact is because it had many different improvements that needed to be done that would showcase my coding skills in relation to Software Design / Engineering & Algorithms and Data Structures. 

**Did you meet the course objectives planned out in milestone one?**

The objectives set in milestone one have been completed. In milestone one, I outlined 8 changes to the Jukebox application  

1.	Incorporate usage of arrays
2.	Incorporate usage of linked lists
3.	Change the structure of the playlists code
4.      Commented code written in classes and objects for greater understanding
5.	Re-organize code to better fit a standard that all classes and objects follow
6.	Condense code so all unnecessary calls and commands are deleted 
7.	Create a separate class that allows the user to create their own custom playlist with songs
8.	Surround user input with try/catch statements so there is a way to recover from invalid user entries.


For changes 1-3 look at the below image:

![image](https://user-images.githubusercontent.com/62579003/154878859-4c76925a-5dd6-4e4f-a4e6-5eea0d566403.png)

In the following code, we see an array list and a linked list. Both data structures are used for different functions. An array list is used the best when storing and accessing data. Manipulation on an array list is slow since an array list internally uses an array. If data stored in this array is removed, all the bits are shifted in memory. On the other hand, we have a linked list, a linked list is best for data manipulation. This is because a linked list uses a doubly linked list which does not require bit shifting. We choose to create an array list for each artist class because we are only storing data and then accessing that stored data. We choose to store all songs into a linked list because we are manipulating data, we have inserted into our linked list by deleting old values and looping through the new values in the linked list to play a song.
By looking at the code above, we are also able to see the structure of the code has been changed to be far more organized. Now we can look at each playlist and understand exactly what is going on in each block of code. This will allow a developer to easily look at the code and understand the functionality.

Another change I have made, is allowing the user to create a custom playlist:

![image](https://user-images.githubusercontent.com/62579003/154878923-28a83fda-fdbd-4d36-820f-7f1b93132163.png)

This function called “createAPlaylist()” is run if the user types the “create” on application startup. The command manager directs this input to the student list class:

![image](https://user-images.githubusercontent.com/62579003/154878953-af8d2889-71d4-4912-9245-d1e1d53b7d8e.png)


The student list class then verifies the input typed in and runs the create_Playlist() function. This function will loop through a process of asking the user for three strings, a title, artist, and link. Once the user gives these three strings, the function creates a song object. Then this song object is added to the array list. This loop will continue until the user types “done” which will end the loop and proceed to play the newly created playlist. An array list was used for this class since we were only adding data, no manipulation was taking place. 

**Reflect on the process of enhancing/modifying your artifact.**

When enhancing my artifact, I ran into the issue of not fully remembering how my code was functioning. This was because my code was very disorganized and none of the code was commented on. After fully going through my code, I started understanding the functionality of each class was. To remember this more clearly, I would start commenting on what each block of codes function was so I could remember what everything was doing. After doing this, I wanted to reorganize all the code to increase the readability. This would allow me to come back to the code and quickly pinpoint what needs to be changed. I then started on changes #4-6. I think my approach of reorganizing all the code before making any changes helped the enhancement process greatly. It allowed me to quickly understand where I needed to implement changes whereas before, it was hard to see where the enhancements should be.

Below is an example of how a class has been updated for better coding design notice the commenting and organization of the code to look more readable:

![image](https://user-images.githubusercontent.com/62579003/154881632-70e95ff7-8246-4bcc-86a8-2e43b097d7f5.png)

![image](https://user-images.githubusercontent.com/62579003/154881648-93181c52-9ab9-4be5-8db5-9c4e6d3e40ac.png)

For change #7, added a new class and object that allows the user to create their own playlist instead of only being able to use hardcoded playlists as shown below:

![image](https://user-images.githubusercontent.com/62579003/154881674-d1816de1-df07-4f4b-a494-548c8ee8ae96.png)

![image](https://user-images.githubusercontent.com/62579003/154881694-67851d82-6e9e-460f-b290-6ee907441ee2.png)

For the last edition of this enhancement (change #8), I added error checking so when a user enters a command that is not recognized, the application understands how to deal with this incorrect input. This was done by creating a try-catch statement that catches any IO exceptions and then tells the user that the input is not recognized and to try again. When the application is first running, we ask for the user’s input, in our code, we have an if statement at this step that will only continue if the input matches one of the commands listed. If the command is not listed, we also display that the command is not recognized and to try again as shown below.

![image](https://user-images.githubusercontent.com/62579003/154882048-cf2eea25-e9b2-4f56-be1c-4d6390a26e26.png)


![image](https://user-images.githubusercontent.com/62579003/154882030-086ff90d-7f8c-46d6-a760-179ffc44feec.png)

**Conclusion**

After finishing this enhancement, I have been able to fully showcase my coding skills relating to software design, data structures, and algorithms. My enhancement contained the creating of objects, re-organizing my code, condensing my code, error checking, implementation of arrays and linked lists, and code documentation. I have learned how important it is to keep code organized and well thought out. If others need to look at your code or if you are needing to change something in the future, having great software design skills will allow you to accurately comprehend your code. Finding time to keep code organized can also help bring bugs and security flaws to the surface. The implementation of correct data structures, algorithms, error checking, and objects all lead to a more organized application that won’t only look pretty, but will also increase the application’s efficiency. 

Click [here](https://github.com/masonvoorhees/ePortfolio/blob/main/jukebox-player(fullyEnhanced).zip) to access the enhanced Juke-Box artifact.

_To access the full github repository click [here](https://github.com/masonvoorhees/ePortfolio)._








