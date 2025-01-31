all:
	cd ../../ttl2html-doc/ && git pull
	cp -f ../../ttl2html-doc/docs/*.rst .
	sphinx-build -b gettext . _build/gettext
	tx push --source
	tx pull --all
	for f in locales/*/LC_MESSAGES/*.po; do \
	  echo "$$f"; \
	  msgcat --no-wrap -o "$$f" "$$f"; \
	done
