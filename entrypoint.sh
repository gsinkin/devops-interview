#!/bin/sh
if [ -n "$1" ]; then
  echo $1 && python $1
else
  FLASK_APP=app.py flask run -p ${PORT}
fi
