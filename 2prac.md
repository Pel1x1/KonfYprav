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
var float: root_version = 1.0; 
set of float: foo_versions = {0.0, 1.0}; 
var float: foo_version; 
var float: left_version; 
var float: right_version; 
set of float: shared_versions = {0.0, 1.0}; 
var float: shared_version; 
set of float: target_versions = {1.0, 2.0}; 
var float: target_version;

% Ограничения
constraint (foo_version == 1.0 -> (target_version == 2.0));
constraint (foo_version == 1.0 -> (left_version == 1.0) /\ (right_version == 1.0));
constraint (left_version == 1.0 -> (shared_version >= 1.0));
constraint (right_version == 1.0 -> (shared_version < 2.0));

% Установите диапазоны для переменных
constraint foo_version in foo_versions;
constraint left_version in 0.0..1.0;
constraint right_version in 0.0..1.0;
constraint shared_version in shared_versions;
constraint target_version in target_versions;

solve satisfy;
```
![image](https://github.com/user-attachments/assets/423f9588-1ed8-4950-bd4a-a9e27f9b5f89)

