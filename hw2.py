import requests
import sys

class DependencyGraph:
    def __init__(self):
        self.graph = {}

    def add_dependency(self, package, dependency):
        if package not in self.graph:
            self.graph[package] = []
        self.graph[package].append(dependency)

    def to_graphviz(self):
        lines = ['digraph G {']
        for package, dependencies in self.graph.items():
            for dependency in dependencies:
                lines.append(f'    "{package}" -> "{dependency}";')
        lines.append('}')
        return '\n'.join(lines)

    def fetch_dependencies(self, package_name):
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            dependencies = data.get('info', {}).get('requires_dist', [])
            for dep in dependencies:
                dep_name = dep.split(';')[0].strip() 
                self.add_dependency(package_name, dep_name)
        else:
            print(f"Package '{package_name}' not found on PyPI.")

def main(package_name):
    dg = DependencyGraph()
    dg.fetch_dependencies(package_name)
    print(dg.to_graphviz())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dependency_graph.py <package_name>")
        sys.exit(1)

    main(sys.argv[1])
