#!/bin/sh
curl http://www.graphicsmagick.org/ 2>/dev/null |grep '(Released' |sed -e 's,.*<p>,,' |cut -d' ' -f1
