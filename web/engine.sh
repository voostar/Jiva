#!/bin/bash
# This script will control runserver

# startup
COMMAND="$1" # operation type
IPADDR=`grep "IPADDR" engine.cfg | awk -F'=' '{print $2}'` # read IP address from cfg
PORT=`grep "PORT" engine.cfg | awk -F'=' '{print $2}'` # read IP address from cfg
echo "[+]This Django instance runs \"${COMMAND}\" on ${IPADDR}:${PORT}"

case $COMMAND in
start)
	echo "[+]Starting instance on ${IPADDR}:${PORT}"
	nohup python2.7 manage.py runserver ${IPADDR}:${PORT} 2>/dev/null &
	echo "[+]Done."
	;;
stop)
	echo "[+]Stoping instance on ${IPADDR}:${PORT}"
	PID=`ps -ef | grep "runserver ${IPADDR}:${PORT}" | grep -v grep | awk '{print $2}'`
	if [ x"$PID" = x ];then
		echo "[+]Django instance NOT running. Exit."
	else
		echo "---[-]Killing PID: ${PID}"
		ps -ef | grep "runserver ${IPADDR}:${PORT}" | grep -v grep | awk '{print $2}' | xargs kill -9
		echo "[+]Done."
	fi
	;;
*)
	echo "Args not accpect, showing the instance status. You can use \"start\" or \"stop\" to enable\kill this instance." 
	PID=`ps -ef | grep "runserver ${IPADDR}:${PORT}" | grep -v grep | awk '{print $2}'`
	if [ x"$PID" = x ];then
		echo "[+]Django instance NOT running as well."
	else
		echo "[+]Django instance:"
		ps -ef | grep "runserver ${IPADDR}:${PORT}" | grep -v grep
	fi
	exit 1
esac
