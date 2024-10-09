# Практическая №2.

# Задание 1
```
-pip install matplotlib
-pip show matplotlib
-pip freeze
-pip install pipdeptree
-!pipdeptree --packages matplotlib
```

![image](https://github.com/user-attachments/assets/dd1951e7-f22b-41c2-9f12-7631bf4946ea)


>Для получения прямо из репозитория:
```
git clone https://github.com/matplotlib/matplotlib.git
```


# Задание 2
```
Перейдти в директорию вашего проекта, где установлен Express
- cd путь/к/проекту
- npm list express
```
![image](https://github.com/user-attachments/assets/0bde7eb8-d73b-40f5-becb-cb102a982480)
```
- npm view express
```
![image](https://github.com/user-attachments/assets/c97fad06-ec86-4682-bb81-123355cafba6)

```
""Как получить пакет без менеджера пакетов, прямо из репозитория?""
```
``` js
const express = require('./path/to/package'); // указать путь к пакету который установлен самостоятельно
const app = express();
```

# Задание 3
``` Graphviz
digraph dependencies {
    rankdir=LR;
    node [shape=box];

    matplotlib [label="matplotlib"];
    numpy [label="numpy"];
    pyparsing [label="pyparsing"];
    python_dateutil [label="python-dateutil"];
    cycler [label="cycler"];
    
    express [label="express"];
    accepts [label="accepts"];
    array_flatten [label="array-flatten"];
    cookie_parser [label="cookie-parser"];
    debug [label="debug"];
    depd [label="depd"];
    finalhandler [label="finalhandler"];
    media_type [label="media-type"];
    methods [label="methods"];
    on_finished [label="on-finished"];
    range_parser [label="range-parser"];
    send [label="send"];
    serve_static [label="serve-static"];

    express -> accepts;
    express -> array_flatten;
    express -> cookie_parser;
    express -> debug;
    express -> depd;
    express -> finalhandler;
    express -> media_type;
    express -> methods;
    express -> on_finished;
    express -> range_parser;
    express -> send;
    express -> serve_static;

    matplotlib -> numpy;
    matplotlib -> pyparsing;
    matplotlib -> python_dateutil;
    matplotlib -> cycler;
}
```
![image](https://github.com/user-attachments/assets/a111d4bf-4398-416e-9009-d29c403bbae9)


# Задание 4
```  minizinc
include "globals.mzn";

array[1..6] of var 0..9: digits;
constraint all_different(digits);

var int: sum_first = sum(digits[1..3]);
var int: sum_last = sum(digits[4..6]);

constraint sum_first = sum_last;
solve minimize sum_first;
```
![image](https://github.com/user-attachments/assets/8ee98a9e-1105-4ff9-9536-b5391f7a711b)


# Задание 5
``` minizinc
set of int: MenuVersion = {100, 110, 120, 130, 150};
set of int: DropdownVersion = {230, 220, 210, 200, 180};
set of int: IconsVersion = {100, 200};

var MenuVersion: menu;
var DropdownVersion: dropdown;
var IconsVersion: icons;

constraint if menu >= 110 then dropdown >= 200 else dropdown = 180 endif;

constraint if dropdown <= 200 /\ dropdown > 180 then icons = 200 else icons = 100 endif;

solve satisfy;
```
![image](https://github.com/user-attachments/assets/74c11b8a-c6ce-4d87-a27c-79958a66bc3c)




# Задание 6
```
var int: root_major = 1; 
var int: root_minor = 0; 
var int: root_patch = 0;

set of int: foo_major = {0, 1}; 
var int: foo_major_version; 
var int: foo_minor_version = 0; 
var int: foo_patch_version = 0;

var int: left_major = 1; 
var int: left_minor = 0; 
var int: left_patch = 0;

var int: right_major = 1; 
var int: right_minor = 0; 
var int: right_patch = 0;

set of int: shared_major = {0, 1}; 
var int: shared_major_version; 
var int: shared_minor_version = 0; 
var int: shared_patch_version = 0;

set of int: target_major = {1, 2}; 
var int: target_major_version; 
var int: target_minor_version = 0; 
var int: target_patch_version = 0;

constraint (foo_major_version == 1 -> (target_major_version == 2));
constraint (foo_major_version == 1 -> (left_major == 1) /\ (right_major == 1));
constraint (left_major == 1 -> (shared_major_version >= 1));
constraint (right_major == 1 -> (shared_major_version < 2));

constraint foo_major_version in foo_major;
constraint left_major in {0, 1};
constraint right_major in {0, 1};
constraint shared_major_version in shared_major;
constraint target_major_version in target_major;

solve satisfy;

output [
    "root version: ", show(root_major), ".", show(root_minor), ".", show(root_patch), "\n",
    "foo version: ", show(foo_major_version), ".", show(foo_minor_version), ".", show(foo_patch_version), "\n",
    "left version: ", show(left_major), ".", show(left_minor), ".", show(left_patch), "\n",
    "right version: ", show(right_major), ".", show(right_minor), ".", show(right_patch), "\n",
    "shared version: ", show(shared_major_version), ".", show(shared_minor_version), ".", show(shared_patch_version), "\n",
    "target version: ", show(target_major_version), ".", show(target_minor_version), ".", show(target_patch_version)
];
```
![image](https://github.com/user-attachments/assets/303c2da7-0715-4250-99b6-d770783eb7cd)

# Задание 7
Для начала установим пакеты
``` bash
pip install matplotlib
pip install subprocess
```
Далее код на Python
``` python
import subprocess

def get_package_info(package_name):
    """Получает информацию о пакете и его зависимостях с помощью pip show."""
    try:
        result = subprocess.run(['pip', 'show', package_name], capture_output=True, text=True)
        if result.returncode != 0:
            return {"error": f"Package '{package_name}' not found."}
        info = {}
        for line in result.stdout.splitlines():
            if line.startswith("Name:"):
                info["name"] = line.split(": ")[1]
            elif line.startswith("Version:"):
                info["version"] = line.split(": ")[1]
            elif line.startswith("Requires:"):
                dependencies = line.split(": ")[1].split(", ") if ": " in line else []
                info["dependencies"] = dependencies
        return info
    except Exception as e:
        return {"error": str(e)}

def print_dependencies(package_info, level=0):
    indent = " " * (level * 4)  
    print(f"{indent}{package_info['name']} ({package_info['version']})")
    
    if package_info["dependencies"]:
        for dep in package_info["dependencies"]:
            dep_info = get_package_info(dep.strip())
            if "error" not in dep_info:
                print_dependencies(dep_info, level + 1)
            else:
                print(f"{indent}    {dep} (not found)")

package_name = "matplotlib"
package_info = get_package_info(package_name)

if "error" in package_info:
    print(package_info["error"])
else:
    print_dependencies(package_info)
    
```
## Результат работы 
![image](https://github.com/user-attachments/assets/c1e6601e-2e2d-4967-9be8-b241969cdf64)




