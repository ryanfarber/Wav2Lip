# config.py
# this is my custom config

# python3 inference.py --checkpoint_path "./checkpoints/wav2lip_gan.pth" --face "./input/face_b3_480.mp4" --audio "./input/5.wav" --pads 0 15 0 0

# options
# wav2lip.pth
# wav2lip_gan.pth
# lipsync_exper.pth
checkpoint = "./checkpoints/wav2lip_gan.pth"
video = "./input/pic.jpeg"
audio = "./input/audio2.wav"
chinPad = 15
nosmooth = False 

# python3 inference.py --checkpoint_path "./checkpoints/wav2lip_gan.pth" --face "./input/test.mov" --audio "./input/comments.wav" --pads 0 15 0 0


# video = "./input/face_a_30sec.mp4"