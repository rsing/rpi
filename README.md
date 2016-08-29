# STACK

### SETUP

0. Anaconda
1. Python & packages
2. Flask
3. Mongo DB
4. Elasticsearch
5. Postgres
6. Node.js
7. Angular JS
8. Chart.js
9. Raspberry Pi 3 Model B & sensors
10. Apache Spark

### INSTALLATION

0. Anaconda
----------

$ conda info --envs  # Get environments
$ source activate myenv # To activate an environment

But before we activate, let's create two environments called rpi2 (python 2) and rpi3 (python 3).
$ sudo conda create -n rpi2 python
$ sudo conda create -n rpi3 python=3

Now activate an envt:
$ source activate rpi2

Check list of installed packages and their versions on Conda:
$ conda list
$ conda list | grep flask  # To find if a specific package is installed

1. Python
---------
Python already set up through Step 0
Common base packages we will need: numpy, scipy, pandas, scikit-learn, jupyter, bokeh, flask, mongodb
$ sudo conda install --name rpi2 numpy
$ sudo conda install --name rpi3 numpy
(Do the same with other packages)
python> import numpy
etc.

2. Flask
---------
Just use conda to install it, or the 'traditional' way of downloading from
flask from http://flask.pocoo.org, and using pip:

$ sudo conda install --name rpi2 flask
$ sudo pip install (once you have downloaded the latest release to the local directory)
python> import flask

3. Mongo DB
-----------
Install using Homebrew:

To install Homebrew (do *not* run this as 'sudo'):
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
To install MongoDB (do *not* run this as 'sudo'):
$ brew install mongodb

Install using Conda:
$ sudo conda install --name rpi2 mongodb


4. Elasticsearch
----------------
Install is as simple as downloading the tar file, and unzipping it in some location ("path_to_es"). Then you just call the binary to start the server:

$ path_to_es/bin/elasticsearch

Python connector can be downloaded through pip:

$ sudo pip install elasticsearch
python> import elasticsearch

5. Postgresql
-------------

Install using conda:
$ sudo conda install postgresql

Create a database cluster (we're doing it inside a new directory "data/pgdb")
$ initdb -D data/pgdb

Start the database server
$ pg_ctl -D data/pgdb -l logfile start

Stop the database server
$ pg_ctl stop -D data/pgdb

https://www.postgresql.org/docs/9.0/static/app-postgres.html

6. Node.js

Download the OSX installer from website. Run the installer.
Node is installed at 
   /usr/local/bin/node
npm is installed at
   /usr/local/bin/npm
Make sure that /usr/local/bin is in your $PATH.

7. Angular JS


### LICENSES

* Anaconda
Three clause BSD License:
Copyright 2016, Continuum Analytics, Inc.

* Python
"Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006 Python Software Foundation; All Rights Reserved"

* Flask
Flask is licensed under a three clause BSD License.
Copyright (c) 2015 by Armin Ronacher and contributors.

* Mongo DB
Free Software Foundation's GNU AGPL v3.0. (Commercial licenses are also available from MongoDB, Inc.).
Basically: If you modify the Mongo DB source code, it needs to be shared with the community.
But software that uses Mongo DB is not covered under this.
Read: http://blog.mongodb.org/post/103832439/the-agpl

* Elasticsearch
Apache 2 Open Source License
Elasticsearch can be downloaded, used, and modified free of charge. It is available under the Apache 2 license, one of the most flexible open source licenses available.

