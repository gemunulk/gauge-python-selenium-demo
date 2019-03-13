# gauge-python-selenium-demo project [![Build Status](https://travis-ci.org/gemunulk/gauge-python-selenium-demo.svg?branch=master)](https://travis-ci.org/gemunulk/gauge-python-selenium-demo) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=gemunulk_gauge-python-selenium-demo&metric=alert_status)](https://sonarcloud.io/dashboard?id=gemunulk_gauge-python-selenium-demo)

This is an example project, illustrating how to do test automation using [Gauge](https://github.com/getgauge/gauge) test automation framework, with python support.

This project uses 

- [Gauge](http://getgauge.io/)
- [Python 3](https://docs.python.org/3/index.html)
- [Selenium](http://selenium-python.readthedocs.org/)


# Concepts covered

- Use [Webdriver](http://docs.seleniumhq.org/projects/webdriver/) as base of implementation
- Specs
- Table driven execution

# Prerequisites

- [Install Gauge](http://getgauge.io/download.html)
- [Install Python 3](https://www.python.org/downloads/)
- [Install Gauge-Python plugin](https://github.com/kashishm/gauge-python/wiki/User-Documentation) by running
  ````
  gauge install python
  ````

## System Under Test (SUT)

```
Using the "APP_ENDPOINT" /env/default/default.properties
```
* The SUT should be available at [http://newtours.demoaut.com](http://newtours.demoaut.com)

# Executing specs

### Set up
This project requires pip to install dependencies. To install dependencies run :  
````
pip3 install -r requirements.txt
````

### Propertes
On Windows: Please updated the env/default/python.properties as bellow.
````
GAUGE_PYTHON_COMMAND = python
````

### All specs
````
gauge run specs
````
This will also compile all the supporting code implementations.
