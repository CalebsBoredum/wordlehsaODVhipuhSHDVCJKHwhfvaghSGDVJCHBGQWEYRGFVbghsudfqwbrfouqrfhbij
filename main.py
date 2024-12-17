import random

score=0
score1=[]
LettersU=[]

f=open("fiveLettersNoPlurals.txt")
words=[]
word1=f.readlines()
for i in word1:
		i=i.strip()
		words.append(i)


def word2letterL(FIWord):
		FLettersU=FIWord.split()
		return FLettersU

W2LD={}
for i in words:
		a = [ch for ch in i]
		W2LD[i]=a


#fella


IWord=input("starting word seperate letters with spaces ")
LettersU=word2letterL(IWord)



unuse=[]
use=[]
word=["zz","zz","zz","zz","zz"]
wrong=[]
while (score != 100):
		scoreI= input("score ")
		score1=scoreI.split()
		for i in range(0,len(score1)):
				score1[i]=int(score1[i])
		score=sum(score1)
		if score==100:
				print("you win")
				break
		c=-1

		

		T={}
		for i in score1:
				c+=1
			
				if i==0:
						unuse.append(LettersU[c])

				if i==1:
						use.append(LettersU[c])
						for j in W2LD:

								if j.count(LettersU[c])>0 and j[c]!=LettersU[c]:
										#print (j)
										#print(LettersU[c])
										#print(wrong)
										if j not in wrong:											
											T[j]=W2LD[j]
											
								else:
										wrong.append(j)
				

				if i==20:
						word[c]=LettersU[c]
						use.append(LettersU[c])
						for j in W2LD:
								#print (j.count(LettersU[c]))
								if j.count(LettersU[c])>0 and j[c]==LettersU[c]:
										T[j]=W2LD[j]


				#print (T)
		if score!=0:
			W2LD=T.copy()
		#print (W2LD)
		for i in wrong:
			if i in W2LD:
				del W2LD[i]

		if len(W2LD)==1:
				print(W2LD)
				score=100
				break
			
		g=True

		for q in use:
				#print(q)
				if unuse.count(q)>0:
						for m in range (0,unuse.count(q)):
								unuse.remove(q)
		print(unuse)
		print(use)

		while g:
			x=True
			y=True
			GK = random.choice(list(W2LD.keys()))
			#print (GK)
			GN = W2LD[GK]
			LettersU=GN
			#guess=W2LD[GN]
			#print (str(GN))
			#print(W2LD[GN])
			#if set(GN)
	
			for check in unuse:
				#print (check)
				if GN.count(check)!=0:
					x=False
	
			for check2 in use:
				#print (check2)
				if GN.count(check2)==0:
					x=False
					#print (check2)
					#print(GN)
			for c in range(0,4):
				if GN[c]!=word[c] and word[c]!="zz":
					x=False
					#print (GN)
			
			if x:
				print (word)
				print (GK)
				print (len(W2LD))
				LettersU=GN
				del W2LD[GK]
				g=False

			else:
				del W2LD[GK]

							
			
			

'''
		for i in W2LD:
			x=False

			for check in unuse:
				#print (check)
				if i.count(check)!=0:
					#print(i)
					del W2LD[i]
					break


			#if x==True:
				else:
					for check2 in use:
						#print (check2)
						if i.count(check2)==0:
							del W2LD[i]
							print (i)
		#print (W2LD)
'''
