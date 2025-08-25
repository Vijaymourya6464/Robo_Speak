import win32com.client as wincom
if __name__ == '__main__':
    print("Welcome to Window speaking system 1.1 Created by Vijay Mourya")
    speaker = wincom.Dispatch("SAPI.SpVoice")

    while True:
        x = input("Enter what you want to speak (type 'exit' to quit): ")
        if x.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        speaker.Speak(x)