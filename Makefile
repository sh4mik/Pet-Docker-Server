#.PHONY build start stop clean healthcheck

build:
	docker-compose build

start: build
	docker-compose up

stop:
	docker-compose stop

clean:
	docker-compose stop
	docker-compose rm

healthcheck:
	@if (docker --version 1> /dev/null 2> /dev/null); then echo "OK"; else echo "install docker" | exit; fi
	@if (flask --version 1> /dev/null 2> /dev/null); then echo "OK"; else echo "install flask" | exit; fi
	@if (redis --version 1> /dev/null 2> /dev/null); then echo "OK"; else echo "install redis" | exit; fi
	@if (pymongo --version 1> /dev/null 2> /dev/null); then echo "OK"; else echo "install pymongo" | exit; fi

.PHONY: build start stop clean healthcheck
