import PyPDF2
pdfReader = PyPDF2.PDFFileReader(open('oop.pdf', 'rb'))
import pyttsx3
speaker = pyttsx3.init()
for page in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

engine.save_to_file(text,'audio.mp3')
engine.runAndWait()