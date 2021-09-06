import os

def output_by_subject(f):
    if os.path.isdir("./output_by_subject")==False:
        os.mkdir("./output_by_subject")
    column_names=f.readline().split(',')
    for rows in f:
        rows=rows.split(',')
        new_heading=column_names[0]+','+column_names[1]+','+column_names[3]+','+column_names[8]
        new_row=rows[0]+','+rows[1]+','+rows[3]+','+rows[8]
        if os.path.exists("output_by_subject/%s.csv"%rows[3])==False:
            new_f=open("output_by_subject/%s.csv"%rows[3], "a")
            new_f.write(new_heading)
            new_f.write(new_row)
            new_f.close()
        else :
            new_f=open("output_by_subject/%s.csv"%rows[3], "a")
            new_f.write(new_row)
            new_f.close()
    return

def output_individual_roll(f):
    if os.path.isdir("output_individual_roll")==False:
        os.mkdir("output_individual_roll")
    column_names=f.readline().split(',')
    for rows in f:
        rows=rows.split(',')
        new_heading=column_names[0]+','+column_names[1]+','+column_names[3]+','+column_names[8]
        new_row=rows[0]+','+rows[1]+','+rows[3]+','+rows[8]
        if os.path.exists("output_individual_roll/%s.csv"%rows[0])==False:
            new_f=open("output_individual_roll/%s.csv"%rows[0], "a")
            new_f.write(new_heading)
            new_f.write(new_row)
            new_f.close()
        else :
            new_f=open("output_individual_roll/%s.csv"%rows[0], "a")
            new_f.write(new_row)
            new_f.close()
    return

f=open("regtable_old.csv", "r")
output_individual_roll(f)
f.close()
f=open("regtable_old.csv", "r")
output_by_subject(f)
f.close()