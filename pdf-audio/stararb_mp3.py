
import pyttsx3,PyPDF2

pdfreader = PyPDF2.PdfFileReader(open('Statistical Arbitrage with Mean-Reverting Overnight Price Gaps on High-Frequency Data of the S&P 500.pdf', 'rb')) # pass in the PDF
speaker = pyttsx3.init()# initiate speaker
    
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
speaker.save_to_file(clean_text, 'Statistical Arbitrage with Mean-Reverting Overnight Price Gaps on High-Frequency Data of the S&P 500.mp3')
speaker.runAndWait()

speaker.stop()