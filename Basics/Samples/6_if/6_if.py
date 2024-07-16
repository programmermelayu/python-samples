# while mentioning topics say that timeline is in video description
# so you don't need to watch entire video

n=input("(Q1) Enter a number: ")
n=int(n)
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")

	
# Show the execution by debugging
# If is called control statement as it controls the flow of code execution

# go to idle and explain different operators

# ==
# !=
# >
# <
# >=
# <=
#
# 3>2 and 4>1
# 3>1 or 4>8
# not 4==4

print()

# Cousine checker. Explains if..elif..else
indian_foods=["roti canai","tandoori","dal","naan"]
chinese_foods=["kueteow","dim sum","mee tarik"]
malay_foods=["nasi lemak","sate","rojak mi"]

dish=input("(Q2) Enter a dish name: ")

if dish in indian_foods:
    print(f"{dish} is indian cuisine")
elif dish in chinese_foods:
    print(f"{dish} is chinese cuisine")
elif dish in malay_foods:
    print(f"{dish} is malay cuisine")
else:
    print(f"Based on my limited knowledge, I don't know which cuisine is {dish}")
	
print()

# Ternary operator
print("Q3) Ternary operator demo")
n=input("Enter a number:")
n=int(n)
message="Number is even" if n%2==0 else "Number is odd"
print(message)	
