#!/bin/bash
# establish relative path
relative_path=$(dirname "$0")
printf "relative path is %s\\n" "$relative_path"

# import common functions
source "$relative_path/tool/shell_operations.sh"

# establish interpreter
interpreter=$relative_path"/env/bin/python"
printf "interpreter is %s\\n" "$interpreter"
file_exist "$interpreter"

# establish script
script=$relative_path"/script/main.py"
printf "script is %s\\n" "$script"
file_exist "$script"

# launch python routine
"$interpreter" "$script"
