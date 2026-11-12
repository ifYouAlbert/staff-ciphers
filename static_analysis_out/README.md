# Вывод статических анализаторов

Нужен для отчета ПР7 (Issue: #3)

## Логи получены:

Из корня:

```bash
uv run mypy src main.py > ./static_analysis_out/mypy.txt
```

```bash
uv run ruff check src main.py --output-format concise --output-file ./static_analysis_out/ruff.txt
```
