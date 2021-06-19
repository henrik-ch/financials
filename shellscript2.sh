#!/usr/bin/env nix-shell
#! nix-shell -i bash

symbol=$1
start=$2
end=$3

# echo "Retrieving frame for $symbol, starting from $start"
python symbol-frame.py $symbol $start $end

echo "Opening retreived data with vd"
vd $symbol.csv
