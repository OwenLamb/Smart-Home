import speech_recognition as sr
import pyttsx3 
 
# Initialize the recognizer 
r = sr.Recognizer() 
 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# template sets up the AI as one big string. As converstation history progresses it will remeber what happened previously
template = """
You are an assistant named Regis which stands for Really Efficient Generative Intelligence System, you have short responses to questions while being sarcastic and throwing insults. Do not put reactions in *'s 

Here is the converstation history: {history}

Input: {input}

"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context = ""

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

def GenerateAI(rawInput):
    global context
    user_input = ("You: " + rawInput)  # Format so AI will know what info came from what source
    result = chain.invoke({"history": context, "input": user_input})
    print(result)
    context += f"\nUser: {user_input}\nAI: {result}"
    return result

     
 
while(1):    
     
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2, phrase_time_limit=15)
            MyText = MyText.lower()

            #Call local AI model
            result = GenerateAI(MyText)
            
            #Call TTS
            SpeakText(result)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")