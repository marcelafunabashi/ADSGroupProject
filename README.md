# StayXchange
## 1. Project Description:
StayXchange is a platform that provides housing solutions for incoming and parting exchange students struggling with finding accommodation.
Our platform has 2 main functions:
1. It allows students to enlist their flats or rooms for subletting and set a price.
2. It allows students to search and select a space they wish to rent during their exchange semester. 
### Issue Addressed:
Incoming exchange students at IE University in Madrid often report their struggles on locating a place to stay during their short-term studies. According to initial findings, this is due to the fact that rental options are mostly offered on long-term contracts.
On the other hand, IE students going abroad find themselves unnecessarily paying for long-term contracts, at the lack of shorter options, and wasting money as they are not staying for the duration of their exchange. The supply of one group is the demand of the other.
### Technologies Used
For the development of our platform, we used Python 3.11 within PyCharm 2023.2.1 (Professional Edition). 
## 2. Installation and Set-Up:
To be able to run this program, the following are required:
### Python Programming Language
Latest version is always recommended, Python 3.11 was used for this version of the platform.
### Libraries
This program is making use of the Pillow library. 
To download the library, use the following command:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
### Supporting Image Files
For the prototype to properly run, supporting images (img1.jpg through img8.jpg) must be downloaded into the same directory as the Python file, main.py

After assuring proper setup, the file named main.py can be downloaded and run.
## 3. Use:
### Code Description
This code defines a simple GUI (Graphical User Interface) application. The application allows users to search, filter, and display information about apartments. Here's a breakdown of the functionalities within the code:
#### Apartment Data:
The code defines a list of dictionaries named apartments, where each dictionary represents an apartment with various attributes including: ID, bedrooms, bathrooms, heater availability, pets allowed, price, location, and an image path.
#### Filtering Function:
We made a function named filter_apartments that takes the dictionary of apartments and a dictionary of filters. It filters the apartments based on the specified criteria such as minimum bedrooms, minimum bathrooms, maximum price, and location. This is done in order to narrow the apartment offerings once the user has selected their requirements.
#### GUI Setup:
The main GUI is set up using Tkinter. It includes entry fields, checkboxes, buttons, and labels for filtering apartments based on criteria that was previously specified.
#### Image Loading Function:
The load_image function takes an image path, resizes the image, and converts it into a Tkinter PhotoImage object in order to be able to fit it into the GUI.
#### Sorting Algorithm:
The selection_sort_by_price function implements selection sort algorithm to sort the list of apartments based on their prices.
#### Display Function:
There is a function named display_apartments that opens a new window and displays information about apartments. It uses a canvas with a scrollbar in case there are more than one apartment.
#### Update Preview Function:
The update_preview function updates a preview section in the main window based on the selected filters. It displays the image and details of the first filtered apartment. 
#### Add Apartment Function:
The add_apartment function creates a new window to add a new apartment. It includes entry fields for bedrooms, bathrooms, heater, pets allowed, price, location, and a button to select an image. The user should use that function to enlist a new apartment, providing the required fields.
#### Main Application Loop:
The main loop (root.mainloop()) runs the Tkinter application.
## 4. Extra Information:
### Data Structures:
Dictionaries – used to keep track of apartments and filters.
### Algorithms:
Selection Sort – the selection sort algorithm was implemented to sort apartments through prices. The function takes in the apartments dictionary, and applies a for loop so all elements are iterated. A min_index variable is assigned the variable in iteration. Another for loop iterates through the remaining elements in the list and uses an if statement to test which apartment in the dictionary has a higher price. The apartment with the lower price is then ordered in variable 'apts' which, after all iterations, is returned by the function containing an ordered list of the apartments by ascending price.
## 5. Credits:
Project Creators:
* Antonio Argenta
* Cloe Chapotot
* João Paulo Prado
* Marcela Funabashi
* Moritz Goebbels
* Vittorio Fialdini

