# passwords = [
#   "1-3 a: aabcde",
#   "1-3 b: cdefg",
#   "2-9 c: cccccccccasas"
# ]


f = open("day2.txt")
content = f.readlines()
print(content)
f.close()

correct_ones = 0
passwords=[]

for item in content: 
    passwords.append(item)



for password in passwords:
  components = password.split(" ")
  

  actual_password = components[2]
  character = components[1][0]
  
  condition_num = components[0].split("-")
  
  number1 = int(condition_num[0])
  number2 = int(condition_num[1])
  
  count = 0
  
  
  #LOGIC FOR PART 2
  if character == actual_password[number1-1] and character != actual_password[number2-1] or character != actual_password[number1-1] and character == actual_password[number2-1]:
          correct_ones+=1
          
  
  #LOGIC FOR PART 1
  
  # for letter in actual_password:
  #     if character == letter:
  #         count+=1
          
          
  # print("count value",count)
      
  # if count < number1 or count > number2:
  #     print("Password: ",actual_password, "is not a valid one")
  
  # else:
  #     print("Password: ",actual_password, "is a valid one")
  #     correct_ones +=1


  

print("Correct password count is: ",correct_ones)
  
  
