# Application name : gis_utils
This application analyses client information of audit corporation

# Function
- Authenticate using jwt
- Collect audit news from the News API
- Collect client information by scraping from the web
- Notified by e-mail after scraping is complete
- List audit News
- Show client address on map
- Analyse client employee and financial information
- Add and delete user

# System environment
## Production environment
- heroku
- dyno(ubuntu)
- postgres

## Development environment
- gitpod
- docker(debian)
- github
- sqlite3

## CI/CD
- github actions
- test module(python: unittest.testcase)

## Programming language, library, framework, tool, etc.
- Python(bautifulsoup, sqlalchemy, newsapi, googletrans, etc.)
- Django(DRF, djoser, etc.)
- Vue(Vue Router, Vuex, BootstrapVue, leaflet, vue-chartjs, VeeValidate etc.)
- jwt
- Node.js
- webpack
- Bash

## Scraping Web Site
- 上場企業データベース : https://xn--vckya7nx51ik9ay55a3l3a.com/

## Use Web API
- News API : https://newsapi.org/

## This URL
- https://gis-utils.herokuapp.com/#/
