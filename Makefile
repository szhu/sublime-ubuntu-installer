BUILD = build/sublime-installer.zip

SRC_FILES_REL_SRC = $(shell cd src && git ls-files)
SRC_FILES_REL_ROOT = $(shell git ls-files src)

all: $(BUILD)

$(BUILD): $(SRC_FILES_REL_ROOT)
	rm -f $(BUILD)
	cd src && zip -r ../$(BUILD) -- $(SRC_FILES_REL_SRC)

run: all
	python $(BUILD)

clean:
	rm -f $(BUILD)

.PHONY: all clean run
