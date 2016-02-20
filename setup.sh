if [ ! -d bin ]; then
	virtualenv .
	source bin/activate
	pip install -r requirements.txt
fi
