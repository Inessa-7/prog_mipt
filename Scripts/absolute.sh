#!/bin/bash
mkdir /tmp/hello_world
cat <<END >/tmp/hello_world/absolute.txt
hello world!!
END
cat /tmp/hello_world/absolute.txt
lsattr /tmp/hello_world/absolute.txt
