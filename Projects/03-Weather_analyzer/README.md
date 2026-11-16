# Проект 3. Анализатор погодных данных

Проект объединит объектно-ориентированное программирование, исключения, модули, CSV и JSON, статистику, получение данных через API и построение графиков.

## Организация папки анализатора погодных данных

В начале проекта структура минимальна:

```text
Projects/
└── 03-Weather_analyzer/
    ├── README.md
    └── weather_analyzer.py
```

После изучения ООП, исключений и файлов:

```text
Projects/
└── 03-Weather_analyzer/
    ├── README.md
    ├── main.py
    ├── models.py
    ├── loaders.py
    ├── statistics.py
    └── data/
        └── sample_weather.csv
```

Финальная версия:

```text
Projects/
└── 03-Weather_analyzer/
    ├── README.md
    ├── main.py
    ├── models.py
    ├── loaders.py
    ├── statistics.py
    ├── api.py
    ├── charts.py
    ├── reports.py
    ├── data/
    │   └── sample_weather.csv
    └── tests/
        ├── test_loaders.py
        ├── test_models.py
        └── test_statistics.py
```

Структура усложняется вместе со знаниями студентов. Папки и модули появляются тогда, когда они изучены.
