Prerequisites:

This application was built using Python 3.8.3 and Django 4.0.1.  I also used a few other extensions to django.
Below is a list of everything that needs to be installed:

django
django-tables2
django-filter
django-bootstrap3


Usage:

To start the server, open terminal/command prompt and set the current directory to the folder BattedBallApplication.
The server can then be started using the command 'python3 manage.py runserver'.

Next, open a browser and naviate to 'http://127.0.0.1:8000/'.  You will be greeted by the main page which
displays the data in a table and has filtering search bars on the left side of the screen.

<img width="1440" alt="Screen Shot 2022-04-20 at 9 23 45 PM" src="https://user-images.githubusercontent.com/25231780/164353054-374b8f13-4ba4-4ae6-82e3-b56bb118cbba.png">

In order to contextualize the data, we can filter what data is present in the table.  To do this, use the filter search bars
on the left side of the screen and then click the Search button to filter down the data.

<img width="1440" alt="Screen Shot 2022-04-20 at 9 23 00 PM" src="https://user-images.githubusercontent.com/25231780/164352958-35c3ccb9-0cec-40c1-818f-0f986d2909a3.png">

We can also order the data in the table by clicking on the column headers.  Click a header once to order by ascending order
and click the same header again to filter by descending order.

This filtering and sorting is done very quickly, as data is stored in a SQLite database which was created from the Excel file you
provided.

Under the column VIDEO LINK, clicking the link will bring you to a video of the at bat.  Clicking the back arrow in your browser
will return you to the application, where the filtering and ordering will be the same as when you left to watch the video.

<img width="1438" alt="Screen Shot 2022-04-20 at 9 22 08 PM" src="https://user-images.githubusercontent.com/25231780/164352870-3d2477ad-e344-4b19-a1ce-b8be68d0948b.png">

Clicking the Open button in the DataBreakdown column will open a new page where a scatter plot is displayed to visualize the data.
Exit Velocity and Launch Angle are plotted, and the data points are colored by hit outcome.  Clicking on a category in the legend
allows you to filter that data out of the plot.  Clicking again will reintroduce that data into the plot.  For example, if I wanted
to only look at the selected at bat and homeruns, I would click on Other, Singles, Doubles, and Triples to exclude them.
This visualization allows for useful analysis of the dataset and allows the user to see where the selected at bat fits into 
the dataset as a whole.

<img width="1439" alt="Screen Shot 2022-04-20 at 9 20 53 PM" src="https://user-images.githubusercontent.com/25231780/164352798-fdb33596-20c8-461b-a733-13137e66dee5.png">



