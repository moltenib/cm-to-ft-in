#!/bin/sh

### cm-to-ft-in: Converts CM to feet and inches.

[ $# -ne 1 ] && {
    cat << EOF
Usage: $0 CM
EOF
    exit 1
}

format_() {
    printf "%d'%1.f\"\n" $@
}

format_ $(
bc << EOF
a = $1
a / 30.48
b = a % 30.48
scale = 1
b / 2.54
EOF
)

