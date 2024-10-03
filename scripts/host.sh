#!/bin/bash

# --- Check if the OS is Mac
if [[ "$OSTYPE" != "darwin"* ]]; then
  echo "This script is designed to run only on macOS."
  exit 1
fi

# --- Variables
HOST1="ytb-analyser"
HOST2="api.ytb-analyser"
IP="127.0.0.1"
HOSTS_FILE="/etc/hosts"

# --- Function to add a host if not present
add_host() {
  local host="$1"
  local ip="$2"
  if ! grep -q "$host" "$HOSTS_FILE"; then
    echo "$ip  $host" | sudo tee -a "$HOSTS_FILE" >/dev/null
    echo "Entry for $host has been added."
  else
    echo "Entry for $host already exists."
  fi
}

# --- Add the entries to the hosts file
add_host "$HOST1" "$IP"
add_host "$HOST2" "$IP"

# --- Display success message
echo "Entries for $HOST1 and $HOST2 have been added/verified in the /etc/hosts file."
