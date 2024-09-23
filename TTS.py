from elevenlabs import save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key = "enterAPIKey",
)

audio = client.generate(
    text = "Hi, this is a test",
    voice = "Rachel",
    model = "eleven_multilingual_v2"
)

save(audio, "test.mp3")
