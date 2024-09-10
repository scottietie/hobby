#! /bin/sh

CURDIR=$(dirname `readlink -f $0`)

while :
do
	python3 $CURDIR/application.py
done

