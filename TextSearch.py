from os import walk 
from os import path
import re 
import threading 
import time

response = []





def search_text_findall(file_path , keyword):
    global response 
    res = []
    with open(file_path , mode='r' , encoding='utf8' ) as myfile:
        for i , line in enumerate(myfile.readlines()):
            seached_words = re.findall(fr"({keyword})" , line )
            for word in seached_words:
                res.append(tuple((   file_path , str(i+1) )))  
        myfile.close()
        if(len(res) != 0 ):
            response.extend(res)

def search_on_folder(dir_path , file_names , keyword ):
    for file_name in file_names:
        file_path =  f"{dir_path}\{file_name}"
        if path.splitext(file_path)[1] in ['.txt' , '.py' , '.cpp' , '.js' , '.rs'  ]:
            search_text_findall(file_path , keyword)



def search_keyword(dir_path , keyword ):
    if keyword == '' :
        return "Not Found"
    global response 
    response.clear()
    threads = []
    for (dir_path, _ , file_names) in walk(dir_path):
            thread = threading.Thread(target=search_on_folder , args=(dir_path , file_names , keyword ))
            threads.append(thread)
            thread.start()
                

    for thread in threads:
        thread.join()
          
    if len(response) == 0 :
            return "Not Found"
    return response







        


