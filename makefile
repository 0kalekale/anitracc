PY = python3

install: 
	pip3 install requests anilistpy flask 
	
setup: 
	mkdir instance && touch instance/config.json

run: 
	$(PY) anitracc/server.py 
	
clean: 
	rm -rf instance/* && rm -rf instance
