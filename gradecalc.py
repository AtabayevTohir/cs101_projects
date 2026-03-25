def username():
    name = input("What is your name: ")
    return name

def new_user_info():
    assignment = {}
    quiz = {}
    midterm={}
    final ={}
    na,nq=1,1
    condition  = input("Do you want to add information? ")
    while condition == "yes" or condition=="yeah" or condition == "yep":
        if condition=="no":
            break
        type_of_info = input("What type of information do you want to add? \n Assignment,Quiz,Midterm , Final exam : ")
        if type_of_info == "assignment" or type_of_info=="Assignment":
            assignment_grade = input(f"What is your grade in your Assignment-{na}:  ")
            assignment[f"Assignment-{na}"]=assignment_grade
            na+=1
        elif type_of_info == "quiz" or type_of_info=="Quiz":
            quiz_grade = input(f"What is your grade in your {nq}-quiz:  ")
            quiz[f"{nq}-Quiz"]=quiz_grade
            nq+=1
        elif (type_of_info == "midterm" or type_of_info=="Midterm") and midterm.get("Midterm",0)==0:
            midterm_grade = input(f"What is your grade in your Midterm:  ")
            midterm[f"Midterm"]=midterm_grade
            
        elif (type_of_info == "final" or type_of_info=="Final" or type_of_info=="Final exam" or type_of_info == "final exam") and final.get("Final exam",0)==0:
            final_grade = input(f"What is your grade in your Final exam:  ")
            final[f"Final exam"]=final_grade
        else:
            if type_of_info == "midterm" or type_of_info=="Midterm":
                ttt = input(f"You already entered your data for {type_of_info}\n Do you want to change it?  ")
                if ttt == "yes" or ttt=="yeah" or ttt == "yep":
                    midterm_grade = input(f"What is your changed grade in your Midterm then:  ")
                    midterm[f"Midterm"]=midterm_grade
                else:
                    print("okay changing data is stopped")
            elif type_of_info == "final" or type_of_info=="Final" or type_of_info=="Final exam" or type_of_info == "final exam":
                ttt = input(f"You already entered your data for {type_of_info}\n Do you want to change it?  ")
                if ttt == "yes" or ttt=="yeah" or ttt == "yep":
                    final_grade = input(f"What is your changed grade in your Final exam:  ")
                    final[f"Final exam"]=final_grade
                else:
                    print("okay changing data is stopped")
            else:
                print('pls only choose assignment,quiz,nidterm,final !!!')
        condition  = input("Do you want to add information again?  ")
    return assignment,quiz,midterm,final    
    
def weight_calc(asssignment,quiz,midterm,final):
    total_assignment = 0
    total_quiz =0
    weight_avarage_assignment=0
    weight_avarage_quiz =0
    final_weight = 0
    midterm_weight=0
    num_a = 0
    num_q = 0

    for grade in asssignment.values():
        total_assignment += float(grade)
        num_a += 1

    if num_a != 0:
        avarage = total_assignment / num_a
        weight_avarage_assignment = 0.15 * avarage

    for grade_q in quiz.values():
        total_quiz += float(grade_q)
        num_q += 1

    if num_q != 0:
        avarage_quiz = total_quiz / num_q
        weight_avarage_quiz = 0.15 * avarage_quiz

    for grade_m in midterm.values():
        if grade_m ==None:
            grade_m=0
        midterm_weight = float(grade_m)*0.3

    for grade_f in final.values():
        if grade_f==None:
            grade_f=0
        final_weight = float(grade_f)*0.4
    
    
    return weight_avarage_assignment,weight_avarage_quiz,midterm_weight,final_weight,num_a,num_q

def abs(w_a,w_q,w_m,w_f):
    total_weight = w_a+w_q+w_m+w_f
    grade = None
    if total_weight >= 95:
        grade = "A+"
    elif total_weight >=90:
        grade ="A"
    elif total_weight >=85:
        grade ="B+"
    elif total_weight >=80:
        grade = "B"
    elif total_weight >=65:
        grade = "C+"
    elif total_weight>=55:
        grade="C"
    elif total_weight>=40:
        grade="D"
    elif total_weight<40:
        grade="F"
    return grade,total_weight

# def gpa():
    


# def file():
#     name = username()
#     assignment_dict,quiz_dict,midterm_dict,final_dict=new_user_info()
#     weight_a,weight_q,weight_m,weight_f,num_a,num_q = weight_calc(assignment_dict,quiz_dict,midterm_dict,final_dict)
    
#     with open(name,'w') as report:
#         report.write("\nGrade Calculator")
#         report.write("\n-----------------------")
#         for task_a,grade in assignment_dict.items():
#             report.write(f"\nYour {task_a} grade: {grade}   ({float(weight_a/num_a) :.2f}%)")
#         report.write("\n-----------------------")
#         for task_q,grade_q in quiz_dict.items():
#             report.write(f"\nYour {task_q} grade: {grade_q}   ({float(weight_q/num_q) :.2f}%)")
#         report.write("\n-----------------------")
#         for  midterm,grade_m in midterm_dict.items():
#             report.write(f"\nYour {midterm} grade: {grade_m}   ({weight_m :.2f}%)")
#         report.write("\n-----------------------")
#         for  final,grade_f in final_dict.items():
#             report.write(f"\nYour {final} grade: {grade_f}   ({weight_f :.2f}%)")
        # report.write("\n-----------------------")