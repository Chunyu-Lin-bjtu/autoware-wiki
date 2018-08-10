#!/bin/bash

set -Ceu

rm -rf Autoware
git clone https://github.com/CPFL/Autoware.git
python3 UpdateReadmeList/UpdateReadmeList.py ../Readme-List.md UpdateReadmeList/ReadmeListHeader.md
