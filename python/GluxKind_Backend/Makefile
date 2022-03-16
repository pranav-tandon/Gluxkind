.PHONY:	logs clean_logs start stop restart push build
install_requirements:
    $(info Install: Installing python libraries for script")
    pip install -r requirements.txt

run:
    $(info Run: Running python script")
    python parser.py

build:
	@make -s install_requirements
	@make -s run


