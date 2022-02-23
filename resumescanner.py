import docx2txt
from tkinter import *
from tkinter import filedialog

def openfile1():
    filepath = filedialog.askopenfilename(initialdir = r"D:\resumeScanner") #gui
    global file1
    file1 = docx2txt.process(filepath)

def openfile2():
    filepath = filedialog.askopenfilename(initialdir = r"D:\resumeScanner") #gui
    global file2
    file2 = docx2txt.process(filepath)

def submit():
    global contents
    contents = [file1,file2]
    from sklearn.feature_extraction.text import CountVectorizer
    cvs = CountVectorizer()
    matrices = cvs.fit_transform(contents)
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_matrices = cosine_similarity(matrices)
    similarities = similarity_matrices[1][0] * 100
    label = Label(text = 'job requirements : ' + str(round(similarities, 2)) + '%') #gui
    label.place(x = 50 , y = 80) #gui

#gui
window = Tk()
window.title('resume scanner')
window.geometry('225x112')
window.iconbitmap(r"D:\resumeScanner\icon.ico")
button1 = Button(window , text = 'resume', command = openfile1, width = 13)
button1.grid(row = 0,column = 0,pady = 10,padx = 5)
button2 = Button(window , text = 'job description', command = openfile2)
button2.grid(row = 0 ,column = 1,pady = 10,padx = 5)
button3 = Button(window , text = 'submit', command = submit, width = 13)
button3.place(x = 62 , y = 50)
window.mainloop()
