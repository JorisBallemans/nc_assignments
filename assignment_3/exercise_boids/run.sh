#!/bin/bash

N=$1
i=$2
o=$3
c=$4
s=$5
a=$6

output_file="experiments/${N}_${i}_${o}_${c}_${s}_${a}"

if [ -e "${output_file}.csv" ]; then
    count=1
    while [ -e "${output_file}_${count}.csv" ]; do
        count=$((count + 1))
    done
    output_file="${output_file}_${count}"
fi

node node-boids-template.js -f 400 -N $N -i $i -o $o -c $c -s $s -a $a -T 1000 > "${output_file}.csv"
# node node-boids-template.js -f 400 -N $N -i $i -o $o -c $c -s $s -a $a -T 1000 -I $output_file