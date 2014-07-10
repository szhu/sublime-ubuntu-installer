BUILD = build/sublime-installer.zip

SRC_FILES = $(shell git ls-files src)

all: $(BUILD)

$(BUILD): $(SRC_FILES)
	rm -f $(BUILD)
	cd src && zip -r ../$(BUILD) -- $(SRC_FILES)

run: all
	python $(BUILD)

clean:
	rm -f $(BUILD)

.PHONY: all clean run
