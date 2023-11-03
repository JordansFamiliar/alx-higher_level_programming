#!/bin/bash
#Makes a request that causes the srever to respond with a message
curl -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me | grep -i '^Location:' | awk '{print $2}' | xargs -I % curl %
