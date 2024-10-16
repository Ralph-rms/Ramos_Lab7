name = str (input("Enter your name: "))
sec = str (input("Enter your section: "))
prelim = float (input ("Enter your preliminary grade:" ))
midterm = float (input("Enter you midterm grade: "))
final = float (input("Enter your final grade: "))

 
if prelim < 40.0 or prelim > 100.0:
     print ("error: your grade must stay between 40 and 100. ")
elif midterm < 40.0 or midterm > 100.0:
     print ("error: your grade must stay between 40 and 100." )
elif final < 40.0 or final > 100.0:
     print ("error: your grade must stay between 40 and 100. ")

final = (prelim + midterm + final)
     
final_grade=round(final/3)

if final_grade>= 99.0 and final_grade<= 100.0: 
     grade = 1.00 
     status = "excellent"
elif final_grade>= 96.0 and final_grade<= 99.0: 
     grade = 1.25 
     status = "outstanding"
elif final_grade>= 93.0 and final_grade<= 96.0: 
     grade = 1.50
     status = "superior"
elif final_grade>= 90.0 and final_grade<= 93.0: 
     grade = 1.75
     status = "very good"
elif final_grade>= 87.0 and final_grade<= 90.0: 
     grade= 2.00
     status = "good"
elif final_grade>= 84.0 and final_grade<= 87.0: 
     grade= 2.25 
     status= "satisfactory"
elif final_grade>= 81.0 and final_grade<= 84.0: 
     grade= 2.50
     status= "fairly satisfactory"
elif final_grade>= 78.0 and final_grade<= 81.0: 
      grade= 2.75
      status= "fair"
      
elif final_grade>= 75.0 and final_grade<= 75.0: 
      grade= 3.00
      status= "passed"  
else: 
      grade= 5.00
      status= "failed"
      
print(f"final grade: {final_grade:.2f}") 
print(f"status: {status}")
print(f"gpa:",grade)
