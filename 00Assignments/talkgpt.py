import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
listener =sr.Recognizer()
openai.api_key = "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"

while True:
    with sr.Microphone() as source:
        print("speak now...")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        model = "text-davinci-003"

        if "exit" in data:
            break

    completion = openai.Completion.create(model ="text-davinci-003",
      prompt = data,
      max_tokens = 1024,
      temperature = 0.5,
      n = 1,
      stop = None)
    response = completion.choices[0].text
    choice = int(input("press 1 to print the response or press 2 to print and hear the response: "))

    if choice == 1:
        print(response)
    else:
        print(response)
        engine.say(response)
        engine.runAndWait()

    repeat = input("do you want to ask more questions?: ")
    if repeat in ["no","No","No"]:
        break