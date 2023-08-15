all:
	cd ../ttl2html-doc/ && git pull
	sphinx-build -b gettext . _build/gettext
	tx push --source
	tx pull --all
