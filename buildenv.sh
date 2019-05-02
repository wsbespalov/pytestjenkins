mkdir -p reports
REPO="http://127.0.0.1:8888"
echo Checking for local repo at ${REPO}
curl -f --head ${REPO} > /dev/null 2>&1 || REPO='http://pypi.python.org/simple'
echo "... will use ${REPO}"
echo 'Creating "venv" environment...'
virtualenv --distribute --no-site-packages venv
echo 'Installing dependencies to "venv" environment...'
if [ x$1 == x"--ci" ]; then
    echo "Testing mode."
    PIP=reqs
else
    echo "Dev/deploy mode."
    PIP=stuff
fi
.\venv\Scripts\pip install -q -i ${REPO} -E venv -r .\pip-${PIP}.txt
virtualenv --relocatable venv