TARGET = main
HUFF = huffman

CCX = g++
CC=gcc
CFLAGS = -Wall -g

LINKER = g++
LFLAGS = -I.

SRCDIR = src
OBJDIR = build
BINDIR = bin
INCDIR = include
DOCDIR = doc

SOURCES := $(wildcard $(SRCDIR)/*.cpp)
INCLUDES := $(wildcard $(INCDIR)/*.h)
OBJECTS := $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)
rm = rm -rf

all: $(BINDIR)/$(TARGET)


$(BINDIR)/$(TARGET): $(OBJECTS)
	@$(LINKER) $(OBJECTS) $(LFLAGS) -o $@
	@echo "Linker done"


$(OBJECTS): $(OBJDIR)/%.o : $(SRCDIR)/%.cpp
	@$(CCX) $(CFLAGS) -I$(INCDIR) -c $< -o $@
	@echo "Compiling done"

huffman:
	${CC} ${CFLAGS} -o $(BINDIR)/$(HUFF) $(SRCDIR)/huffman.c

doc:
	@doxygen Doxyfile
	@echo "Documentation done"

run_zip: all
	./bin/main 0 ../input/in1.txt

run_huffman: huffman
	$(BINDIR)/$(HUFF) encode ../input/in1.txt ../results/encoded.txt
	$(BINDIR)/$(HUFF) decode ../results/encoded.txt ../results/decoded.txt

clean:
	@$(rm) $(DOCDIR)/*
	@$(rm) $(OBJECTS)
	@$(rm) $(OBJDIR)/*.o
	@$(rm) $(BINDIR)/$(TARGET)
	@$(rm) in.tab in.rep
	@$(rm) ../results/*.tab
	@$(rm) ../results/zip.txt
	@$(rm) ../results/unzip.txt
	@$(rm) ../results/out.txt
	@$(rm) ../results/decoded.txt
	@$(rm) ../results/encoded.txt


.PHONY: all clean doc
