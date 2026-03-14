#54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 
import string


message = [54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]
alphabet = list(string.ascii_uppercase)
digits = [0,1,2,3,4,5,6,7,8,9]
#print(alphabet)
decrypted = ['']*len(message)
i=0
 #Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase),
# 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message}
for x in message:
	
	y = x % 37 
	print(y)
	decrypted[0]=alphabet[17]
	if y < 26:
		decrypted[i]=alphabet[y]

	if y >= 26 and y <= 35:
		decrypted[i]=digits[y%26]	
	if y == 36:	
		decrypted[i]='_'

	i+=1


print("\n")
print(decrypted)
	#i=i+1	

