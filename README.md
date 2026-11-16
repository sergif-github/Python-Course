# Курс Python

Добро пожаловать на курс Python! Этот бесплатный репозиторий содержит полный курс программирования на Python для начинающих.
Курс поможет вам освоить Python или развить уже имеющиеся навыки программирования.

**Приятного обучения и удачи в программировании!**


## Содержание
- [О Python](#о-python)
- [С чего начать](#с-чего-начать)
- [Обзор курса](#обзор-курса)
- [Структура курса](#структура-курса)


## О Python

Python — универсальный и широко распространённый язык программирования с синтаксисом, близким к естественному языку. Благодаря этому его легко изучать и использовать как начинающим, так и опытным разработчикам. Python применяют в разных отраслях для веб-разработки, создания настольных приложений, системного администрирования и разработки библиотек машинного обучения. Он особенно популярен среди специалистов по анализу данных и машинному обучению.

Python — высокоуровневый интерпретируемый язык программирования, который работает на разных платформах. Гвидо ван Россум начал его разработку в 1989 году. С тех пор Python стал распространённым инструментом для самых разных задач: разработки веб-приложений, настольных программ, средств анализа данных, систем искусственного интеллекта и сценариев автоматизации. Этому способствуют простой и читаемый синтаксис, обширная экосистема библиотек и множество учебных ресурсов.

Для выполнения исходного кода Python нужен интерпретатор. Он читает, разбирает и выполняет код. В таких языках, как C и C++, компилятор заранее преобразует исходный код в машинный. Интерпретатор Python позволяет сразу запускать код и экспериментировать с ним. Выполнение интерпретируемого кода часто медленнее, а безопасность зависит от реализации и способа использования. В состав Python входит стандартный интерпретатор.

Код Python можно запускать из командной строки. Многие интегрированные среды разработки (IDE) используют стандартный интерпретатор. Такие инструменты, как IPython и Jupyter, предоставляют расширенные возможности интерактивной работы. К популярным средам относятся PyCharm, Spyder, Eclipse с расширением PyDev, Visual Studio Code и Jupyter Notebook. Среди известных библиотек экосистемы Python — NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, Keras и PyTorch.

## С чего начать

Для работы с курсом можно установить Python и использовать JupyterLab или IDE на своём компьютере. Можно также работать в Google Colab без локальной установки. Оба варианта подходят для написания и запуска кода, а также для совместной работы.

Если Python уже установлен и вы предпочитаете работать локально, выберите JupyterLab или IDE. Если вы хотите работать в браузере, воспользуйтесь Google Colab.

Выберите вариант, который вам удобнее. Инструкции и примеры курса подходят для обеих сред.

Когда среда будет готова, можно приступать к обучению.


### Установка Python для JupyterLab и IDE

Для работы в IDE или JupyterLab на своём компьютере нужно установить Python.
Он требуется для запуска JupyterLab и выполнения кода.

Порядок установки:

1. Проверьте, установлен ли Python, командой ```python --version```.
    Если Python установлен, команда выведет его версию. В противном случае перейдите к следующему шагу.

2. Установите Python.
    Откройте официальный сайт [python.org](https://www.python.org/). Выберите установщик для вашей операционной системы (Windows, macOS или Linux) и следуйте инструкциям.

    Если установщик предлагает добавить Python в системную переменную `PATH`, включите эту опцию. Так Python можно будет запускать из командной строки или терминала.


### Выбор интегрированной среды разработки (IDE)

Если вы предпочитаете работать в IDE, рассмотрите следующие варианты.
Интегрированные среды предоставляют автодополнение кода, отладчик и средства управления проектами. Поэтому ими пользуются как начинающие, так и опытные разработчики.

- **Visual Studio Code (VS Code)**

    Visual Studio Code, или VS Code, — редактор исходного кода с открытым исходным кодом, разработанный Microsoft.
    Он поддерживает множество расширений и имеет активное сообщество. Есть расширения для разработки на Python.

    Установите VS Code с официального сайта (https://code.visualstudio.com/).


- **PyCharm**

    PyCharm — профессиональная IDE для Python от JetBrains. В неё входят автодополнение кода, отладчик и средства поддержки различных фреймворков.

    Скачайте и установите PyCharm Community Edition (бесплатную) или PyCharm Professional Edition (коммерческую) с сайта JetBrains (https://www.jetbrains.com/pycharm/).


- **Atom**

    Atom — настраиваемый текстовый редактор, созданный GitHub. Пакеты и темы позволяли менять его возможности и внешний вид.

    В исходном курсе указана ссылка на сайт Atom (https://atom.io/).

Это лишь несколько примеров сред для работы с Python. У каждой свои возможности и свой порядок работы, поэтому можно попробовать разные варианты и выбрать подходящий.

IDE упрощает разработку на Python и предоставляет дополнительные инструменты редактирования кода. Для работы с файлами `.ipynb` из этого курса могут потребоваться расширения. Можно также выбрать JupyterLab или Google Colab.

- **JupyterLab**

    JupyterLab — интерактивная среда, в которой можно создавать и запускать ноутбуки Jupyter, работать с кодом и файлами Markdown.

    Чтобы установить JupyterLab, выполните команду ```pip install jupyterlab``` и дождитесь завершения установки.

    Чтобы запустить JupyterLab, выполните команду ```jupyter lab```. Среда откроется в браузере по умолчанию.

- **Google Colab (без установки)**

    Если вы хотите обойтись без установки, можно воспользоваться Google Colab. Эта облачная среда позволяет создавать и запускать ноутбуки Jupyter и работать над ними вместе с другими пользователями.
    В Google Colab уже установлены Python и популярные библиотеки для анализа данных, включая NumPy и Pandas. Код можно писать и выполнять прямо в ячейках ноутбука.

    Чтобы начать работу в Google Colab:

    1. Откройте сайт Google Colab в любом браузере.
    2. Нажмите «Новый ноутбук» (`New Notebook`), чтобы создать пустой ноутбук, или выберите один из готовых шаблонов.


### Форматы файлов курса

Основной формат курса — ноутбуки Jupyter (`.ipynb`). В них представлены примеры кода, упражнения и шаблоны проектов.

Файлы `.ipynb` можно открывать и запускать в JupyterLab, Jupyter Notebook и других совместимых средах. В интерактивном интерфейсе можно выполнять ячейки с кодом, менять код, добавлять заметки и просматривать результаты.

В ноутбуках код, пояснения и визуализации находятся в одном месте. Это помогает понять новые понятия и сразу применять их на практике.


## Обзор курса

Курс знакомит с основами программирования на Python. Темы расположены от базовых к более сложным.

Основные темы курса:
- Введение в Python
- Переменные и базовые типы данных
- Основные операторы
- Инструкции управления потоком выполнения
- Циклы
- Методы и функции
- Объектно-ориентированное программирование (ООП)
- Обработка исключений
- Модули и пакеты
- Работа с файлами
- Дополнительные модули и библиотеки Python
- Продвинутые темы
- Тестирование и отладка

Каждая тема опирается на материал предыдущих разделов. В каждом разделе есть теория, практические примеры и упражнения для закрепления материала.

Цель курса — освоить основы программирования на Python с упором на написание сценариев, базовую обработку данных и организацию программ. К концу курса студенты смогут самостоятельно писать полезные программы, а также читать и изменять код Python, написанный коллегами.


## Структура курса

Курс состоит из модулей, каждый из которых посвящён отдельной теме.

Начните с первого модуля и проходите курс в удобном темпе. Читайте пояснения, запускайте примеры и выполняйте упражнения, чтобы закрепить изученное.

Содержимое репозитория:

**[Модуль 0. Введение в Python](./00-Introduction_to_Python/)**
- [Введение в Python](./00-Introduction_to_Python/01_introduction_python.ipynb)
- [Запуск программ на Python](./00-Introduction_to_Python/02_running_python_programs.ipynb)
- [Основы синтаксиса и отступы](./00-Introduction_to_Python/03_basic_syntax_and_identation.ipynb)
- [Вывод данных и комментарии в коде](./00-Introduction_to_Python/04_printing_and_commenting_code.ipynb)
- [Пользовательский ввод](./00-Introduction_to_Python/05_user_input.ipynb)
- [Упражнения](./00-Introduction_to_Python/06_exercises.ipynb)
- [Решения](./00-Introduction_to_Python/07_solutions.ipynb)

**[Модуль 1. Переменные и типы данных](./01-Variables_and_data_types/)**
- [Переменные и присваивание](./01-Variables_and_data_types/01_variables_and_assignments.ipynb)
- [Числовые типы данных (int, float)](./01-Variables_and_data_types/02_numeric_data_types.ipynb)
- [Строки и работа с ними](./01-Variables_and_data_types/03_string_and_manipulation.ipynb)
- [Логический тип данных](./01-Variables_and_data_types/04_boolean_data_types.ipynb)
- [Преобразование и приведение типов](./01-Variables_and_data_types/05_type_conversion_and_casting.ipynb)
- [Работа с коллекциями (списки, кортежи, множества, словари)](./01-Variables_and_data_types/06_collections.ipynb)
- [Упражнения](./01-Variables_and_data_types/07_exercisies.ipynb)
- [Решения](./01-Variables_and_data_types/08_solutions.ipynb)

**[Модуль 2. Операторы](./02-Operators)**
- [Арифметические операторы](02-Operators/01_arithmetic_operators.ipynb)
- [Операторы сравнения](02-Operators/02_comparison_operators.ipynb)
- [Логические операторы](02-Operators/03_logical_operators.ipynb)
- [Операторы присваивания](02-Operators/04_assignment_operators.ipynb)
- [Побитовые операторы](02-Operators/05_bitwise_operators.ipynb)
- [Приоритет операторов](02-Operators/06_operator_precedence.ipynb)
- [Упражнения](./02-Operators/07_exercises.ipynb)
- [Решения](./02-Operators/08_solutions.ipynb)

**[Модуль 3. Управление потоком выполнения](./03-Control_flow_statements/)**
- [Условные инструкции (if, else, elif)](./03-Control_flow_statements/01_conditional_statements.ipynb)
- [Вложенные условные инструкции](./03-Control_flow_statements/02_nested_conditionals.ipynb)
- [Логические операторы в условиях](./03-Control_flow_statements/03_logical_operators_in_conditionals.ipynb)
- [Условное выражение (тернарный оператор)](./03-Control_flow_statements/04_the_therany_operator.ipynb)
- [Упражнения](./03-Control_flow_statements/05_exercises.ipynb)
- [Решения](./03-Control_flow_statements/06_solutions.ipynb)

**[Модуль 4. Циклы](./04-Loops)**
- [Цикл while](04-Loops/01_while_loop.ipynb)
- [Цикл for](04-Loops/02_for_loop.ipynb)
- [Инструкции управления циклом (break, continue)](04-Loops/03_loop_control_statements.ipynb)
- [Вложенные циклы](04-Loops/04_nested_loops.ipynb)
- [Перебор коллекций](04-Loops/05_looping_collections.ipynb)
- [Упражнения](./04-Loops/06_exercises.ipynb)
- [Решения](./04-Loops/07_solutions.ipynb)

**[Модуль 5. Методы и функции](./05-Methods_and_functions/)**
- [Определение и вызов функций](./05-Methods_and_functions/01_define_and_call_functions.ipynb)
- [Область видимости переменных и ключевое слово global](./05-Methods_and_functions/02_scope_and_global_keyword.ipynb)
- [Функции высшего порядка](./05-Methods_and_functions/03_high_order_functions.ipynb)
- [Лямбда-функции](./05-Methods_and_functions/04_lambda_functions.ipynb)
- [Упражнения](./05-Methods_and_functions/05_exercises.ipynb)
- [Решения](./05-Methods_and_functions/06_solutions.ipynb)
- [Проект «Оценки»](./05-Methods_and_functions/07_milestone_project_grade.ipynb)
- [Решение проекта «Оценки»](./05-Methods_and_functions/08_milestone_project_grade_solution.ipynb)
- [Проект «Калькулятор»](./05-Methods_and_functions/09_milestone_project_calculator.ipynb)
- [Решение проекта «Калькулятор»](./05-Methods_and_functions/10_milestone_project_calculator_solution.ipynb)

**[Модуль 6. Объектно-ориентированное программирование](./06-Object_oriented_programming/)**
- [Введение в ООП](./06-Object_oriented_programming/01_introduction_to_OOP.ipynb)
- [Классы и объекты](./06-Object_oriented_programming/02_classes_and_objects.ipynb)
- [Инкапсуляция и абстракция](./06-Object_oriented_programming/03_encapsulation_and_abstraction.ipynb)
- [Наследование](./06-Object_oriented_programming/04_inheritance.ipynb)
- [Полиморфизм](./06-Object_oriented_programming/05_polymorphism.ipynb)
- [Упражнения](./06-Object_oriented_programming/06_exercises.ipynb)
- [Решения](./06-Object_oriented_programming/07_solutions.ipynb)
- [Проект «Банк»](./06-Object_oriented_programming/08_milestone_project_bank.ipynb)
- [Решение проекта «Банк»](./06-Object_oriented_programming/09_milestone_project_bank_solution.ipynb)

**[Модуль 7. Обработка исключений](./07-Exception_handling/)**
- [Обработка распространённых ошибок](./07-Exception_handling/01_handling_common_errors.ipynb)
- [Что такое исключения](./07-Exception_handling/02_understanding_exceptions.ipynb)
- [Обработка исключений с помощью блоков try-except](./07-Exception_handling/03_handling_exceptions_using_try-except_block.ipynb)
- [Возбуждение исключений](./07-Exception_handling/04_raising_exceptions.ipynb)
- [Упражнения](./07-Exception_handling/05_exercises.ipynb)
- [Решения](./07-Exception_handling/06_solutions.ipynb)

**[Модуль 8. Модули, пакеты и библиотеки](./08-Modules_packages_and_libraries/)**
- [Импорт и использование модулей](./08-Modules_packages_and_libraries/01_importing_and_using_modules.ipynb)
- [Создание и организация пакетов](./08-Modules_packages_and_libraries/02_creating_and_organizing_packages.ipynb)

**[Модуль 9. Работа с файлами](./09-File_manipulation/)**
- [Чтение и запись текстовых файлов](./09-File_manipulation/01_reading_and_writing_files.ipynb)
- [Работа с файловыми объектами](./09-File_manipulation/02_working_with_file_objects.ipynb)
- [Режимы открытия и пути к файлам](./09-File_manipulation/03_file_modes_and_paths.ipynb)
- [Обработка файлов CSV и JSON](./09-File_manipulation/04_csv_and_json_files.ipynb)
- [Обработка ошибок при работе с файлами](./09-File_manipulation/05_error_handling_with_files.ipynb)
- [Упражнения](./09-File_manipulation/06_exercises.ipynb)
- [Решения](./09-File_manipulation/07_solutions.ipynb)

**[Модуль 10. Дополнительные модули Python](./10-Additional_Python_modules/)**
- [Работа с датой и временем (модуль datetime)](./10-Additional_Python_modules/01_datetime_module.ipynb)
- [Математические операции (модуль math)](./10-Additional_Python_modules/02_math_module.ipynb)
- [Генерация случайных чисел (модуль random)](./10-Additional_Python_modules/03_random_module.ipynb)
- [Работа с изображениями (библиотека Pillow)](./10-Additional_Python_modules/04_pillow_module.ipynb)
- [Работа с ZIP-архивами (модуль zipfile)](./10-Additional_Python_modules/05_zipfile_module.ipynb)
- [Регулярные выражения (модуль re)](./10-Additional_Python_modules/06_re_module.ipynb)
- [Сериализация объектов (модуль pickle)](./10-Additional_Python_modules/07_pickle_module.ipynb)
- [Упражнения](./10-Additional_Python_modules/08_exercises.ipynb)
- [Решения](./10-Additional_Python_modules/09_solutions.ipynb)
- [Проект «Интернет-магазин»](./10-Additional_Python_modules/10_milestone_project_store.ipynb)
- [Решение проекта «Интернет-магазин»](./10-Additional_Python_modules/11_milestone_project_store_solution.ipynb)

**[Модуль 11. Продвинутые темы](./11-Advanced_concepts/)**
- [Декораторы функций и классов](./11-Advanced_concepts/01_decorators.ipynb)
- [Итераторы и генераторы](./11-Advanced_concepts/02_iterators_and_generators.ipynb)
- [Рекурсия](./11-Advanced_concepts/03_recursion.ipynb)
- [Отладка](./11-Advanced_concepts/04_debugging.ipynb)
- [Измерение времени выполнения и оптимизация кода](./11-Advanced_concepts/05_code_timming_and_optimization.ipynb)
- [Упражнения](./11-Advanced_concepts/06_exercises.ipynb)
- [Решения](./11-Advanced_concepts/07_solutions.ipynb)

**[Модуль 12. Тестирование и отладка](./12-Testing_and_debugging/)**
- [Модульное тестирование с unittest](./12-Testing_and_debugging/01_unitest_module.ipynb)
- [Разработка через тестирование](./12-Testing_and_debugging/02_test_driven_development.ipynb)
- [Приёмы и стратегии отладки](./12-Testing_and_debugging/03_debugging_techniques_and_strategies.ipynb)
