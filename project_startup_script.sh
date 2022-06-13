#!/bin/bash

# Run command in the background
_evalBg(){
	eval "$@" &>/dev/null & disown;
}
# Commands
backend_cmd="uvicorn routes.main:app --reload";
frontend_cmd="npm start";

# Backend startup
echo "Starting backend server ...";
cd ./backend;
source env/bin/activate;
_evalBg "${backend_cmd}";
deactivate;
echo "Backend startup complete.";

# Frontend startup
echo " ";
echo "Starting frontend server ...";
cd ..;
cd ./frontend/discount-frontend;
_evalBg "${frontend_cmd}";
echo "Frontend server started.";

# Exit
cd ..;
cd ..;
echo " ";
echo "Script exited with no erorrs.";
