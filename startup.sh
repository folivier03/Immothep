#!/bin/bash

pip install -r requirements.txt 
uvicorn srv.main:app --host 0.0.0.0 --port 80
