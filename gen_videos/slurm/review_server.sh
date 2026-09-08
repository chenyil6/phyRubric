#!/bin/bash
# Idempotent: make sure the review web server is running on THIS login node.
# Serves ~/phyRubric on 127.0.0.1:8765 (only reachable through the SSH tunnel).
#   ssh delta 'bash ~/phyRubric/gen_videos/review_server.sh'
cd ~/phyRubric || exit 1
if pgrep -u "$USER" -f "http.server 8765" >/dev/null; then
  echo "review server already running on $(hostname)"
else
  mkdir -p gen_videos/logs
  setsid nohup python3 -m http.server 8765 --bind 127.0.0.1 --directory "$HOME/phyRubric" \
    > gen_videos/logs/http_server.log 2>&1 < /dev/null & disown
  sleep 1
  echo "review server started on $(hostname)"
fi
echo "pages:"; ls gen_videos/review/*.html 2>/dev/null | sed 's|.*/|  http://localhost:8765/gen_videos/review/|'
