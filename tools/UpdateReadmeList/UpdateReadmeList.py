import sys
from pathlib import Path
import re

args = sys.argv
if len(args) != 3:
    print("Usage: UpdateReadmeList.py output_file header_file")
    sys.exit(1)

output_file_name = args[1]
header_file_name = args[2]

local_paths = [readme.as_posix() for readme in Path(".").glob("**/README.md")]
github_prefix = "https://github.com/CPFL/Autoware/tree/master/"

with open(output_file_name, mode="w") as output_file:
    with open(header_file_name) as header_file:
        output_file.write(header_file.read())
    for local_path in local_paths:
        github_path = local_path.replace("Autoware/", "", 1)
        github_uri  = github_prefix + github_path
        output_file.write("- [" + github_path + "]" + "(" + github_uri + ")\n")
