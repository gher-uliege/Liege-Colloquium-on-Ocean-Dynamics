#!/bin/bash

# Compute the number of different countries in each edition 
# of the Colloquium.

# ctroupin, August 2017

datadir="/home/ctroupin/Projects/Liege-Colloquium-on-Ocean-Dynamics/data/"

for datafile in $(ls ${datadir}"/"*"dat"); do
  echo " " 
  echo ${datafile} | egrep -o '[0-9]{4}'
  awk -F "\t" '{print ($4)} ' $datafile | sort | uniq | wc -l
done  
