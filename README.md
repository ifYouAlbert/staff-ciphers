# Цикл практических работ по CI/CD

## Скриншот работы программы для [ПР 6](https://github.com/ifYouAlbert/staff-ciphers/issues/1)

![img.png](public/example_of_work.png)

## Сохраненные логи для [ПР 7](https://github.com/ifYouAlbert/staff-ciphers/issues/3)

* ./static_analysis_out/
  * [README.md](static_analysis_out/README.md)
  * [mypy.txt](static_analysis_out/mypy.txt)
  * [ruff.txt](static_analysis_out/ruff.txt)

## Установка и запуск

Из корня:

```bash
uv sync
```

Запуск программы:

```bash
uv run main.py
```

## Тесты

Установка:

```bash
uv sync --locked --dev
```

Запуск тестов:

```bash
uv run python -m pytest -v
```

Генерация XML-отчёта:

```bash
uv run python -m pytest --junitxml=test-results/pytest.xml
```

Генерация HTML-отчёта:

```bash
uv run python -m pytest --html=test-results/report.html --self-contained-html
```
