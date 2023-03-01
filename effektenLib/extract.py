# importing required modules
from PyPDF2 import PdfReader
import re



def getPdfTxt(fileIn):
  
  # creating a pdf reader object
  reader = PdfReader(fileIn)

  text = ""
  for page in reader.pages:
  # extracting text from page
    text += page.extract_text()
    
  return text

def getRecomTxt(pdfText):

  startKeyword = "Börsenfavoriten"
  parts = pdfText.split(startKeyword)
  if len(parts) != 2:
    raise ValueError

  endKeyword = "Haltepositionen"
  favText = parts[1].split(endKeyword)

  return(favText[0])

def getRecommendations(recomText):

    isinCountryLength = 2
    nsinLength = 9
    isinPattern = r"[A-Z]{" + str(isinCountryLength) + r"}[A-Z0-9]{" + str(nsinLength) + r"}[0-9]"

    return re.findall(isinPattern, recomText)

def getRecommendations(fileIn):
  try:
    pdfText = getPdfTxt(fileIn)
    recomText = getRecomTxt(pdfText)
    recommendations = getRecommendations(recomText)
    return recommendations
  except Exception as e:
    print(type(e))
    print(e.args)  
    