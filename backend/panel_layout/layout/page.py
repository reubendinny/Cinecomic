import os
import random
import copy


def parse_css_file(css_file):
    css_dict = {}
    current_selector = None

    with open(css_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('/*'):
                continue
            if line.endswith('{'):
                current_selector = line[:-1].strip()
                css_dict[current_selector] = {}
            elif line.endswith('}'):
                current_selector = None
            else:
                property_name, value = line.split(':', 1)
                property_name = property_name.strip()
                value = value.strip().rstrip(';')
                if current_selector:
                    css_dict[current_selector][property_name] = value

    return css_dict


def write_css_file(css_dict, output_file):
    with open(output_file, 'w') as f:
        for selector, properties in css_dict.items():
            f.write(f"{selector} {{\n")
            for property_name, value in properties.items():
                f.write(f"    {property_name}: {value};\n")
            f.write("}\n")


def set_background_image(key, image_path, page_template):  
    url_str =   f'url("../../../../frames/final/{image_path}.png");'
    page_template[key]['background-image'] =  url_str



# Function to calculate Hamming distance  
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


templates = ['14124114','312341' , '4432111' , '21411241' , '324114' , '13411141' , '12411131' ,'132113', '131423' , 
'142344' , '234241','2411413','3141214','42111131']


css_file = 'backend/panel_layout/layout/template.css'  # Replace 'styles.css' with your CSS file path
css_dict = parse_css_file(css_file)
print(css_dict)


folder_path = 'frames/final' # Specify the folder path


count = 0

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

        # print(result)
        # print(min(result))
        # print(templates[result.index(min(result))])

        page_templates.append(templates[result.index(min(result))])

        start = start + len(templates[result.index(min(result))]) 


        # print("****************")

    return page_templates





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


def insert_in_grid(page_templates):
    page_css = []

    images = get_files_in_folder(folder_path)
    print(images)
    count_images = 1

    for page_template in page_templates:
        new = copy.deepcopy(css_dict)
        count = 1
        for i in page_template:
            # print(i)

            set_background_image(f'#_{count}', f'frame{count_images:03d}' ,new)

            new[f'#_{count}']['grid-'+ template_specs[i]['direction']] = 'span ' + str(template_specs[i]['span'])   #Trying to assign this: grid-column: span 2;
            # print(new[f'#_{count}']['grid-'+ template_specs[i]['direction']])
            # print(f'count: {count}')
            count = count+1
            count_images+=1

        for i in range(count, 13):
                new[f'#_{i}']['display'] = 'none'
        # print(new)
        page_css.append(new)


    for i in range(0,len(page_css)):
    # print(i)
        print(page_css[i])
        output_file = f'backend/panel_layout/layout/page_css/page{i+1}.css'
        write_css_file(page_css[i],output_file)




# print(page_css)
# print(css_dict)




# output_file = 'page.css'  # Specify the output file path
