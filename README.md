
# imap
A Python GUI app that lets you geocode images and export their information to a CSV.

## How to Install and Run
>Note: You must have Python 3 installed on your computer. If you have not done so already
>please go to https://www.python.org/downloads/ and download the latest version of Python.
1. Download this project (clone or zip)
2. Open terminal and cd into the project folder
3. Create a virtual environment to hold the libraries that the project relies on
    * Type `virtualenv venv`
    * Type `source venv/bin/activate` -- this will activate the virtual environment
    * Type `pip install exifread`
4. Go to https://developers.google.com/maps/documentation/geocoding/get-api-key and follow
the instructions in order to setup your own API key
5. Once you have your API key, go to the `meta.py` file and replace 'your-api-key' under the
'reverse_geocode' function with the one you just set up on Google
6. Go back to the terminal and type `python run.py`. The application should start running
