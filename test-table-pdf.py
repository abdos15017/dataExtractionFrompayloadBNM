
# importing required modules
import PyPDF3
import csv

header = ['Matricule', 'Heures de présence']

with open('ExtractPaieJan23.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # creating a pdf file object
    pdfFileObj = open('jan23.PDF', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF3.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    totalPage = pdfReader.numPages
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    # extracting text from page
    for i in range(0, totalPage - 1):
        object = ''
        object += pdfReader.getPage(i).extractText() + "\n"
        # print(object)
        object = " ".join(object.replace(u"\xa0", " ").strip().split())
        data = ['','','','']
        if(object.find("*** Net congés ***")==-1):
            # Matricule
            index = object.find("Salarié")
            listh_m = object[index + 10:index + 15].split(" ")
            data[0] = listh_m[0],
            #Heures présences
            index_h_p = object.find("Heures de présences")
            list_h_p = object[index_h_p + 19:index_h_p + 23].split(" ")
            data[1]=list_h_p[1]
            #Net à payer
            index_n_p = object.find("Net à payer")
            list_n_p = object[index_n_p + 11:index_n_p + 17].split(" ")
            data[2]= list_n_p[1]
            #Cout Total
            index_c_t = object.find("Coût total")
            list_c_t = object[index_c_t + 10:index_c_t + 16].split(" ")
            data[3] = list_c_t[1]
            writer.writerow(data)



pdfFileObj.close()
