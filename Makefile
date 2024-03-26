
SRCS=umbox.um src/*.um umbox/versions.json
VERSION=$(shell echo $(shell jq .version <box.json))
PORTABLE=umbox_portable
PORTABLE_ZIP=umbox_portable.zip
LINUX_ZIP=umbox_linux.zip
WINDOWS_ZIP=umbox_windows.zip
WIN_INSTALLER=umbox_install.exe

.PHONY: all clean
all: $(PORTABLE_ZIP) $(WIN_INSTALLER) $(WINDOWS_ZIP) $(LINUX_ZIP)
	
clean:
	rm -rf $(PORTABLE) $(PORTABLE_ZIP) $(WIN_INSTALLER) $(WINDOWS_ZIP) $(LINUX_ZIP)

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

$(LINUX_ZIP): $(PORTABLE) $(SRCS)
	cp -r $(PORTABLE) umbox_linux
	rm -f `find umbox_linux/ -name \*.exe`
	rm -f `find umbox_linux/ -name \*.dll`
	rm -f `find umbox_linux/ -name \*.bat`
	rm -f `find umbox_linux/ -name \*_windows.umi`
	zip -r $(LINUX_ZIP) umbox_linux
	rm -rf umbox_linux

$(WINDOWS_ZIP): $(PORTABLE) $(SRCS)
	cp -r $(PORTABLE) umbox_windows
	rm -f `find umbox_windows/ -name \*.so`
	rm -f `find umbox_windows/ -name \*_linux.umi`
	rm -f umbox_windows/umka/umka
	zip -r $(WINDOWS_ZIP) umbox_windows
	rm -rf umbox_windows

$(PORTABLE_ZIP): $(PORTABLE) $(SRCS)
	zip -r $(PORTABLE_ZIP) $(PORTABLE)
	
$(WIN_INSTALLER): $(PORTABLE) $(SRCS) cmd/installer.nsis
	@echo "BU umbox_install.exe"
	@echo "  (requires makensis)"
	makensis cmd/installer.nsis
