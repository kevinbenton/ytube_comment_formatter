#!/bin/bash

string1="North Korea"
string2="Doesn't even lift"

echo $string1

for i in `seq 2 ${#string1}`
do
  echo ${string1:0:(-$i+1)}
done

for i in `seq 1 ${#string2}`
do
  echo ${string2:0:($i)}
done
