#!/bin/bash

echo "# Autogenerated - DO NOT EDIT BY HAND" > main.py
echo "#" >> main.py
echo "# DISCLAIMER: Strange file organization is used for code generation of the corresponding blog post." >> main.py

for file in $(ls breakout); do
   echo -e "\n\n# ------------------------------------------------------" >> main.py
   echo "# ${file}" >> main.py
   echo -e "# ------------------------------------------------------" >> main.py

   cat breakout/$file >> main.py
done
