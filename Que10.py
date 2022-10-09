text = "X-DSPAM-Confidence:    0.8475"
finder=text.find("0")
value=text[finder:finder+6]
print(float(value))
