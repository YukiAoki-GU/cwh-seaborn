#!/bin/bash
set -eu

mkdir -p "$HOME/.ipython/profile_default/startup"

if [ -f /home/jovyan/hooks/00_lc_logger.py ]; then
  cp /home/jovyan/hooks/00_lc_logger.py "$HOME/.ipython/profile_default/startup/00_lc_logger.py"
elif [ -f "$PWD/hooks/00_lc_logger.py" ]; then
  cp "$PWD/hooks/00_lc_logger.py" "$HOME/.ipython/profile_default/startup/00_lc_logger.py"
fi

echo "LC logger startup hook installed"
