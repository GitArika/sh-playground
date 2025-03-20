import os
import shutil

def create_files_from_templates():
    script_path = os.path.dirname(os.path.abspath(__file__))
    templates_path = os.path.join(script_path, 'templates')
    files_to_create = ['eslint.config.js', 'package.json', 'tsconfig.json', '.prettierrc']

    for file_name in files_to_create:
        template_file = os.path.join(templates_path, file_name)
        destination_file = os.path.join(os.getcwd(), file_name)

        if os.path.exists(template_file):
            shutil.copy(template_file, destination_file)
            print(f'{file_name} criado com sucesso.')
        else:
            print(f'Template para {file_name} não encontrado em {template_file}.')

if __name__ == '__main__':
    create_files_from_templates()
