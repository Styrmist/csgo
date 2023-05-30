define HELPBODY
Available commands:

	make help       - this thing.

	make init       - install python dependancies
	make test       - run tests and coverage
	make pylint     - code analysis
	make build      - pylint + test
	make docs       - generate html docs using sphinx

	make dist		- build source distribution
	mage register	- register in pypi
	make upload 	- upload to pypi

	make pb_fetch   - fetch protobufs from SteamRE
	make pb_compile - compile with protoc
	make pb_clear   - removes *.proto
	make pb_update  - pb_fetch + pb_compile

endef

export HELPBODY
help:
	@echo "$$HELPBODY"

init:
	pip3 install -r requirements.txt

test:
	coverage erase
	PYTHONHASHSEED=0 nosetests --verbosity 1 --with-coverage --cover-package=csgo

pylint:
	pylint -r n -f colorized csgo || true

build: pylint test docs

.FORCE:
docs: .FORCE
	$(MAKE) -C docs html

clean:
	rm -rf dist csgo.egg-info csgo/*.pyc

dist: clean
	python setup.py sdist

register:
	python setup.py register -r pypi

upload: dist register
	twine upload -r pypi dist/*

pb_fetch:
	wget -nv --show-progress -N -P ./protobufs/ -i protobuf_list.txt
	sed -i '' -e '1s/^/syntax = "proto2"\;\npackage custom_csgo\;\n/' protobufs/*.proto
	sed -i '' -E 's/(optional|repeated) \.([A-Z])/\1 custom_csgo.\2/' protobufs/*.proto
	sed -i '' -e 's/cc_generic_services/py_generic_services/' protobufs/*.proto

pb_compile:
	for filepath in `ls ./protobufs/*.proto`; do \
		protoc  --python_out ./custom_csgo/protobufs/ --pyi_out=./custom_csgo/protobufs/ --proto_path=./protobufs "$$filepath"; \
	done;
	sed -i '' -e '/^import sys/! s/^import /import custom_csgo.protobufs./' custom_csgo/protobufs/*_pb2.py
	sed -i '' -e '/^import sys/! s/^import /import custom_csgo.protobufs./' custom_csgo/protobufs/*_pb2.pyi

pb_clear:
	rm -f ./protobufs/*.proto ./custom_csgo/protobufs/*_pb2.py

gen_enums:
	python3 gen_enum_from_protos.py > custom_csgo/proto_enums.py

pb_update: pb_fetch pb_compile gen_enums
