from elevenlabs import save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key = "sk_ea2b5e1804860e9e320e5b4a70b423e84dcea9da0ac6e233",
)

audio = client.generate(
    text = "Hi, this is a test",
    voice = "Rachel",
    model = "eleven_multilingual_v2"
)

save(audio, "test.mp3")