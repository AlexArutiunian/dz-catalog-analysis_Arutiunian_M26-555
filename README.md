# Анализ каталога фильмов

Мини-проект первого семестра по программированию на Python.

В проекте используется один основной файл `catalog_analysis.py`. Решение сделано без `pandas` и `numpy`, только средствами Python и модуля `math`.

## Запуск

```bash
uv sync
uv run catalog_analysis.py
```

## Проверка стиля

```bash
uv run ruff check .
```

## Ожидаемый вывод

```bash
uv run catalog_analysis.py
uv run ruff check .

ОТЧеТ ПО КАТАЛОГУ
Средний рейтинг: 7.2
Средний возраст фильмов: 8 лет

Топ-3 фильма:
  "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
  "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
  "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

Фильмов по жанрам:
  drama — 5
  comedy — 3
  sci-fi — 3
  thriller — 3
  action — 2
  mystery — 1

Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller
All checks passed!
```

Python: 3.12.

