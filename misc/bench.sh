#!/usr/bin/bash -eu

DISPLAY_NAME=""
RESULT_FILE=/tmp/result.txt


/home/isucon/private_isu.git/benchmarker/bin/benchmarker  -u /home/isucon/private_isu.git/benchmarker/userdata -t "http://52.197.181.153" > ${RESULT_FILE}

SCORE=$(cat ${RESULT_FILE} | grep -o \"score\":[0-9]* | grep -o [0-9]*)

echo "Score: " ${SCORE}

aws --profile=score-board cloudwatch put-metric-data \
  --namespace private-isu \
  --metric-name score \
  --dimensions Team="${DISPLAY_NAME}" \
  --value ${SCORE}