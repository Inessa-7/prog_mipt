#!/bin/bash
mkdir ../hello_world
echo 'hello parent!!' >> ../hello_world/home.txt
cat ../hello_world/home.txt
lsattr ../hello_world/home.txt
