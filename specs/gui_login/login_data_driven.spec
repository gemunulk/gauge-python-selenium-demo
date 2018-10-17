Login Specification - Data Driven
==================================
Date Created    : 9/12/2016
Version			: 1.0
Owner		    : Gemunu Priyadarshana
Description		: Data driven test using Gauge

     |user_name|password|
     |---------|--------|
     |gem      |gem     |
     |gemunu   |gemunu  |

* On Login Page

Registered users login to the system
------------------------------------

tags: registered-user, successful, login, data-driven

* Login as <user_name> using <password>
* User <user_name> is successfully logged in

____
These are teardown steps
* Logout from the application

