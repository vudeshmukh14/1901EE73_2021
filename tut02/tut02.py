def get_memory_score(check_list):

    memory_list=[]
    score=0
    for x in check_list:
        if x in memory_list:
            score+=1
        elif x not in memory_list and len(memory_list)>=5:
            del memory_list[0]
            memory_list.append(x)
        elif x not in memory_list and len(memory_list)<5:
            memory_list.append(x)

    return score

input_nums = [3, 4, 5, 3, 2, 1]

invalid=[]
for x in input_nums:
    mystr=str(x)
    if (mystr.isdigit()==False):
        invalid.append(x)
    
if len(invalid)>0:
    print("Please enter a valid input list. Invalid inputs detected:", invalid)
    exit()

print("Score:", get_memory_score(input_nums))