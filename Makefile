# see also https://stackoverflow.com/a/18137056
export PYTHONPATH:=$(shell pwd)..:$(PYTHONPATH)

# Print help
HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \

# parse additional args for commands
args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
MESSAGE = "Done"
endif

# Commands
help: ##@Help Show this help
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

fmt:  ##@Code Check code and format code, with ruff settings --fix
	poetry run python3 -m ruff format
	poetry run python3 -m ruff check --fix

clean:  ##@Code Clean directory from garbage files
	rm -fr *.egg-info dist

%::
	echo $(MESSAGE)
