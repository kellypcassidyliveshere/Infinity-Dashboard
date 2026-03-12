#!/bin/bash
while true; do
    CURRENT_TIME=$(date +%H:%M)
    if [ "$CURRENT_TIME" == "23:00" ]; then
        termux-notification -t "Reflection Time" -c "Kelly-Ann, time for Reflection & Gratitude."
        sleep 61
    elif [ "$CURRENT_TIME" == "01:00" ]; then
        termux-notification -t "Prayer Time" -c "1 AM: Time for your sacred prayer."
        sleep 61
    fi
    sleep 30
done
