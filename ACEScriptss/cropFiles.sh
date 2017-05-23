#!/bin/bash
for file in /home/asampath/IPDomainMap/src/CropFiles/*
do
  tail -n +2 "$file" | head -n -2 > "${file}"-new && mv "${file}"-new "$file"
done
