CC = gcc
CFLAGS = -Wall -Wextra -std=c11

all: bcsp_generate.exe bcsp_validate.exe bcsp.exe

bcsp_generate.exe: bcsp_generate.c
	$(CC) $(CFLAGS) $< -o $@

bcsp_validate.exe: bcsp_validate.c
	$(CC) $(CFLAGS) $< -o $@

bcsp.exe: bcsp.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f bcsp_generate.exe bcsp_validate.exe bcsp.exe
