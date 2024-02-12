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
            file_dicts.append({"name": file , 'rank' :  random.randint(1, 3) , 'span' :random.choice(lis) })
    return file_dicts





css_file = 'template.css'  # Replace 'styles.css' with your CSS file path
css_dict = parse_css_file(css_file)
print(css_dict)


# css_dict['#_3']['background-color'] = 'red'


folder_path = 'images' # Specify the folder path
images = get_files_in_folder(folder_path)
print(images)



# print(len(images))

# delete = 9 - len(images)



i=1
total_rank = 0

for image in images:

    total_rank = total_rank + image['rank']
    print(total_rank)
    if(total_rank >=6):
        break

    set_background_image( f'#_{i}', image['name'] )

    css_dict[f'#_{i}']['grid-'+ image['span']] = 'span ' + str(image['rank'])   #Trying to assign this: grid-column: span 2;

    i = i+1
   

# print(total_rank)

# New logic

grid = [[000],[000],[000]]















output_file = 'page.css'  # Specify the output file path
write_css_file(css_dict, output_file)