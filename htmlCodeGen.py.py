

def write_html_file(string):
    html_file=open(file_name, mode = "a")
    html_string=string
    html_file.write(html_string)
    html_file.close()



def init(fileName):
    file_name=fileName
    html_file=open(file_name, mode = "w")
    html_file.close()
    return file_name


class html:
    
    def init(self,file_name="test_report.html"):
        html_string="<!DOCTYPE html>\n<html>\n"
        write_html_file(html_string)
     

    def end(self):
         
         html_string="</html>\n"
         write_html_file(html_string)
        
       
    class head:
        def init():
            html_string="<head>\n"
            write_html_file(html_string)

        def title(title_name):
            html_string="<title>"+title_name+"</title>\n"
            write_html_file(html_string)

        def end():
            html_string="</head>\n"
            write_html_file(html_string)


    class body:
        def init():
            string = "<body>\n"
            write_html_file(string)
            
        def end():
            string = "<body>\n"
            write_html_file(string)

        def heading(headingStyle, heading):
            string="<h"+str(headingStyle)+">"+heading+"</h"+str(headingStyle)+">\n"
            write_html_file(string)

        def paragrah(text):
            string = text.replace('\n' , '<br />')
            string = '<p>'+string+'</p>'
            write_html_file(string)

        def addLine():
            string = '<hr />\n'
            write_html_file(string)

        

        class table:
            def init():
                string = "<table width = 25% >\n"
                write_html_file(string)

            def addHeader(elements):
                len_elements = len(elements)
                string = "<tr align =\"left\">\n"
                write_html_file(string)
                for i in range(0,len_elements):
                    string="<th>"+elements[i]+"</th>\n"
                    write_html_file(string)
                string = "</tr>\n"
                write_html_file(string)

                
            def addElements(elements):
                len_elements = len(elements)
                string = "<tr>\n"
                write_html_file(string)
                for i in range(0,len_elements):
                    string="<td>"+elements[i]+"</td>\n"
                    write_html_file(string)
                string = "</tr>\n"
                write_html_file(string)
        
            
                




file_name=init("TestReport.html")    
page=html()
page.init()
page.head.init()
page.head.title("Title")
page.head.end()
page.body.init()
for i in range(1,6):
    page.body.heading(i,"H"+str(i))
page.body.paragrah("hi hello \n how are you")
page.body.addLine()
page.body.table.init()
page.body.table.addHeader(['T1', 't3', 't5', 't10'])
page.body.table.addElements(['T3', 't3', 't5', 't10'])

page.body.end()






page.end()


            
            


