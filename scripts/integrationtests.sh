#!/bin/bash
set -e

python3 -m pip install .

pip install -r requirements.txt

pytest ./integration-tests/

result=$?

cd "$current_directory"

exit $result
