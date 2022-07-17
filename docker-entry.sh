#!/bin/bash
exec gunicorn -c gunicorn.py bot_skill_server.wsgi:application