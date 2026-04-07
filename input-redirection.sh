#!/bin/bash

cat << 'OUTER_EOF' > show-info.sh
cat -e << EOF
The current directory is: $PWD
The default paths are: $PATH
The current user is: $USERNAME
EOF
OUTER_EOF