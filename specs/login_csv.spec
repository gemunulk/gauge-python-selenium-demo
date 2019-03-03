Login Specification - Data Driven via csv
=========================================
Date Created    : 9/12/2016
Version			: 1.0
Owner		    : Gemunu Priyadarshana
Description		: Data driven test using Gauge

table: resources/users.csv

* On Login Page

Registered users login to the system - csv
------------------------------------------

tags: registered-user, successful, login, data-driven

* Login as <user_name> using <password>
* User <user_name> is successfully logged in

____
These are teardown steps
* Logout from the application



