mkdir /swap
/bin/dd if=/dev/zero of=/swap/extra2.swap bs=30M count=1024
/sbin/mkswap /swap/extra2.swap
/sbin/swapon /swap/extra2.swap
