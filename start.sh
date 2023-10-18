set -eu

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
    curl --silent --show-error --retry 5 https://bootsrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requiments.txt

$VIRTUALENV/bin/python3 app.py
Footer