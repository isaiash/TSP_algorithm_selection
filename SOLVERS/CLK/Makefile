# Generated automatically from Makefile.in by configure.
#
#   This file is part of CONCORDE
#
#   (c) Copyright 1995--1999 by David Applegate, Robert Bixby,
#   Vasek Chvatal, and William Cook
#
#   Permission is granted for academic research use.  For other uses,
#   contact the authors for licensing options.
#
#   Use at your own risk.  We make no guarantees about the
#   correctness or usefulness of this code.
#


SHELL = /bin/sh
SRCROOT = ../../concorde
BLDROOT = ..
CCINCDIR=$(SRCROOT)/INCLUDE

srcdir = ../../concorde/LINKERN
VPATH = ../../concorde/LINKERN

CC = gcc
CFLAGS = -g -O3  -I$(BLDROOT)/INCLUDE -I$(CCINCDIR)
LDFLAGS = -g -O3 
LIBFLAGS = -lm 
RANLIB = ranlib

OBJ_SUFFIX = o
o = $(OBJ_SUFFIX)

THISLIB=linkern.a
LIBSRCS=linkern.c linkern_fixed.c linkern_path.c flip_two.c
ALLSRCS=lk_main.c $(LIBSRCS)

LIBS=$(BLDROOT)/EDGEGEN/edgegen.a $(BLDROOT)/KDTREE/kdtree.a \
     $(BLDROOT)/FMATCH/fmatch.a   $(BLDROOT)/UTIL/util.a

all: linkern $(THISLIB)

everything: all

linkern: lk_main.$o $(THISLIB) $(LIBS)
	$(CC) $(LDFLAGS) -o $@ lk_main.$o $(THISLIB) $(LIBS) $(LIBFLAGS)

clean:
	-rm -f *.$o $(THISLIB) linkern

OBJS=$(LIBSRCS:.c=.o)

$(THISLIB): $(OBJS)
	$(AR) $(ARFLAGS) $(THISLIB) $(OBJS)
	$(RANLIB) $(THISLIB)

.PHONY: $(BLDROOT)/concorde.a
$(BLDROOT)/concorde.a: $(OBJS)
	$(AR) $(ARFLAGS) $(BLDROOT)/concorde.a $(OBJS)
	$(RANLIB) $(BLDROOT)/concorde.a

include ../INCLUDE/Makefile.common

# DO NOT DELETE THIS LINE -- make depend depends on it.

I=$(CCINCDIR)
I2=$(BLDROOT)/INCLUDE

flip_two.$o: flip_two.c $(I)/machdefs.h $(I2)/config.h  $(I)/util.h     \
        $(I)/linkern.h  
linkern.$o:  linkern.c  $(I)/machdefs.h $(I2)/config.h  $(I)/linkern.h  \
        $(I)/util.h     $(I)/kdtree.h   $(I)/macrorus.h 
lk_main.$o:  lk_main.c  $(I)/machdefs.h $(I2)/config.h  $(I)/linkern.h  \
        $(I)/util.h     $(I)/kdtree.h   $(I)/edgegen.h  $(I)/macrorus.h 
