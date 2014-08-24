BUILD = build/sublime-installer.zip
STRINGS_SRC = src/strings/strings.yml
STRINGS_BUILD = src/installer/sublime_strings.py

GIT_LS_ARGS = --exclude-standard
INSTALLER_FILES_LOC = src/installer
INSTALLER_FILES_RLOC = ../..
SRC_FILES_REL_SRC = $(shell cd $(INSTALLER_FILES_LOC) && git ls-files $(GIT_LS_ARGS))
SRC_FILES_REL_ROOT = $(shell git ls-files $(GIT_LS_ARGS) $(INSTALLER_FILES_LOC))

all: Makefile strings $(BUILD)

$(BUILD): Makefile $(SRC_FILES_REL_ROOT)
	rm -f $(BUILD)
	cd $(INSTALLER_FILES_LOC) && zip -r $(INSTALLER_FILES_RLOC)/$(BUILD) -- $(SRC_FILES_REL_SRC)

$(STRINGS_BUILD): Makefile src/strings/process_strings.py $(STRINGS_SRC)
	python src/strings/process_strings.py $(STRINGS_SRC) $(STRINGS_BUILD)

strings: Makefile $(STRINGS_BUILD)

run: Makefile all
	python $(BUILD)

clean:
	rm -f $(BUILD) $(STRINGS_BUILD)

.PHONY: all clean run strings
