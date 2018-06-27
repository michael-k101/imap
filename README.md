
# iMap
A Python GUI app that lets you geocode images and export their information to a CSV file.

## How to Install and Run
>Note: You must have Python 3 installed on your computer. If you have not done so already,
>please go to https://www.python.org/downloads/ and download the latest version of Python.
1. Download this project (clone or zip)
2. Open terminal and cd into the project folder
> Before you continue, make sure you have the 'virtualenv' package installed. 
> This can be done by typing `pip3 install virtualenv` in a terminal window.
3. Create a virtual environment to hold the packages that the project uses
    * Type `virtualenv venv` -- this will create the virtual environment
    * Type `source venv/bin/activate` -- this will activate the virtual environment
    * Install the necessary packages
        * Type `pip3 install exifread`
        * Type `pip3 install requests`
4. Go to https://developers.google.com/maps/documentation/geocoding/get-api-key and follow
the instructions in order to setup your own API key
5. Once you have your API key, go to the `meta.py` file inside of the 'app' folder and replace 'your-api-key' under the
'reverse_geocode' function with the one you just set up on Google
6. Go back to the terminal, cd into the 'app' directory, and type `python3 run.py`. The application should appear on your screen. Happy geocoding!
