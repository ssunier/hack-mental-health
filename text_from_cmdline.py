import subprocess
import sys

NUM=sys.argv[1]
MESSAGE=" ".join(sys.argv[2:])
# curl -X POST http://textbelt.com/text -d number=7178238102 -d "message=http://www.facebook.com"
cmd=["curl","-XPOST","http://textbelt.com/text","-d","number="+str(NUM),"-d","message="+MESSAGE]
subprocess.check_output(cmd)
