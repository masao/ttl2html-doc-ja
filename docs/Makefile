all:
	cd ../../ttl2html-doc/ && git pull
	cp -f ../../ttl2html-doc/docs/*.rst .
	sphinx-build -b gettext . _build/gettext
	tx push --source
	tx pull --all
