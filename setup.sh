#! /bin/sh

# Install the required packages from pip
if type pip > /dev/null 2>&1; then
  sudo -H pip install -r requirements.txt
else 
  echo "Could not find 'pip'"
  exit
fi

# Do we have homebrew? If so, use that to install terminal-notifier
if type brew > /dev/null 2>&1; then
  brew install terminal-notifier
# What about macports?
elif type ports > /dev/null 2>&1; then
  ports install terminal-notifier
else 
  echo "Unable to locate 'Homebrew' or 'MacPorts'"
  exit
fi

# Now let's make things executable and start it
cp check_conn.py check_conn
chmod u+x check_conn

echo "Done"
exit 0