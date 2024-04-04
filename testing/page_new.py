import os
import random
import copy

class panel:
    def __init__(self,image,row_span,col_span):
       self.image = image
       self.row_span = row_span
       self.col_span = col_span



template_specs = {
    "1" : {
        "span" : 1,
        "direction": "row"
    },
    "2" : {
        "span" : 2,
        "direction": "row"
    },
    "3" : {
        "span" : 3,
        "direction": "column"
    },
     "4" : {
        "span" : 2,
        "direction": "column"
    }
      
}

input = '443333333343333333343434344333333334344433433'



def hammingDist(str1, str2): 
    i = 0
    count = 0
  
    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count

def get_files_in_folder(folder_path):
    file_dicts = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            rank = random.randint(1, 3) 

            file_dicts.append({"name": file , 'rank' :  rank})
    return file_dicts

templates = ['14124114','312341' , '4432111' , '21411241' , '3241141' , '13411141' , '12411131' ,'1321113', '131423' , 
'142344' , '234241','2411413','3141214','42111131']

min_length = 6
folder_path = 'frames/final' # Specify the folder path



def get_templates(input):
    page_templates = []
    start = 0

    while(start<len(input)):
        # print(f"start: {start}")
        result = []
        print(input)
        for template in templates:

            temp = input[start:start + len(template)]
            print(f"start: {start} len:{len(template)} temp:{temp}" )
            result.append(hammingDist(temp,template))            

       
        page_templates.append(templates[result.index(min(result))])

        start = start + len(templates[result.index(min(result))]) 



    if(len(temp) < min_length):
        if(len(temp) ==1):
          temp="5"
        elif(len(temp) ==2):
          temp="67"
        elif(len(temp) ==3):
          temp="666"
        elif(len(temp) ==4):
          temp="4488"
        elif(len(temp) ==5):
          temp="44446"

        page_templates[len(page_templates)-1] = temp
        # print("****************")

    return page_templates



def page_create(page_templates):

    pages = []

    images = get_files_in_folder(folder_path)
    print(images)
    count_images = 1

    for page_template in page_templates:
        count = 1
        try:
            for i in page_template:

                if(template_specs[i]['direction'] == 'row'):
                    new = panel(f'frame{count_images:03d}',template_specs[i]['span'] , 1)
                else:
                    new = panel(f'frame{count_images:03d}', 1 ,template_specs[i]['span'])
                pages.append(new)
                print(new.__dict__)
                count = count+1
                count_images+=1
        except:
           continue
        
    
    return(new)


v = get_templates(input)
page_create(v)
print(page_create(v))

