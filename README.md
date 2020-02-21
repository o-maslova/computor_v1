# computor_v1
The purpose of this project is to make a program that solves simple equations.
The program takes a polynomial equation. That is to say, involving only powers, no complicated functions.
The program display its solution(s).
The program could be running in console as well as in browser.

### Run the program in console
To run the program in console you should clone this git repository in some directory,
go to this directory and then type:
```bash
python3 main.py "your_equation"
```
#### Flags
You can also use next flags:
* **--test** - will run the program with test
* **-d** - will show you the detailed output

### Examples of work in console
![alt-text](/images/image_3.png "Console output")

### Run the program in browser
To run the program in browser you should clone this git repository in some directory,
go to this directory and then type:
```bash
source script.sh
```
It will create a virtual enviroment, install requirements in there and activate this enviroment.
When instalation is over, run the server:
```bash
python manage.py runserver
```
And go to the address 127.0.0.1:8000.

### Examples of work in browser

#### View without solving details
![alt-text](/images/image_1.png "View without details")
#### View with solving details
![alt-text](/images/image_2.png "View with details")
