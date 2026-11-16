# Проект 1. Калькулятор

Калькулятор — первый компактный проект курса. Он объединяет пользовательский ввод, арифметические операции, условные конструкции, циклы и функции.

## Задание

Полное условие находится в ноутбуке [«Проект „Калькулятор“»](../../05-Methods_and_functions/09_milestone_project_calculator.ipynb).

Реализуйте функции в файле [`calculator.py`](./calculator.py), затем запустите программу:

```bash
python3 Projects/01-Calculator/calculator.py
```

Для базовой самопроверки выполните:

```bash
python3 Projects/01-Calculator/check_calculator.py
```

Эталонное решение приведено в ноутбуке [«Решение проекта „Калькулятор“»](../../05-Methods_and_functions/10_milestone_project_calculator_solution.ipynb).

## Организация папки калькулятора

В начале курса структура минимальна:

```text
Projects/
└── 01-Calculator/
    ├── README.md
    └── calculator.py
```

После изучения функций появляются отдельная точка запуска и открытые проверки:

```text
Projects/
└── 01-Calculator/
    ├── README.md
    ├── main.py
    ├── operations.py
    └── check_calculator.py
```

Финальная версия после изучения тестирования:

```text
Projects/
└── 01-Calculator/
    ├── README.md
    ├── main.py
    ├── calculator/
    │   ├── __init__.py
    │   ├── operations.py
    │   └── cli.py
    └── tests/
        ├── test_operations.py
        └── test_cli.py
```

Структура усложняется вместе со знаниями студентов. Новые файлы и модули появляются после изучения соответствующих тем.
