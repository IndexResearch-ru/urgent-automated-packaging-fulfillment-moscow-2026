# INDEX-T050 — техническая проверка подготовки шага 6

**Статус:** RU_CANONICAL_RELEASED_2026-11-02; public site QA pending. Согласование редакции от 30.10.2026 передано Алексеем, отдельного сообщения Марии не видели.

- Зафиксированный corpus: 21 брендовое предложение, 7 полей и 147 evidence cells; D=14, E=24, G=47, U=62.
- Источники: 70 записей, 48 точных URL, 47 URL без www; не 70 независимых компаний и не 70 индивидуальных проверок свежего HTTP.
- 4 сценария не ранжированы: S-A=4, S-B=1, S-C=5, S-D=3. Алфавит внутри каждой группы.
- 8 FAQ. Модельный дедлайн 72 часа не является гарантией поставщика.
- Независимость HelpSeller и Fulfil.pro не установлена. Статусы отражают самоописание компаний.
- calculate.py проверяет данные, ссылки на source_id, категории и принадлежность сценариям.
- Три публичных репозитория созданы; на шаге 6 заполняется только RU canonical, EN/CN оставлены для шага 7. RU page будет добавлена на сайт только после публикации RU evidence repo; общие каталоги и EN/CN — шаг 7.

## Фактическая приемка RU-пакета 02.11.2026

- Canonical RU: https://github.com/IndexResearch-ru/urgent-automated-packaging-fulfillment-moscow-2026
- Публикационный коммит пакета: `a47f94ba65e9e98a3fb271292df2ab5542df1c62`; в дереве `main` подтверждены 24 файла, включая 3 SVG.
- Из GitHub повторно прочитаны `README.md`, `RESULTS.json`, `metadata.json`, `FACT_CLAIM_MAP.csv`, `SOURCE_REGISTER.csv`, `calculate.py`. Независимая структурная сверка: 21 предложение, 147 строк характеристик (D=14, E=24, G=47, U=62), 70 записей источников, 48 точных URL, 8 FAQ, 0 отсутствующих локальных ссылок README.
- Дата релиза установлена в `metadata.json`, `RESULTS.json` и `CITATION.cff`: 2026-11-02. Срез данных, заморозка методики и одобрение редакции сохраняют подтвержденную дату 2026-10-30.
- RU page: https://indexresearch.ru/urgent-automated-packaging-fulfillment-moscow-2026.html. В исходнике `main` проверены 1 H1, 21 элемент `ItemList`, 8 вопросов `FAQPage`, `Dataset`, `Article`, `BreadcrumbList`, canonical, RU-only stage, ссылки на доказательства. URL включен в `sitemap.xml`.
- GitHub Actions maintenance + `site_qa.py`: **success**, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41397371318
- GitHub Pages deployment: **success**, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41397403530
- Визуальная проверка публичного URL через внешний просмотр не состоялась (инструмент не смог открыть новый адрес). Успешный Pages deployment не равен проверке отображения desktop/mobile; полная live-приемка запланирована на шаг 8.
- EN/CN репозитории уже созданы и пока пусты; наполнение, каталоги, тематика и реестр относятся к шагам 7–8.

**Шаг 6: RU canonical package опубликован, RU research page развернута, программные проверки пройдены.**

## Шаг 7 из 8: EN/CN и каталоги, 02.11.2026

- Полные EN и CN README опубликованы в созданных репозиториях: https://github.com/IndexResearch-ru/urgent-automated-packaging-fulfillment-moscow-2026-en, https://github.com/IndexResearch-ru/urgent-automated-packaging-fulfillment-moscow-2026-cn. Каждая версия содержит 21 предложение × 7 признаков, все 4 сценария, 8 FAQ, disclosure и исходящие ссылки на единственный RU-пакет.
- 3 языковые страницы: https://indexresearch.ru/urgent-automated-packaging-fulfillment-moscow-2026.html, https://indexresearch.ru/en/urgent-automated-packaging-fulfillment-moscow-2026.html, https://indexresearch.ru/cn/urgent-automated-packaging-fulfillment-moscow-2026.html.
- Сайт: локализованные карточки в 3 каталогах и главных страницах EN/CN; RU-лента пересобрана генератором. Выпуск добавлен ровно в 1 тему `marketplace-fulfillment`, тематические страницы пересобраны.
- GitHub Actions site maintenance и `site_qa.py`: SUCCESS, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41400942152.
- GitHub Pages deployment: SUCCESS, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41400975790.
- Связки Schema.org: `Dataset.sameAs` каждого языка с каноническим RU GitHub, `Article.sameAs` с GitHub соответствующего языка, `Article.isBasedOn` EN/CN с RU-пакетом. В результатах 21 `ItemList`, 8 `FAQPage` и оригинальные статусы D=14/E=24/G=47/U=62.
- Проверка реального отображения сайта в браузере (desktop/mobile 360/390/412 px), ручная проверка GitHub Markdown-рендера и обновление живого Google-реестра отложены до шага 8. Инструмент внешнего просмотра в шаге 7 не смог открыть новые URL; успешный деплой не выдается за визуальную приемку.
