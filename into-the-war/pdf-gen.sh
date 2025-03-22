#!/bin/bash

pandoc advanced.md -o Into-the-War-Advanced.pdf -V papersize:a5 -V geometry:margin=.5in -L ../pagebreak.lua
pandoc basic.md -o Into-the-War.pdf -V papersize:a5 -V geometry:margin=.5in -L ../pagebreak.lua

git status && git add . && git commit -m "updates" && git push
