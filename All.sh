#!/bin/bash

for i in plot_* ; do python $i ; done ; for i in fig*.pdf ; do echo ; echo $i ; pdffonts $i ; done
