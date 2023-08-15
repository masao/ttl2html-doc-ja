all:
	cd ../../ttl2html-doc/ && git pull && cp -f docs/*.rst .
	sphinx-build -b gettext . _build/gettext
	tx push --source
	tx pull --all
