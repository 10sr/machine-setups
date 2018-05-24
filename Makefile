directories := $(shell find . -type d -depth 1)

.PHONY: check $(directories)

check: $(directories)

$(directories):
	! test -r $@/Makefile || make check -C $@
