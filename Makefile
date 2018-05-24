directories := $(shell find . -maxdepth 1 -type d)

.PHONY: check $(directories)

check: $(directories)

$(directories):
	! test -r $@/Makefile || make check -C $@
