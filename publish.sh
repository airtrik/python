source env/bin/activate
rm -r dist/*
python setup.py sdist bdist_wheel
twine upload dist/*