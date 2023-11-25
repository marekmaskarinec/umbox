
SRCS=pak.um src/*.um pak/versions.json
VERSION=$(shell jq .version <pak.json)
PORTABLE=pak_portable-$(VERSION).zip

.PHONY: all clean
all: $(PORTABLE)

$(PORTABLE): $(SRCS) Makefile
	@echo "BU pak_portable.zip"
	mkdir -p pak_portable/dat
	cp cmd/run_scripts/* pak_portable

	cp -r pak.um src pak/ pak_portable/dat
	cp README.md pak_portable
	cp LICENSE pak_portable
	
	zip -r $(PORTABLE) pak_portable
	rm -r pak_portable
