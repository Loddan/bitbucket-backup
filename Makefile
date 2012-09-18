SHELL := /bin/bash

env:
	rm ./env -fr
	virtualenv ./env
	/bin/bash -c 'source ./env/bin/activate ; pip install -e . '
