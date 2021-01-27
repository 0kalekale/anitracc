PY = python3

setup: 
	mkdir instance && touch instance/config.json

run: 
	$(PY) anitracc/server.py 
	
clean: 
	rm -rf instance/* && rm -rf instance
