#!/bin/bash

if [ "$#" -ne 5 ]; then
    echo "Usage: $0 [customer_id] [developer_token] [client_id] [client_secret] [refresh_token]"
    exit 1
fi

if ! [ -x "$(command -v python3)" ]; then
    echo 'Error: python3 is not installed.' >&2
    exit 1
fi

if [[ $(python3 --version 2>&1) == *"3.6"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.7"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.8"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.9"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.10"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.11"* ]] ||
    [[ $(python3 --version 2>&1) == *"3.12"* ]]; then
    echo 'Python version is 3.6 or higher'
else
    echo 'Error: Python version is not 3.6 or higher.' >&2
    exit 1
fi

if ! [ -x "$(command -v sed)" ]; then
    echo 'Error: sed is not installed.' >&2
    exit 1
fi

customer_id=$1
developer_token=$2
client_id=$3
client_secret=$4
refresh_token=$5

sed -i '' "s|customer_id = '.*'|customer_id = '$customer_id'|" index.py
sed -i '' "s|developer_token = '.*'|developer_token = '$developer_token'|" index.py
sed -i '' "s|client_id = '.*'|client_id = '$client_id'|" index.py
sed -i '' "s|client_secret = '.*'|client_secret = '$client_secret'|" index.py
sed -i '' "s|refresh_token = '.*'|refresh_token = '$refresh_token'|" index.py

#venv is not exist then create venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller

pyinstaller --onefile --additional-hooks-dir=./hooks --name kwplanner index.py

chmod +x dist/kwplanner
sudo mv dist/kwplanner /usr/local/bin/

echo "Setup complete. The executable is now available in /usr/local/bin"

# disable venv
source deactivate
