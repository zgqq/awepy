#!/bin/bash
if [ -f "/tmp/bg" ]; then
    value=`cat /tmp/bg`
else
    touch /tmp/bglog
    value=0
    touch /tmp/bg
    echo 0>/tmp/bg
fi
i=0
count=$(ls -1 "/home/zgq/Dropbox/Images/desktop" | wc -l)
_dfiles="/home/zgq/Dropbox/Images/desktop/*"
for file in $_dfiles ; do
    if [ $i -eq $value ]; then
        tmp=$(($i+1))
        if [ $tmp -eq $count ]; then
            echo '0' > /tmp/bg
            DISPLAY=:0 feh --bg-fill "$file" 2> /tmp/bglog
        else
            ((i++))
            echo $i > /tmp/bg
            DISPLAY=:0 feh --bg-fill "$file" 2> /tmp/bglog
            break
        fi
    fi
    ((i++))
done
