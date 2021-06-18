#!/bin/bash

echo "Instrument: $1"


./symbol-frame.py $1

vd $1.csv