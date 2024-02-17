import os
import random


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


def set_background_image(key, image_path):  
    url_str =   f'url("images/{image_path}");'
    css_dict[key]['background-image'] =  url_str

lis = ['row' , 'column']

def get_files_in_folder(folder_path):
    file_dicts = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            span = random.choice(lis)
            if(span == 'row'):
                rank = random.randint(1, 4) 
            else:
                rank = random.randint(1, 3) 

            file_dicts.append({"name": file , 'rank' :  rank, 'span' :span})
    return file_dicts





css_file = 'template.css'  # Replace 'styles.css' with your CSS file path
css_dict = parse_css_file(css_file)
print(css_dict)


# css_dict['#_3']['background-color'] = 'red'


folder_path = 'images' # Specify the folder path
images = get_files_in_folder(folder_path)
print(images)




i=1
total_rank = 0



print(css_dict)

# New logic














output_file = 'page.css'  # Specify the output file path
write_css_file(css_dict, output_file)