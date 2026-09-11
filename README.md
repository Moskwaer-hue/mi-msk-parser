
# MI.MSK Parser

Система автоматизации карточек товаров для магазина mi.msk.ru.

## Цель

Получать прайс поставщика, находить информацию о товаре, собирать характеристики и фото, генерировать описание и SEO, создавать карточку в InSales.

## Структура

- src/parser/ — основной код
- src/parser/models.py — модели данных
- src/parser/normalizer.py — разбор названий товаров
- src/parser/pipeline.py — сквозной прогон
- src/parser/suppliers/ — адаптеры поставщиков
- src/parser/enrichment/ — поиск и обогащение данных через ИИ
- src/parser/insales/ — клиент InSales API
- src/parser/storage/ — база данных
- scripts/run_demo.py — демонстрационный запуск
- tests/test_normalizer.py — тесты

## Установка

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Запуск демо

    python3 scripts/run_demo.py

## Тесты

    python3 -m pytest tests/

## Статус

Ранний. Ядро нормализации названий. Дальше — адаптеры поставщиков, обогащение, InSales.