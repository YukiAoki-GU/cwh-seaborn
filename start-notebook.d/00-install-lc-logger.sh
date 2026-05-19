
#!/bin/bash

set -eu

mkdir -p "$HOME/.ipython/profile_default/startup"

cp /home/jovyan/hooks/00_lc_logger.py "$HOME/.ipython/profile_default/startup/00_lc_logger.py"

echo "LC logger startup hook installed"

