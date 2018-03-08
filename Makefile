TIMESTAMP=`date +"%Y%m%d.%s"`
run-flake8:
	flake8 hl7apy

run-tests:
	nosetests tests hl7apy --with-doctest --with-coverage --cover-package hl7apy

run-profile:
	nosetests tests hl7apy --with-cprofile --cprofile-stats-file=stats-$(TIMESTAMP).prof hl7apy

install-deps:
	pip install nose coverage flake8 nose-cprof