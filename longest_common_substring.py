words = input().split()

def is_common_substring(sub):
	counter = 0
	for word in words:
		if sub in word:
			counter += 1			
	if counter == len(words):
		return True
	else:
		return False

lcs = ""
for i in range(len(words[0])):
	for j in range(i+1,len(words[0])+1):
		sub = words[0][i:j]
		if is_common_substring(sub):
			if len(sub) > len(lcs):
				lcs = sub

print(lcs)
