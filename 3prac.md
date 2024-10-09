# Практическая №3.

# Задание 1
``` jsonnet
local groupTemplate(index) = "ИКБО-" + index + "-20";

local groups = [groupTemplate(i) for i in std.range(1, 24)];

local studentTemplate(name, age, group) = {
  age: age,
  group: group,
  name: name,
};

local students = [
  studentTemplate("Иванов И.И.", 19, "ИКБО-4-20"),
  studentTemplate("Петров П.П.", 18, "ИКБО-5-20"),
  studentTemplate("Сидоров С.С.", 18, "ИКБО-5-20"),
  studentTemplate("Киселев К.С.", 18, "ИКБО-65-23"),
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление",
}
```
``` json
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 18,
      "group": "ИКБО-65-23",
      "name": "Киселев К.С."
    }
  ],
  "subject": "Конфигурационное управление"
}
```
<div width="200" height="200">
<img src="https://github.com/user-attachments/assets/7678b991-cf86-4140-b84c-f88959008774" alt="image" width="50%" height="50%" /><img src="https://github.com/user-attachments/assets/40732681-186f-4027-a516-92dfdae0687b" alt="image" width="50%" height="50%" />
</div>

<br><br>

# Задание 2

```
let Group = List Text

let Student = { age : Natural, group : Text, name : Text }

let groups : Group =
      [ "ИКБО-1-20"
      , "ИКБО-2-20"
      , "ИКБО-3-20"
      , "ИКБО-4-20"
      , "ИКБО-5-20"
      , "ИКБО-6-20"
      , "ИКБО-7-20"
      , "ИКБО-8-20"
      , "ИКБО-9-20"
      , "ИКБО-10-20"
      , "ИКБО-11-20"
      , "ИКБО-12-20"
      , "ИКБО-13-20"
      , "ИКБО-14-20"
      , "ИКБО-15-20"
      , "ИКБО-16-20"
      , "ИКБО-17-20"
      , "ИКБО-18-20"
      , "ИКБО-19-20"
      , "ИКБО-20-20"
      , "ИКБО-21-20"
      , "ИКБО-22-20"
      , "ИКБО-23-20"
      , "ИКБО-24-20"
      ]

let students : List Student =
    [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
    , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
    , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
    , { age = 18, group = "ИКБО-65-23", name = "Киселев К.С." }
    ]

in
  { groups = groups
  , students = students
  , subject = "Конфигурационное управление"
  }
```

```
groups:
  - "ИКБО-1-20"
  - "ИКБО-2-20"
  - "ИКБО-3-20"
  - "ИКБО-4-20"
  - "ИКБО-5-20"
  - "ИКБО-6-20"
  - "ИКБО-7-20"
  - "ИКБО-8-20"
  - "ИКБО-9-20"
  - "ИКБО-10-20"
  - "ИКБО-11-20"
  - "ИКБО-12-20"
  - "ИКБО-13-20"
  - "ИКБО-14-20"
  - "ИКБО-15-20"
  - "ИКБО-16-20"
  - "ИКБО-17-20"
  - "ИКБО-18-20"
  - "ИКБО-19-20"
  - "ИКБО-20-20"
  - "ИКБО-21-20"
  - "ИКБО-22-20"
  - "ИКБО-23-20"
  - "ИКБО-24-20"
students:
  - age: 19
    group: "ИКБО-4-20"
    name: "Иванов И.И."
  - age: 18
    group: "ИКБО-5-20"
    name: "Петров П.П."
  - age: 18
    group: "ИКБО-5-20"
    name: "Сидоров С.С."
  - age: 18
    group: "ИКБО-65-23"
    name: "Киселев К.С."
subject: "Конфигурационное управление"
```

<div width="200" height="200">
<img src="https://github.com/user-attachments/assets/3b483a85-8675-4980-9f9a-b1371efb339d" alt="image" width="50%" height="50%" /><img src="https://github.com/user-attachments/assets/55575c8d-2119-4421-a6bd-c5fdbe0e5c59" alt="image" width="50%" height="50%" />
</div>

# Задание 3 

```
BNF = '''
S = A | B | C | D | E
A = 1 | 1 A | 1 B
B = 0 | 0 B
C = 1 1
D = 1 0 1 1 0 1
E = 0 0 0
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/f1b4b31d-7a7b-4b27-a111-d017e311f50a)

# Задание 4

```
BNF = '''
S = A | B | C
A = ( S ) | { S } | ε
B = ( A ) | { A }
C = ε
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))

```
![image](https://github.com/user-attachments/assets/27bd51eb-2fc3-468b-8fe2-6e6ea9afe851)

# Задание 5

```
BNF = '''
S = E
E = E & T | E | T
T = T | F | ~T | ( E )
F = x | y
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/d5234d99-1a2f-4a5e-b517-9de70e43dc25)

