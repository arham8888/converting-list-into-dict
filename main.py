def test(list):
 result={}
 for item in list:
  result[item[0]]=item[1:]
  return result
students= [ [1,"Hasnain"], [2,"Ahmad"] , [3,"Zaibi"] , [4,"soban"]]

print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))