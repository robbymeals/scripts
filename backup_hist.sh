#!/bin/bash
NOW=`date +'%Y-%m-%d_%H_%M'`;
cp /home/${USER}/.bash_history /home/${USER}/Dropbox/histories/bash_history_${NOW};
gzip /home/${USER}/Dropbox/histories/bash_history_${NOW};
