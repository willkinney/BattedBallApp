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

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/25231780/164352060-4af0392b-c675-497f-853d-9a86e9cc6c92.png">

In order to contextualize the data, we can filter what data is present in the table.  To do this, use the filter search bars
on the left side of the screen and then click the Search button to filter down the data.

<img width="1440" alt="image1" src="https://user-images.githubusercontent.com/25231780/164352161-5ab6cee5-8bbe-4347-9615-e2916c9731c3.png">

We can also order the data in the table by clicking on the column headers.  Click a header once to order by ascending order
and click the same header again to filter by descending order.

This filtering and sorting is done very quickly, as data is stored in a SQLite database which was created from the Excel file you
provided.

Under the column VIDEO LINK, clicking the link will bring you to a video of the at bat.  Clicking the back arrow in your browser
will return you to the application, where the filtering and ordering will be the same as when you left to watch the video.

<img width="1440" alt="image2" src="https://user-images.githubusercontent.com/25231780/164352273-6094b96c-b4de-4cb3-9b9c-48a894d030ef.png">

Clicking the Open button in the DataBreakdown column will open a new page where a scatter plot is displayed to visualize the data.
Exit Velocity and Launch Angle are plotted, and the data points are colored by hit outcome.  Clicking on a category in the legend
allows you to filter that data out of the plot.  Clicking again will reintroduce that data into the plot.  For example, if I wanted
to only look at the selected at bat and homeruns, I would click on Other, Singles, Doubles, and Triples to exclude them.
This visualization allows for useful analysis of the dataset and allows the user to see where the selected at bat fits into 
the dataset as a whole.

<img width="1440" alt="image3" src="https://user-images.githubusercontent.com/25231780/164352377-363beb6c-7972-4c4a-80f6-2a5b64017d29.png">



