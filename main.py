# importing required modules
import PyPDF3
import csv

header = ['Matricule', 'Heures de présence']

with open('ExtractPaieNov23.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # creating a pdf file object
    pdfFileObj = open('11.PDF', 'rb')

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
        index = object.find("Rubriques")
        # print(object)
        lish_m = []
        list_h_a = []
        j = 0
        #if (i % 2 == 0):
        a = ['0','0']
        b = ['0','0']
        c = ['0','0']
        d = ['0','0']
        e = ['0','0']
        f = ['0','0']
        g = ['0','0']
        lish_m = object[index + 10:index + 51].split(" ")
        print(lish_m)
        print(lish_m[0])
            # 1
        a[j]=lish_m[0]
            # 2
        b[j] = lish_m[1]
            # 3
        c[j] = lish_m[2]
            # 4
        d[j] = lish_m[3]
            # 5
        e[j] = lish_m[4]
            # 6
        f[j] = lish_m[5]
            # 7
        g[j] = lish_m[6]
        #else:
        j+=1
        indexHeureAb = object.find("Total des heures d'absence")
        indexF_H_A = object.find("Absence")
        list_h_a = object[indexHeureAb + 27:indexF_H_A - 1].split(" ")
            # 1
        a[j] = 'P' + str(173-int(list_h_a[0]))
            # 2
        b[j] ='P' + str(173-int(list_h_a[1]))
            # 3
        c[j] ='P' + str(173-int(list_h_a[2]))
            # 4
        d[j] ='P' + str(173-int(list_h_a[3]))
            # 5
        e[j] ='P' + str(173-int(list_h_a[4]))
            # 6
        f[j] ='P' + str(173-int(list_h_a[5]))
            # 7
        g[j] ='P' + str(173-int(list_h_a[6]))

        writer.writerow(a)
        writer.writerow(b)
        writer.writerow(c)
        writer.writerow(d)
        writer.writerow(e)
        writer.writerow(f)
        writer.writerow(g)

pdfFileObj.close()