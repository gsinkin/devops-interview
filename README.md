# devops-interview
 A webserver and background processor for the DevOps interview

# Getting started
1. `python3 -m venv venv-devops-interview`
1. `source venv-devops-interview/bin/activate`
1. `pip install -r requirements.txt -r test_requirements.txt`

# Run server
1. `FLASK_APP=app.py flask run`

# Examples
```
curl http://localhost:5000/key/1234

{"1234":null}

curl -X POST http://localhost:5000/key/1234 --header "Content-type: application/json" --data '{"test": true}'

curl http://localhost:5000/key/1234

{"1234":{"test":true}}
```
