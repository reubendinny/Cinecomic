from backend.class_def import Page,panel,bubble
import json

def page_create(page_templates,panels,bubbles):
    count = 0
    pages = []
    for page_template in page_templates:

        new_page = Page(panels[count:count+len(page_template)],bubbles[count:count+len(page_template)])
        pages.append(new_page)
        count = count +len(page_template)
        print(new_page.__dict__)        

    return pages


def page_json(pages):
    pages_dict = []

    for page in pages:
        pages_dict.append(page.__dict__)

    with open('page.js', 'w') as f:
        f.write(f'var pages = ')
        json.dump(pages_dict, f , indent=4)