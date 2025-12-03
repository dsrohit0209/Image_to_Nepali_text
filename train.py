import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("nepali_text.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise
gray = cv2.medianBlur(gray, 3)

# Increase sharpness with threshold
thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31, 2
)

# OCR for Nepali
text = pytesseract.image_to_string(thresh, lang="nep")

print("Extracted Nepali Text:")
print(text)

