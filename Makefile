BUILD = build/sublime-installer.zip
STRINGS_SRC = src/strings/strings.yml
STRINGS_BUILD = src/installer/strings.py

GIT_LS_ARGS = -mo --exclude-standard
INSTALLER_FILES_LOC = src/installer
SRC_FILES_REL_SRC = $(shell cd $(INSTALLER_FILES_LOC) && git ls-files -mo --exclude-standard)
SRC_FILES_REL_ROOT = $(shell git ls-files -mo --exclude-standard $(INSTALLER_FILES_LOC))

all: Makefile $(BUILD)

$(BUILD): Makefile $(SRC_FILES_REL_ROOT)
	rm -f $(BUILD)
	cd $(INSTALLER_FILES_LOC) && zip -r ../$(BUILD) -- $(SRC_FILES_REL_SRC)

$(STRINGS_BUILD): Makefile src/strings/process_strings.py $(STRINGS_SRC)
	python src/strings/process_strings.py $(STRINGS_SRC) $(STRINGS_BUILD)

strings: Makefile $(STRINGS_BUILD)

run: Makefile all
	python $(BUILD)

clean:
	rm -f $(BUILD) $(STRINGS_BUILD)

.PHONY: all clean run strings
