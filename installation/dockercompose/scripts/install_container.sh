#!/bin/bash
set -x

dos2unix scripts/install_python3.sh scripts/install_python3.sh
chmod +x scripts/install_python3.sh
scripts/install_python3.sh

while true
do
	echo "Press [CTRL+C] to stop.."
	sleep 1
done




