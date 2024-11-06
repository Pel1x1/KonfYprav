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

def get_commits(repo_path):
    result = subprocess.run(
        ['git', '-C', repo_path, 'log', '--pretty=format:%H'],
        stdout=subprocess.PIPE,
        text=True
    )
    commits = result.stdout.splitlines()
    return commits

def generate_plantuml_code(commits):
    lines = ["@startuml", "digraph G {"]
    for i in range(len(commits) - 1):
        lines.append(f'  "{commits[i]}" -> "{commits[i+1]}"')
    lines.append("}")  
    lines.append("@enduml")
    return "\n".join(lines)

def write_output(output_path, content):
    with open(output_path, 'w') as f:
        f.write(content)

def main(config_path):
    config = read_config(config_path)
    commits = get_commits(config['repo_path'])
    plantuml_code = generate_plantuml_code(commits)
    print(plantuml_code)
    write_output(config['output_path'], plantuml_code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Напишите: py hw2.py <config_path>")
        sys.exit(1)
    main(sys.argv[1])