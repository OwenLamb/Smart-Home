Heres the thought process

Smart home UI is ran by home assistant found here on a raspberry pi 4b:
    UI and easy to use app for users
    Connects all my microcontrollers and smart appliances all in one app

Old gaming PC runs AI models and other tasks
    AI:
        LLM for generating response text
        LLM for processing commands to send to the home assistant server
        STT for receiving a .wav file from the raspberry pi endpoints via HTTP
        TTS for generating a new .wav file to play on the raspberry pi via HTTP

    Security Camera:
        I think its called tail scale? Not sure what the software it is but it just handles recordings from camera and deleting old footage etc.

    Cloudfare server? - I want to use home assistant on my phone outside of the network. To do that I need some outside server hosted. Not sure how to do that yet

Raspberry pi zero to use as microphone and speakers throughout the house
    AI:
        Custom Wake up model that waits for a keyword source: https://github.com/dscripka/openWakeWord

    Then just uses the microphone to record data to a .wav file to send to the server
    I plan to use MQTT to handle states since I'd like to have multiple PI's running
    Something like
        topic: house/office/endpoint_status
        payload: INPUT, RESPONSE, SLEEP
            where:
            SLEEP = sleep state where PI is only listening for wakeup word and models on server shouldn't be running or in a sleep state
            INPUT = this is set after the pi has uploaded .wav file for the server to grab data for STT
            RESPONSE = this is set after the server has uploaded a .wav file for the PI to play over the speaker
