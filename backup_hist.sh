NOW=`date +'%Y-%m-%d_%H_%M'`;
cp /home/rmealey/.bash_history /home/rmealey/Dropbox/histories/bash_history_${NOW};
gzip /home/rmealey/Dropbox/histories/bash_history_${NOW};
