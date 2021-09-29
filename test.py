import re
import datetime
import librosa

# date = datetime.datetime.now()
# ts = date.strftime("%y%m%d-%H%M%S")

# checkpointName = re.search("(?<=checkpoints/).+?(?=.pth)", config.checkpoint)
# if not checkpointName:
# 	checkpointName = "checkpoint_name"
# else:
# 	checkpointName = checkpointName.group()

# filename = f"{checkpointName}_{ts}"
# print(filename)





# gets duration of wav file and converts to minutes & seconds
def convert(duration):
	if duration > 60:
		minutes = round(duration / 60)
		seconds = round(duration - minutes * 60)
		return f"{minutes}m{seconds}s"
	else:
		return f"{round(duration)}s"
	
