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


css_file = 'page.css'  # Replace 'styles.css' with your CSS file path
css_dict = parse_css_file(css_file)
print(css_dict)








output_file = 'page.css'  # Specify the output file path
write_css_file(css_dict, output_file)