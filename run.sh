#!/bin/sh

export FLASK_APP=app.py
printf ""
printf "\\n[*] Use the URL format: http://localhost:5000/[woff|woff2]/(variant)/(size)\\n"
printf "[*] Valid sizes include: 8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 30, 36, 48, 60, 72, 90\\n\\n"
flask run
