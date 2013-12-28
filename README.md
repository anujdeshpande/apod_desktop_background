Change your Mac OS X Desktop background to NASA's pic of the day.
(Tested on Mavericks)
NASA Astronomy Picture of the Day 
http://apod.nasa.gov/apod/ can be found out here.  

Pre Requisites :
    
	sudo pip install beautifulsoup4

#### To use 
Change the directory path on line 17

       python get_nasa_apod.py

#### How it works :

We use sqlite3 to update the database file (.db extension) which points towards the image to be used for the desktop background.  
It will then restart the Dock using 'killall Dock' so that the changes take place.  

NOTE FOR LINUX USERS:
     The only difference between Mac OS X and a Linux box will be the config file where we actually change the desktop background. Downloading the file and the cron job script should work fine for you (haven't tested it (yet) though) 