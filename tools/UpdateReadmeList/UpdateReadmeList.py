import sys
from pathlib import Path
import re

args = sys.argv
if len(args) != 4:
    print("Usage: UpdateReadmeList.py output_file header_file")
    sys.exit(1)

output_file_name = args[1]
header_file_name = args[2]
git_hash         = args[3]

local_paths = [readme.as_posix() for readme in Path(".").glob("**/README.md")]
github_prefix = "https://github.com/CPFL/Autoware/tree/master/"

with open(output_file_name, mode="w") as output_file:
    with open(header_file_name) as header_file:
        header = header_file.read()
        git_hash_prefix = git_hash[0:7]
        git_link = "[" + git_hash_prefix + "](" + "https://github.com/CPFL/Autoware/commit/" + git_hash + ")"
        header = header.replace("HEAD", git_link)
        output_file.write(header)
    for local_path in local_paths:
        github_path = local_path.replace("Autoware/", "", 1)
        github_uri  = github_prefix + github_path
        output_file.write("- [" + github_path + "]" + "(" + github_uri + ")\n")
