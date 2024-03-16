from pydub import AudioSegment as AS

src = "g_23"
dst = "g_23.wav"

audSeg = AS.from_mp3(src + ".mp3")
audSeg.export(dst, format="wav")
