#!/bin/bash
source env/bin/activate
rm -r dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
ver=$(<version.txt)
git add .
git commit -m "v"$ver
git push -u origin master
git checkout -b "v"$ver
git push -u origin "v"$ver