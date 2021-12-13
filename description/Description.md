## Tutorial to run the project.

### To use as a Flask app :

* Clone the project  

* Inside the src/app.py source code, change the model and vectorizer path (indicated), adapted for Flask, and save.  

* Open the cmd/bash  

* In the cmd, go to the src directory and type :
```
your_Path\dataengineering2_project\src>python app.py
```
* Open localhost (port 5000) in your favorite browser
<br>
<br>



### To use in Docker:

* Clone the project  

* Inside the src/app.py source code, change the model and vectorizer path (indicated), adapted for Docker, add host="0.0.0.0" in the end (indicated) and save.  

* Open the cmd/bash  

* In the cmd, go to the dataengineering2_project directory and type :
```
your_Path\dataengineering2_project>docker-compose up
```
* Open localhost (port 5000) in your favorite browser
