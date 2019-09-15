# Calculations For Tips
import re
import datetime
import random

class NameStuff(object):
        @staticmethod
        def clear_files():
                p = open("total_tips.txt", "r+")
                q = open("tip_scoreboard.txt",'r+')
                p.seek(0)
                q.seek(0)
                p.truncate(0)
                q.truncate(0)
                p.close()
                q.close()
                return
                
        
        @staticmethod
        def calculate_total_tips(string):
                      output = ""
                      ba = ""
                      total=""
                      added_lines= []
                      total_array=[]
                      edited_lines= []
                      existing_lines =[]
                      total_lines =[]
                      amount_recieved = 0.00
                      textfile = open("total_tips.txt", "r")
                      text = textfile.read()
                      textfile.close()
                      total_array = string.split(",")
                      total_array.pop(len(total_array)-1)
                      #removes empty set
                      for x  in range(0,len(total_array)):
                             current_added = total_array[x].strip()
                             #"Xieu recieves $6.8"
                             ba = current_added.split("$")
                             name_recieved = ba[0]
                             #"Xieu recieves "
                             amount_recieved = ba[1]
                             if (re.search(name_recieved,text))==None:
                                     f = name_recieved + "$" +str(amount_recieved)
                                     added_lines.append(f)
                             #"6.8"
                             #Check each line for name recived
                             infile=open("total_tips.txt", "r+")
                             for line in infile:
                               changed = False
                               if(re.search(name_recieved,line.strip()))!=None:
                                      changed = changed or True
                                      #The name is in one of the lines in the file but not in 
                                      ba2 = line.split("$")
                                      current_amount = ba2[1]
                                      current_name = ba2[0]
                                      e = float(current_amount) + float(amount_recieved)
                                      new_amount = round(e,2)
                                      newline = (str(ba[0]) + "$"+ str(new_amount))
                                      edited_lines.append(newline)
                               else:
                                      changed = changed or False
                               
               
                               if (changed==False) and (line.split('$')[0] not in string):
                                   count = 0
                                   for match in line:
                                        if count==0 and (line.strip()) not in existing_lines:
                                          existing_lines.append(line.strip())
                                          count = count+1
                                   
                      infile.seek(0)
                      infile.truncate(0)          
                      total_lines = (edited_lines + existing_lines + added_lines)
                      for x in range(0, len(total_lines)):
                                   output = total_lines[x]
                                   total = total + total_lines[x]+"\n"
                                   if x!=(len(total_lines)-1):
                                          infile.write(output+"\n")
                                   else:
                                          infile.write(output)
                                   
                            
                      infile.close()
                      return total
        @staticmethod
        def capital_name(x):
            #This method takes a name with any case and returns the name with a capital for the first letter.
            my_name = str(x)
            result = ""
            letter_list = []
            new_list = []
            complete = False
            for x in range(0,len(my_name)):
                letter_list.append(my_name[x])
                if x == (len(my_name)-1):
                    first_letter = letter_list.pop(0)
                    first_letter = first_letter.upper()
                    letter_list.insert(0,first_letter)
                    new_list = letter_list
                    x=0
                    for x in range(0,len(my_name)):
                        result = result + new_list[x]
                        if result.lower() == my_name.lower():
                            #^This Just tests to make sure the names are indeed the same.
                            return result
        @staticmethod
        def hours_fulltime(this):
            if this =='F' or this =='f':
                return 8.5
            elif this=='l' or this=='L':
                return 3.5
            else:
                return 5.0   
        @staticmethod
        def round_to(n, precision):
            correction = 0.5 if n >= 0 else -0.5
            return int( n/precision+correction ) * precision
        @staticmethod
        def add_to_quickselect(user_name,score_value,end_text):
             file = open("tip_scoreboard.txt",'r+')
             name_list = []
             score_list = []
             score_value_list = []
             basetext ="Quick Select Enter Number To Select Name >> Sorted by Max Tips Recived<<\n"
             final_line = ""
             if end_text == "":
                 removed=0
             else:
                 removed=len(end_text)
             score_value = score_value+end_text
             name_list.append(user_name)
             score_list.append(score_value)
             mscore_value = float(score_value[:-removed])
             score_value_list.append(mscore_value)
             content = file.read()
             #step 1: reading and parsing the data of the allready existing file STATUS: Working / Modifyable reads the existing leaderboard as a text. Tried readlines()
             # but was getting a glitch where it read lines downward instead of accross.
             file.seek(0)
             file.truncate(0)
             #step 2: clears the text file
             #the input for a line looks like this (pos). Bryan Nelson : 9.087%\n
             these_lines = content.split('\n')
             #splits by line ^
             for x in range(1,len(these_lines)):
                 eachline = str(these_lines[x])
                 components = eachline.split(':')
                 #step 3: breaking up the input string.
             # This line returns (num).\tFirstname\tLastname\t
             # Also returns \t18.76%. splits it by ':' returns both sides for al values
                 for y in range(0,len(components)):
                     #This uses components instead of 2 which is the value of len(components)
                     # Map if y!=0 - \t18.76% if y=1 (num).\tFirstname\tLastname\t
                           if y!=0:
                              score = (components[y]).strip()
                              mscore_value = float(score[:-removed])
                              #score = 18.76%
                           else:
                               #pos wil be recalculated every time so this split removes the position
                             namewit_pos = (components[y])
                             name = (namewit_pos.split('.')[1])
                             # name = \tFirstname\tLastname\t
                             name = str(name).strip()
                             # name = Firstname\tLastname - The first name and last name is already computed by the regular code below.

                 #This compares number values to tell if the score should be added replacing the other dict value :)
                 if name in name_list :
                     x = name_list.index(name)
                     new_score = score_value_list[x]
                     if mscore_value <= new_score:
                        name_list.remove(name)
                        y = score_list.pop(x)
                        z = score_value_list.pop(x)
                        score_list.append(y)
                        score_value_list.append(z)
                        name_list.append(name)
                     else:
                         name_list.append(name)
                         score_list.append(score)
                         score_value_list.append(mscore_value)
                         
                 else:
                     name_list.append(name)
                     score_list.append(score)
                     score_value_list.append(mscore_value)
                 #This adds the score and name to a list.
             #This part of the function returns the score and name by line on iteration compiled to a list which must be mapped and sorted
             position_collection=dict(zip(name_list,score_list))
             #step 4: creation of a dictionary from the name_list and score_list and sorting it by value
             sorted_position = sorted(position_collection.items(), key=lambda kv: float(kv[1][:-removed]), reverse=True)
             #This is the part of the code found on stack overflow it orders the dictionary by the key value I do not fully understand this code but it is causing issues.
             # I got it from here  - https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
             for z in range(0,len(sorted_position)):
                 this_tuple=tuple(sorted_position[z])
                 pos = z+1
              # This takes the position from the amount of tuples returned. Notice the cast to tuple. What was returned was an array I think? containing all of the tuples
              # When tuple = 0 it is the Name 1 is the score
                 if z!=len(sorted_position)-1:
                    #step 5: taking the tuples name and score and adding them to final_line the finished product that will be outputed.
                     final_line = final_line + str(pos)+". "+str(this_tuple[0])+" : "+str(this_tuple[1])+"\n"
                 else:
                     final_line = final_line + str(pos)+". "+str(this_tuple[0])+" : "+str(this_tuple[1])

             result = basetext.lstrip()+final_line
             result = result.lstrip()
             #step 6: the basetext is the ==leaderboard== then the ordered position final lines are dropped in
             file.write(result)
             #step 7: the result is writen to the leaderboard text and updated it is then outputed as the return of the method.
             file.close()
             return
            #The problem with this is that the sorting method does not take into account the position of decimals is there any other methods I could use to sort the Dict
            #or instead sort an list of tuples. Dict also does not allow for repeats as you cannot input your name twice.
        @staticmethod
        def show_quickselect():
                file = open("tip_scoreboard.txt",'r')
                content = file.read()
                these_lines = content.split('\n')
                print("Quick Select Enter Number To Select Name >> Sorted by Max Tips Recived<<")
                for z in range(1,len(these_lines)):
                        print(these_lines[z])
                file.close()
                return
        @staticmethod
        def pull_name(num):
                file = open("tip_scoreboard.txt",'r')
                content = file.read()
                these_lines = content.split('\n')
                eachline = str(these_lines[num])
                components = eachline.split(':')
                for v in range(0,len(components)):
                        namewit_pos = (components[v])
                        name = (namewit_pos.split('.')[1])
                        name = str(name).strip()
                        if name not in name_array:
                                name_array.append(name)
                        else:
                              employee_name = str(input("Enter Employee Firstname >> ")).strip()
                              employee_name = NameStuff.capital_name(employee_name)
                              if NameStuff.lookfor_int(employee_name)==True:
                                      employee_name = NameStuff.pull_name(int(employee_name))
                                      if employee_name not in name_list:
                                              name_list.append(employee_name)
                                      return;
                                
                        
                        file.close()
                        return name
        @staticmethod
        def lookfor_int(name):
         try:
                name = int(name)
                return True
         except:
                return False
                
              
def Name_body():        
        print("////////////////////////////////////////////////////////////////////////")
        print(" Calculations for Tips: Done By Orion")
        print("////////////////////////////////////////////////////////////////////////")
        a = True
        total_tips_slave =""
        new_given = 0.00
        total = 0
        name_array= []
        total_hours = 0
        name_list = []
        hours_list = []
        final_list = []
        number_of_employees=0
        while a == True:
            try:
                tips_amount = float(input("What was the number of tips for the day in $ >> "))
                number_of_employees =  int(input("Enter the number of employees >> "))
                if number_of_employees !=0:
                        a=False

                NameStuff.show_quickselect()
                for x in range (0, number_of_employees):
                    employee_name = str(input("Enter Employee Firstname >> ")).strip()
                    employee_name = NameStuff.capital_name(employee_name)
                    if NameStuff.lookfor_int(employee_name)==True:
                            employee_name = NameStuff.pull_name(int(employee_name))
                    if employee_name not in name_list:
                            name_list.append(employee_name)
                    hours_worked =input("What is the number of hours that the employee has worked f= full day h = half day l = lunch >> ").strip()
                    try:
                        eval_worked = eval(hours_worked)
                    except:
                            pass
                    if hours_worked == 'F' or hours_worked == 'f':
                        hours_worked = NameStuff.hours_fulltime(str(hours_worked))
                        #print(hours_worked)
                        hours_list.append(hours_worked)
                        total_hours = float(total_hours) + hours_worked
                        #print(total_hours)
                    elif hours_worked == 'h' or hours_worked == 'H':
                        hours_worked = NameStuff.hours_fulltime(str(hours_worked))
                        #print(hours_worked)
                        hours_list.append(hours_worked)
                        #print(hours_list)
                        total_hours = float(total_hours) + hours_worked
                    elif hours_worked == 'l' or hours_worked == 'L':
                        hours_worked = NameStuff.hours_fulltime(str(hours_worked))
                        #print(hours_worked)
                        hours_list.append(hours_worked)
                        #print(hours_list)
                        total_hours = float(total_hours) + hours_worked
                        #print(total_hours)
                    elif type(eval_worked)==float:
                        hours_worked = float(hours_worked)
                        #print(hours_worked)
                        hours_list.append(hours_worked)
                        total_hours = total_hours + hours_worked
                        #print(total_hours)
                    elif type(eval_worked)==int:
                        hours_worked = float(str(hours_worked)+".00")
                        #print(hours_worked)
                        hours_list.append(hours_worked)
                        total_hours = total_hours + hours_worked
                        #print(total_hours)
                    else:
                        print("Error: Please enter a propper value")
                        continue
                        
                        
                        
            except Exception as e:
                print(e)
        for x in range (0, (number_of_employees)):
                #print(total_hours)
                #print(tips_amount)
                c = round((hours_list[x]/total_hours)*tips_amount,2)
                amount_given = NameStuff.round_to(c,0.05)
                total = float(total) + float(amount_given)
                NameStuff.add_to_quickselect(str(name_list[x]),str(round(amount_given,2)),"$ in Tips.")
                output = (str(name_list[x])+ " recieves  $" + str(round(amount_given,2)))
                final_list.append(output)
        total = round(total,2)
        if total != tips_amount:
                #print(tips_amount)
                #print(total)
                diffrence = tips_amount-total
                diffrence = round(diffrence,2)
                pos_add_diffrence = random.randint(0,(number_of_employees-1))
                edited = final_list.pop(pos_add_diffrence)
                #print(edited)
                split_array = edited.split("$")
                #>> "Eve recieves  $9.0"
                #split_array[0] = "Eve recives "
                #split_array[1] = "9.00"
                new_given = float(split_array[1]) + diffrence
                d = split_array[0]+"$"+str(round(new_given,2))
                final_list.append(d)
        for y in range(0, (number_of_employees)):
                total_tips_slave = total_tips_slave + final_list[y] + ","
                
                print(final_list[y])
        print("/////////////////////Total Tips Recived General/////////////////")
        print(NameStuff.calculate_total_tips(total_tips_slave))
        endKey = input('Press Any Key To Exit R to restart and C to Clear Lists')
        if (endKey=="R" or endKey=="r"):
                Name_body()
        elif (endKey=="c" or endKey=="C"):
              NameStuff.clear_files()
              Name_body()
                
        else:
                pass
Name_body()
        
        


        
