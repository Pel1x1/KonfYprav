import subprocess
import xml.etree.ElementTree as ET
import os

def read_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()
    config = {
        'visualizer_path': root.find('visualizer_path').text,
        'repo_path': root.find('repo_path').text,
        'output_path': root.find('output_path').text
    }
    return config

def get_commit_tree(repo_path):
    result = subprocess.run(
        ['git', '-C', repo_path, 'log', '--pretty=format:%H %s', '--reverse'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8' 
    )
    
    if result.returncode != 0:
        print("Ошибка при получении коммитов:", result.stderr)
        return {}

    commits = result.stdout.splitlines()
    commit_info = {} #инфа для каждого коммита
    
    for commit in commits:
        hash_value, message = commit.split(' ', 1)
        commit_info[hash_value] = {
            'message': message,
            'children': []
        }

    # информация о дереве файлов для каждого коммита    
    for hash_value in commit_info.keys():
        result = subprocess.run(
            ['git', '-C', repo_path, 'diff-tree', '--no-commit-id', '--name-status', '-r', hash_value],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"Ошибка при получении файлов для коммита {hash_value}:", result.stderr)
            continue
        
        files = result.stdout.splitlines()
        
        for file in files:
            status, filename = file.split('\t')
            commit_info[hash_value]['children'].append((status, filename))
    
    return commit_info

def generate_plantuml_code(commit_info): #создание дерева коммитов
    lines = ["@startuml", "digraph G {"]
    
    commit_nodes = {}
    
    previous_commit = None
    
    for commit_hash, info in commit_info.items():
        short_commit_hash = commit_hash[:7]  #показываем хэш коммита
        commit_node = f'"{info["message"]} ({short_commit_hash})" [shape=box]'
        lines.append(commit_node)
        commit_nodes[commit_hash] = info["message"]

        if previous_commit:
            lines.append(f'  "{previous_commit}" -> "{info["message"]} ({short_commit_hash})"')

        for status, filename in info['children']:
            action_hash = commit_hash[:5]  #показываем хэш действия
            
            if status == 'A':
                action = f'create file {filename} ({action_hash})'
            elif status == 'M':
                action = f'edit file {filename} ({action_hash})'
            elif status == 'D':
                action = f'remove file {filename} ({action_hash})'
            else:
                action = f'unknown action {filename} ({action_hash})'

            file_node = f'"{action}" [shape=ellipse]'
            lines.append(file_node)

            lines.append(f'  "{info["message"]} ({short_commit_hash})" -> "{action}"')

        previous_commit = f"{info['message']} ({short_commit_hash})"

    lines.append("}")  
    lines.append("@enduml")
    
    return "\n".join(lines)
    
def write_output(output_path, content):
    with open(output_path, 'w') as f:
        f.write(content)

def main(config_path):
    config = read_config(config_path)
    commit_info = get_commit_tree(config['repo_path'])
    plantuml_code = generate_plantuml_code(commit_info)
    print(plantuml_code)
    write_output(config['output_path'], plantuml_code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        #print("Напишите: py hw2.py <config_path>")
        sys.argv.append("config.xml")
    main(sys.argv[1])