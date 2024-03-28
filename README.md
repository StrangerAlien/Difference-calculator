### Hexlet tests and linter status:
[![Actions Status](https://github.com/StrangerAlien/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/StrangerAlien/python-project-50/actions)
[![tests](https://github.com/StrangerAlien/python-project-50/actions/workflows/tests.yml/badge.svg)](https://github.com/StrangerAlien/python-project-50/actions/workflows/tests.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e27e483496124fd2498e/maintainability)](https://codeclimate.com/github/StrangerAlien/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e27e483496124fd2498e/test_coverage)](https://codeclimate.com/github/StrangerAlien/python-project-50/test_coverage)

Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов, например, jsondiff. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Возможности утилиты:

- Поддержка разных входных форматов: yaml, json
- Генерация отчета в виде plain text, stylish и json

Пример использования:

```bash
gendiff --format plain filepath1.json filepath2.yml

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

### Dependencies

- python = ">=3.11"
- poetry = ">=1.7.1"
- pip = ">=23.3.2"

### Install

```bash
git clone https://github.com/StrangerAlien/Difference-calculator

cd python-project-50/

make build
make install
make package-install
```

### Сравнение плоских файлов (JSON)
[![asciicast](https://asciinema.org/a/G39xeFtm6yjpt7nfGtkSJ3Uh4.svg)](https://asciinema.org/a/G39xeFtm6yjpt7nfGtkSJ3Uh4)<br>

### Сравнение плоских файлов (YAML)
[![asciicast](https://asciinema.org/a/fU2LFWBKRaLGwC4IL1VVYMomr.svg)](https://asciinema.org/a/fU2LFWBKRaLGwC4IL1VVYMomr)<br>

### Рекурсивное сравнение
[![asciicast](https://asciinema.org/a/wPiO41uTeWzSVrUI3P7AuvzEs.svg)](https://asciinema.org/a/wPiO41uTeWzSVrUI3P7AuvzEs)<br>

### Плоский формат
[![asciicast](https://asciinema.org/a/FrzWB0KL6BbEYJBzOZfJyEC0T.svg)](https://asciinema.org/a/FrzWB0KL6BbEYJBzOZfJyEC0T)<br>

### Вывод в JSON
[![asciicast](https://asciinema.org/a/Fgq1xmMwr7iVx7hyGzmBcFh3T.svg)](https://asciinema.org/a/Fgq1xmMwr7iVx7hyGzmBcFh3T)<br>
