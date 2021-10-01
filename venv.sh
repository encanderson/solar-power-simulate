#!/bin/bash

activate(){
    . ./solar-master-env/bin/activate
    # gunicorn -w 3 --bind 0.0.0.0:5001 app:create_app
    # gunicorn --worker-class eventlet --bind 0.0.0.0:5002 -w 1 --threads 100 app:create_app
    # python mongo.py
    
    # python app.py
    uvicorn main:app --reload --port 5006
}

activate