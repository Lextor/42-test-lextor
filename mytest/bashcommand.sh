#!/bin/bash

python manage.py project_info 2> $(date +'%Y-%m-%d').dat
