PACKAGE=ggmm
PREFIX=/usr/local
BINDIR=$(PREFIX)/bin
DOCDIR=$(PREFIX)/share/doc/$(PACKAGE)

.PHONY: all build install
all: build

build:
	./GIT-VERSION-GEN

install: build
	install -m 755 $(PACKAGE) $(BINDIR)
	mkdir -p $(DOCDIR)
	install -m 644 LICENSE $(DOCDIR)
	install -m 644 README.md $(DOCDIR)

uninstall:
	rm -rf $(BINDIR)/$(PACKAGE)
	rm -rf $(DOCDIR)/LICENSE
	rm -rf $(DOCDIR)/README.md

clean:
	-@rm -rf $(PACKAGE) *~

test: build
	python3 $(PACKAGE) -a && test -s irc_meeting_log.eml
