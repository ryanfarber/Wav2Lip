import re
import datetime

date = datetime.datetime.now()
ts = date.strftime("%y%m%d-%H%M%S")

checkpointName = re.search("(?<=checkpoints/).+?(?=.pth)", config.checkpoint)
if not checkpointName:
	checkpointName = "checkpoint_name"
else:
	checkpointName = checkpointName.group()

filename = f"{checkpointName}_{ts}"
print(filename)