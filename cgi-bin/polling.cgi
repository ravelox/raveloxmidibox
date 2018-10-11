#!/bin/bash

echo Content-Type: text/json
echo
cat <<@EOF
{
	"returnstring" : "$(date)"
}
@EOF
exit 0
