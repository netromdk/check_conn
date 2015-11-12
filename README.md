# Check_conn

Get notified when your internet connection drops and when it comes back 
up. I use it where connection is poor.

# Installation

* Clone this repo
* Execute `./setup.sh` - which will install all the dependencies
* Execute the application `./check_conn&`

# Troubleshooting

* Make sure the correct Python binary is being used
* Ensure the script is executable `chmod u+x check_conn.py`
* If you're not using `homebrew` or `macports` you can download the binary for
[terminal-notifier](https://github.com/julienXX/terminal-notifier/releases) 
and place in your path so `check_conn` can execute it.
