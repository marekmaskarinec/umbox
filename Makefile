
SRCS=umbox.um src/*.um umbox/versions.json
VERSION=$(shell echo $(shell jq .version <box.json))
PORTABLE=umbox_portable
PORTABLE_ZIP=umbox_portable-$(VERSION).zip
WIN_INSTALLER=umbox_install.exe

.PHONY: all clean
all: $(PORTABLE_ZIP) $(WIN_INSTALLER)
	
clean:
	rm -rf $(PORTABLE) $(PORTABLE_ZIP) $(WIN_INSTALLER)

$(PORTABLE): $(SRCS)
	@echo "BU umbox_portable.zip"
	mkdir -p umbox_portable/dat
	cp cmd/run_scripts/* umbox_portable

	cp -r umbox.um src umbox/ umbox_portable/dat
	cp README.md umbox_portable
	cp LICENSE umbox_portable

	# dirty hack to convince Make the directory changed
	touch umbox_portable/a
	rm umbox_portable/a

$(PORTABLE_ZIP): $(PORTABLE) $(SRCS)
	zip -r $(PORTABLE_ZIP) $(PORTABLE)
	
$(WIN_INSTALLER): $(PORTABLE) $(SRCS) cmd/installer.nsis
	@echo "BU umbox_install.exe"
	@echo "  (requires makensis)"
	makensis cmd/installer.nsis
