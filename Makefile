
SRCS=pak.um src/*.um pak/versions.json
VERSION=$(shell jq .version <pak.json)
PORTABLE=pak_portable
PORTABLE_ZIP=pak_portable-$(VERSION).zip
WIN_INSTALLER=pak_install.exe

.PHONY: all clean
all: $(PORTABLE_ZIP) $(WIN_INSTALLER)
	
clean:
	rm -rf $(PORTABLE) $(PORTABLE_ZIP) $(WIN_INSTALLER)

$(PORTABLE): $(SRCS) Makefile
	@echo "BU pak_portable.zip"
	mkdir -p pak_portable/dat
	cp cmd/run_scripts/* pak_portable

	cp -r pak.um src pak/ pak_portable/dat
	cp README.md pak_portable
	cp LICENSE pak_portable

$(PORTABLE_ZIP): $(PORTABLE)
	zip -r $(PORTABLE_ZIP) $(PORTABLE)
	
$(WIN_INSTALLER): $(PORTABLE) cmd/installer.nsis
	@echo "BU pak_install.exe"
	@echo "  (requires makensis)"
	makensis cmd/installer.nsis