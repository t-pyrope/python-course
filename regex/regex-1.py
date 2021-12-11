import re
import os

# 1. Nahrazeni v textu
list_original = ["Agalma elegans", "Frillagalma vityazi", "Cordagalma tottoni"]
list__modified = []
for phrase in list_original:
	new_phrase = re.sub(r'(\w)(\w+) (\w+)', r'\1. \3', phrase)
	list__modified.append(new_phrase)
print(list__modified)
