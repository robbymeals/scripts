#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
mkdir /swap && /bin/dd if=/dev/zero of=/swap/extra.swap bs=30M count=1024 && /sbin/mkswap /swap/extra.swap && /sbin/swapon /swap/extra.swap
