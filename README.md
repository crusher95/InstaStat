# InstaStat
Statistics of Instagram accounts, Know you unfollowers and Fans

#Live Demo at :
http://apps.securitylabs.in/

# Description :

- Completely written in Flask micro framework
- RESTful API to get listof followers, unfollowers and user details
- Angular JS web interface to consume this rest api
- Option to whitelist particular user lists from displaying in unfolloers
- Own JSON data storage system for keeping track of users
- **CODE originally STORES the access tokens of users locally on json file.**
- For session maintaining purpose code stores access tokens against a random uuid4 value
- This uuid4 value is stored in users cookies, which are checked on every requets.
- Login Page Dynamically fetechs the link for Login via Instagram
- Dashboard design is in static/main.html which consumes the rest api of this app using Angular JS
- AJAX is used for following and unfollowing on click.
- Beautiful spinner is used to show while data loading is pending from http://tobiasahlin.com/spinkit/



Edit Following files for configuring it in your system
-----
    static/js/fetch.js 
    static/js/directive.js

Edit conf.json to add your Instagram APP client ID, Client Secret and Redirect URL


Requirements :
instagram
flask
uuid

How to install requirements :
-----
    pip install python-instagram
    pip install flask
    pip install uuid

All set then :D

Steps for Setting it up and Running :
-----
    1. clone repository in desired folder
    2. install requirements
    3. python main.py
