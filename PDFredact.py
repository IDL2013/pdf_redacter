import fitz
import re

# import pdf for redaction
file_link = input("Enter link to file:")
file_name = input("Enter filename (including .pdf)")
loc = file_link + "/" + file_name
print("Full location is: " + loc)
lines = open(loc)


