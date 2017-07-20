[![Build Status](https://travis-ci.org/justmesam/Bucketlist_app.svg?branch=flask-develop)](https://travis-ci.org/justmesam/Bucketlist_app)


# Bucketlist_app
## Introduction
An application to record and edit bucketlists...   
It is a fun thing to keep record of bucketlist to keep count on those to strike out.

#### Getting Started
What the bucketlist app let you do;
>  * create an account
>  * login to your account
>  * create a bucketlist plus add its items
>  * view your bucketlists and its items
>  * edit your bucketlists and/or its items
>  * delete your bucketlists and/or its items
>  * view others public bucketlists(feature in progress)

#### Installation and Set Up

Open up your terminal and lets get started;

Clone this repository with  `https://github.com/justmesam/Bucketlist_app.git`  
Change your directory to the directory  `cd Bucketlist_app`

1. ### Setting Up
Let's start with creating a virtual environment;   
First install virtual environment globally; `pip install virtualenv`  
Lets create our virtual environment now, just simply do; `virtualenv venv` done!   
Lets install all the packages we need, its quite easy; `pip install -r requirements.txt`  

2. ### Testing   
We will test with nose and coverage `nosetests -v --with-coverage`  
How they work;   
 + `-v` runs the test in verbose   
 + `--with-coverage` shows the test coverage

3. ###  Running the app   
On your terminal you have to change the permission of the run file :
`chmod a+x run.py`  
Now simply run: `./run.py`   
When the server starts it will be running on `http://127.0.0.1:5000/`   

Launch your favourite browser paste the url link the program is running on, most likely
`http://127.0.0.1:5000/` and let then fun start.

#### Credits
* [Samuel Thiong'o][1]
* [Andela community][2]


[1]: https://github.com/justmesam
[2]: https://andela.com/
