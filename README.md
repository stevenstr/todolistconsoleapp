# To Do list on json-server.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


**To Do list** is a simple application for creating tasks and putting them into a to-do list using json-server. 


## Installation

Cloning, installing, and running Hyde is as simple as executing the following commands:

##### Step 1: clone the repo
```
git clone git@github.com:myusername/todolistconsole.git
```

##### Step 2: setup node.js
 - https://nodejs.org/en/download

##### Step 3: Install JSON Server
```
npm install -g json-server
```


## Documentation

```
cd TODOLISTCONSOLE
python -m pydoc .\main.py
```


## Supported Features
- Create task
- Read task/-s
- Update task
- Delete task

## Rountes

 | HTTP method | URL                                     |
 | ----------- | --------------------------------------- |
 | GET         | http://localhost:3000/tasks/{get_id}    |
 | GET         | http://localhost:3000/tasks/            |
 | POST        | http://localhost:3000/tasks/            |
 | PUT         | http://localhost:3000/tasks/{what_updt} |
 | DELETE      | http://localhost:3000/tasks/{id_delet}  |


## Running the app

Cloning, installing, and running Hyde is as simple as executing the following commands:

##### Step 1: Start JSON Server
```
cd TODOLISTCONSOLE
json-server --watch todo.json
```
##### Step 2: Run the main app
```
py main.py
```

## Contributing

If you're looking for an easy way to contribute to this project but aren't sure where to start, I've created a list of minor bugs and/or issues to be fixed before the projects initial release, which you can find here or you can just try out the app and provide some feedback. Additionally, if you'd like to submit a pull-request, I would ask that you first take a look at the projects contributing guidelines.
example@gmail.com
