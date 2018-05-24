directories := $(shell find * -maxdepth 0 -type d)

.PHONY: check $(directories)

check: $(directories)

$(directories):
	! test -r $@/Makefile || make check -C $@
