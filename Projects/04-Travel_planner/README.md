# Проект 4. Планировщик путешествий

Итоговый проект объединит маршруты, бюджет, даты, погодные данные и описания мест. В нём будут использованы компоненты текстового и погодного анализаторов.

## Организация папки планировщика путешествий

В начале проекта структура минимальна:

```text
Projects/
└── 04-Travel_planner/
    ├── README.md
    └── travel_planner.py
```

После изучения модулей, файлов и дат:

```text
Projects/
└── 04-Travel_planner/
    ├── README.md
    ├── main.py
    ├── planner.py
    ├── budget.py
    ├── storage.py
    └── data/
        └── sample_trip.json
```

Финальная версия:

```text
Projects/
└── 04-Travel_planner/
    ├── README.md
    ├── main.py
    ├── models.py
    ├── planner.py
    ├── budget.py
    ├── storage.py
    ├── weather_service.py
    ├── text_service.py
    ├── reports.py
    ├── data/
    │   └── sample_trip.json
    └── tests/
        ├── test_budget.py
        ├── test_planner.py
        └── test_storage.py
```

Структура усложняется вместе со знаниями студентов. Папки и модули появляются тогда, когда они изучены.
