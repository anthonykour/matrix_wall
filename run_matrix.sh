#!/bin/bash

# Run matrix_animation.py inside Konsole and exit AFTER it starts
konsole --hold -e bash -c "
    python3 "$(dirname "$0")/matrix_animation.py"
"
