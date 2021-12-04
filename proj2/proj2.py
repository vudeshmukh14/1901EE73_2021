from flask import Flask, render_template, request
import os
from fpdf import FPDF
import csv
from datetime import date 
from datetime import datetime

# making required imports

# initialization of Flask object
app = Flask(__name__, template_folder="templates")
# configuring the path where the uploaded folders will be saved
app.config['UPLOAD_FOLDER']='D:\\1901EE73_2021\\proj2'

# class defination for PDFs
class PDF(FPDF):
    # method for generating transcript for given roll number
    def create_transcript(self, roll, dict_roll_names, dict_roll_sem_subcode, dict_roll_subcode_grade, dict_subjects_master):

        self.rect(10.0, 10.0, 400.0, 277.0)  # outer margin

        # the header section
        self.rect(10.0, 10.0, 47, 32)
        self.rect(57.0, 10.0, 306, 32)
        self.rect(363, 10.0, 47, 32)
        self.image(r"preprocessing\logo.png", 11, 11, 45, 30)
        self.image(r"preprocessing\title.jpg", 85, 10.7, 250, 30)
        self.image(r"preprocessing\logo.png", 364, 11, 45, 30)

        # the student information section
        branch={'CS':"Computer Science and Engineering",'EE':"Electrical Engineering","ME":"Mechanical Engineering"}
        roll=roll[0:4]+roll[4:6].upper()+roll[6:]
        name=dict_roll_names[roll].capitalize()
        year='20'+roll[:2]

        self.rect(90, 44, 240, 14)
        
        self.set_xy(95, 44)
        self.set_font('Helvetica', 'B', 12)
        self.cell(15, 8, "Roll No: ", align='L')
        self.set_xy(124, 44)
        self.set_font('Helvetica', '', 12)
        self.cell(15, 8, roll, align='L')

        self.set_xy(176, 44)
        self.set_font('Helvetica','B',12)
        self.cell(15, 8, "Name: ", align='L')
        self.set_xy(192, 44)
        self.set_font('Helvetica','',12)
        self.cell(15, 8, name, align='L')

        self.set_xy(272, 44)
        self.set_font('Helvetica','B',12)
        self.cell(30, 8, "Year of Admission: ", align='L')
        self.set_xy(317, 44)
        self.set_font('Helvetica','',12)
        self.cell(15, 8, year, align='L')

        self.set_xy(95, 51)
        self.set_font('Helvetica','B',12)
        self.cell(15, 8, "Programme: ", align='L')
        self.set_xy(124, 51)
        self.set_font('Helvetica','',12)
        self.cell(30, 8, "Bachelor of Technology", align='L')

        self.set_xy(176, 51)
        self.set_font('Helvetica','B',12)
        self.cell(15, 8, "Course: ", align='L')
        self.set_xy(192, 51)
        self.set_font('Helvetica','',12)
        self.cell(30, 8, branch[roll[4:6]], align='L')

        # defining different coordinates based on the number of semesters
        x=[15, 115, 215, 315] 
        if len(dict_roll_sem_subcode[roll].keys())>8:
            y=[60, 128, 190]
            self.line(10, 127, 410, 127)
            self.line(10, 189, 410, 189)
            self.line(10, 240, 410, 240)
        else :
            y=[60, 148]
            self.line(10, 147, 410, 147)
            self.line(10, 234, 410, 234)
        xi=0
        yi=0

        # varibales for calculations
        total_credits=0
        cpi=0
        grade_equivalent={"AA":10, "AA*":10, "AB":9, "AB*":9, "BB":8, "BB*":8, "BC":7, "BC*":7, "CC":6, "CC*":6, "CD":5, "CD*":5, "DD":4, "DD*":4, "F":0, "F*":0, "I":0, "I*":0}
        # iterating for each semester
        for sem in dict_roll_sem_subcode[roll]:

            spi=0
            sem_credits=0
            cleared_credits=0

            # semester number
            head="Semester "+sem
            self.set_xy(x[xi%4], y[yi])
            self.set_font("Helvetica", 'BU', 8)
            self.cell(17, 5, head)
            self.ln()

            # table column headings
            self.set_x(x[xi%4])
            self.set_font("Helvetica", "", 8)
            self.cell(17, 5, "Sub. Code", border=1, align="C")
            self.cell(44, 5, "Subject Name", border=1, align="C")
            self.cell(11, 5, "L-T-P", border=1, align="C")
            self.cell(9, 5, "CRD", border=1, align="C")
            self.cell(9, 5, "GRD", border=1, align="C")
            self.ln()

            # table rows
            for subcode in dict_roll_sem_subcode[roll][sem]:
                self.set_x(x[xi%4])
                self.set_font("Helvetica", "", 8)
                self.cell(17, 5, subcode, border=1, align='C')
                self.set_font("Helvetica", "", 6)
                self.cell(44, 5, dict_subjects_master[subcode][0], border=1, align='C')
                self.set_font("Helvetica", "", 8)
                self.cell(11, 5, dict_subjects_master[subcode][1], border=1, align='C')
                self.cell(9, 5, dict_subjects_master[subcode][2], border=1, align='C')
                self.cell(9, 5, dict_roll_subcode_grade[roll][subcode], border=1, align='C')
                if(float(grade_equivalent[dict_roll_subcode_grade[roll][subcode].strip()])>0):
                    cleared_credits+=float(dict_subjects_master[subcode][2])
                sem_credits+=float(dict_subjects_master[subcode][2])
                spi+=float(grade_equivalent[dict_roll_subcode_grade[roll][subcode].strip()])*float(dict_subjects_master[subcode][2])
                self.ln()
            
            # required calculations
            total_credits+=sem_credits
            cpi+=spi

            # table summary
            self.ln()
            self.set_x(x[xi%4])
            self.set_font("Helvetica", "", 8)
            self.cell(90, 5, f"Credits Taken: {sem_credits}   Credits Cleared: {cleared_credits}  SPI: {round(spi/sem_credits, 2)}   CPI: {round(cpi/total_credits, 2)}", border=1, align='C')
            
            # updates for loop
            xi+=1
            if(xi%4==0) :
                yi+=1

        # footer section
        self.set_xy(15, 260)
        self.set_font("Helvetica", "B", 13)
        today=date.today()
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        self.cell(15, 8, 'Date of issue:  '+today.strftime("%d %b %Y")+", "+current_time)
        self.line(340, 263, 405, 263)
        self.set_xy(340, 265)
        self.set_font("Helvetica", '', 13)
        self.cell(15, 8, 'Assistant Registrar (Academic)')
        if(os.path.isfile(r'preprocessing\seal.jpg')):
            self.image(r'preprocessing\seal.jpg', 200, 245, 40, 40)
        if(os.path.isfile(r'preprocessing\sign.jpg')):
            self.image(r'preprocessing\sign.jpg', 340, 245, 15, 15)


@app.route("/")
def transcript_generator():
    return render_template("index.html")

@app.route('/upload', methods = ['POST', 'GET'])  # for uploading all the files and saving it
def upload():
    if request.method == 'POST':
        f = request.files['File']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], os.path.join("preprocessing", f.filename)))
        return render_template("upload.html", message="File saved successfully, you can go back :)")

@app.route('/', methods=['POST'])    # for taking input of range of roll numbers
def input_range():
    text1 = request.form['text1']
    text2 = request.form['text2']
    processed_text1 = text1.upper()
    processed_text2 = text2.upper()
    f=open("preprocessing\\start.txt", "w")
    f.write(processed_text1)
    f.close()
    f=open("preprocessing\\end.txt", "w")
    f.write(processed_text2)
    f.close()
    return "Input taken, you can go back :)"

def generate_transcript_all():   # for generating transcript for all roll numbers

    # crreating the transcripts folder if it does not exist
    if os.path.exists("transcriptsIITP")==False:
        os.mkdir("transcriptsIITP")

    dict_roll_names={}  # {roll: names}
    dict_roll_sem_subcode={} # {roll: {sem: [subcode, ]}}
    dict_roll_subcode_grade={} # {roll: {subcode: grade}}
    dict_subjects_master={} # {subcode: [subname, ltp, crd]}

    # if the files have not been uploaded then throwing error
    if os.path.exists("preprocessing\\names-roll.csv")==False:
        return render_template("forward.html", message="Please upload 'names-roll.csv' file")
    if os.path.exists("preprocessing\\grades.csv")==False:
        return render_template("forward.html", message="Please upload 'grades.csv' file")
    if os.path.exists("preprocessing\\subjects_master.csv")==False:
        return render_template("forward.html", message="Please upload 'subjects_master.csv' file")

    # creating dictionaries from files for fast and easy access
    with open("preprocessing\\names-roll.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            dict_roll_names[row[0]]=row[1]

    with open("preprocessing\\grades.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0] in dict_roll_sem_subcode.keys():
                if row[1] in dict_roll_sem_subcode[row[0]].keys():
                    dict_roll_sem_subcode[row[0]][row[1]].append(row[2])
                else :
                    dict_roll_sem_subcode[row[0]][row[1]]=[row[2]]
            else :
                dict_roll_sem_subcode[row[0]]={row[1]:[row[2]]}
            if row[0] in dict_roll_subcode_grade.keys():
                dict_roll_subcode_grade[row[0]][row[2]]=row[4]
            else :
                dict_roll_subcode_grade[row[0]]={row[2]:row[4].strip()}

    with open("preprocessing\\subjects_master.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            dict_subjects_master[row[0]]=[row[1], row[2], row[3]]

    # for every roll number creating the pdf and then saving it in transcriptsIITP folder
    for roll in dict_roll_names:
        if roll=="Roll":
            continue
        pdf=PDF(orientation="L", unit="mm", format="A3")
        pdf.set_auto_page_break(False, 0)
        pdf.add_page()
        pdf.create_transcript(roll, dict_roll_names, dict_roll_sem_subcode, dict_roll_subcode_grade, dict_subjects_master)
        pdf.output(os.path.join("transcriptsIITP", str(roll)+".pdf"),'F')

    return render_template("forward.html", message="Transcripts generated successfully, you can go back :)")


def generate_transcript_range():   # for generating transcripts for a range

    # crreating the transcripts folder if it does not exist
    if os.path.exists("transcriptsIITP")==False:
        os.mkdir("transcriptsIITP")

    # if the button is pressed without giving a range
    if os.path.exists("preprocessing\\start.txt")==False:
        return render_template("forward.html", message="Please give starting range")
    if os.path.exists("preprocessing\\end.txt")==False:
        return render_template("forward.html", message="Please give end range")

    
    with open("preprocessing\\start.txt", "r") as file:
        line=file.readline()
        start=line.strip()
    with open("preprocessing\\end.txt", "r") as file:
        line=file.readline()
        end=line.strip()

    if start=="":
        return render_template("forward.html", message="Please give starting range")
    elif end=="":
        return render_template("forward.html", message="Please give end range")

    # if the files have not been uploaded then throwing error
    if os.path.exists("preprocessing\\names-roll.csv")==False:
        return render_template("forward.html", message="Please upload 'names-roll.csv' file")
    if os.path.exists("preprocessing\\grades.csv")==False:
        return render_template("forward.html", message="Please upload 'grades.csv' file")
    if os.path.exists("preprocessing\\subjects_master.csv")==False:
        return render_template("forward.html", message="Please upload 'subjects_master.csv' file")
    
    dict_roll_names={}  # {roll: names}
    dict_roll_sem_subcode={}  # {roll: {sem: [subcode, ]}}
    dict_roll_subcode_grade={}  # {roll: {subcode: grade}}
    dict_subjects_master={}  # {subcode: [subname, ltp, crd]}

    # creating dictionaries from files for fast and easy access
    with open("preprocessing\\names-roll.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            dict_roll_names[row[0]]=row[1]

    with open("preprocessing\\grades.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0] in dict_roll_sem_subcode.keys():
                if row[1] in dict_roll_sem_subcode[row[0]].keys():
                    dict_roll_sem_subcode[row[0]][row[1]].append(row[2])
                else :
                    dict_roll_sem_subcode[row[0]][row[1]]=[row[2]]
            else :
                dict_roll_sem_subcode[row[0]]={row[1]:[row[2]]}
            if row[0] in dict_roll_subcode_grade.keys():
                dict_roll_subcode_grade[row[0]][row[2]]=row[4]
            else :
                dict_roll_subcode_grade[row[0]]={row[2]:row[4].strip()}

    with open("preprocessing\\subjects_master.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            dict_subjects_master[row[0]]=[row[1], row[2], row[3]]

    non_existing=[]  # list of roll numbers that donot exist from given range

    # if range has different braches in start and end, ex. 0401C01-0401ME60
    if (start[:6]!=end[:6]):
        return render_template("forward.html", message="Please specify range in the same branch, you can go back :)")

    
    # iterating over the given range
    for number in range(int(start[6:]), int(end[6:])+1):

        # if roll number exists then creating a transcript for it
        if (start[:6]+str(number).zfill(2)) in dict_roll_names.keys():
            roll_no=start[:6]+str(number).zfill(2)
            pdf=PDF(orientation="L", unit="mm", format="A3")
            pdf.set_auto_page_break(False, 0)
            pdf.add_page()
            pdf.create_transcript(roll_no, dict_roll_names, dict_roll_sem_subcode, dict_roll_subcode_grade, dict_subjects_master)
            pdf.output(os.path.join("transcriptsIITP", str(roll_no)+".pdf"),'F')
        else:
            non_existing.append(start[:6]+str(number).zfill(2))

    if (len(non_existing)!=0):
        return render_template("forward.html", message="Transcripts generated, you can go back :)", ls=non_existing, mess="These roll numbers do no exist")
    return render_template("forward.html", message="Transcripts generated, you can go back :)", ls=non_existing)


@app.route("/forward", methods=['POST'])   # action performed on clicking buttons
def button_clicks():
    if request.method == 'POST':
        if request.form['submit_button'] == 'all':
            return generate_transcript_all()
        elif request.form['submit_button'] == 'range':
            return generate_transcript_range()
        elif request.form['submit_button'] == 'sealed':
            f=open("preprocessing\\sealed.txt", "w")
            f.write("1")
            f.close()
            return render_template("forward.html", message="Input taken, you can go back :)")
        elif request.form['submit_button'] == 'signed':
            f=open("preprocessing\\signed.txt", "w")
            f.write("1")
            f.close()
            return render_template("forward.html", message="Input taken, you can go back :)")

if __name__=="__main__":
    app.run(debug=True)




