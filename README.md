# iiit-selenium-workshop

## Installation

* Install python 3.7
* Clone this directory
```
git clone git@github.com:raj454raj/iiit-selenium-workshop.git
cd iiit-selenium-workshop
```
* Create a virtualenv in python `venv`
```
virtualenv --python python3.7 venv
```
* Source the environment
```
source venv/bin/activate
```
* Install the requirements
```
pip install -r requirements.txt
```
* Copy BrowserStack's credentials in bash environment (You can also add this to `~/.bash_profile` or `~/.bashrc`)
```
export automate_username="<your_browserstack_username>"
export automate_authkey="<your_browserstack_authkey>"
```
