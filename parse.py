#!/usr/bin/env python
import fileinput
with fileinput.input('ome.obo', inplace=True) as f:
    count = 0
    for line in f:
        if line.startswith("id: "):
            line = f"id: OME:{count:04}\n"
            count += 1
        print(line, end='')
