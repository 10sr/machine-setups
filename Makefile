directories := $(shell find * -maxdepth 0 -type d)

.PHONY: install check $(directories)

install check: $(directories)

$(directories):
	! test -r $@/Makefile || $(MAKE) $(MAKECMDGOALS) -C $@
