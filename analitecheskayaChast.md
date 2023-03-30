# Аналитическая часть 

## Изучение и сравнительный анализ инструментов аннотирования медиафайлов

1. Label Studio

Она поддерживает широкий ассортимент видов аннотирования, в том числе классификацию изображений, распознавание объектов и семантическую сегментацию. Она работает практически со всеми типами данных (аудио, изображения, текст и HTML), а также имеет уникальную конфигурацию под названием Labeling Config, в которой пользователь может проектировать собственный UI. У инструмента есть множество управляемых алгоритмами функций автоматизации, в том числе опция предварительной разметки, которая может самостоятельно размечать данные на основе имеющейся модели машинного обучения.

2. Diffgram

На фоне остальных инструментов его выделяет то, что наряду с платформой аннотации он также имеет различные функции управления массивами данных и рабочими процессами. Он поддерживает практически все виды пространственного аннотирования на изображениях и в видео, в том числе ограничивающие прямоугольники, кубоиды и ключевые точки. Функция семантической сегментации имеет различные инструменты, например, автоматическое определение границ, комбинирование форм и преобразование точек в многоугольники. Кроме того, функция аннотирования видео поддерживает интерполяцию и разметку последовательностей, например, отслеживание событий и объектов.

3. CVAT

ПО, разработанное компанией Intel. Хотя его UI не самый понятный, оно очень мощное, обладает современными функциями и работает в Chrome.

CVAT обеспечивает распознавание объектов, классификацию и сегментацию изображений, аннотирование прямоугольниками, многоугольниками, линиями и ключевыми точками. CVAT даже имеет различные функции автоматизации, например, копирование и перенос объектов, отслеживание, интерполяция и автоматическое аннотирование объектов, реализованные на основе TensorFlow OD API. Благодаря этому инструменту легко организовать совместную работу, позволяющую разделять и делегировать задания.

4. ImageTagger

Эта платформа разработана Никласом Фидлером с кафедры информатики Гамбургского университета специально для Robot World Cup и спроектирована таким образом, чтобы сама процедура разметки была как можно более интуитивной и быстрой.

Она позволяет размечать массивы изображений ограничивающими прямоугольниками, многоугольниками, линиями и ключевыми точками. У неё есть опции управления проектами и функции помощи в QA, например, предварительная загрузка изображений, загрузка существующих меток и проверка меток. Кроме того, в ней сделан упор на совместную работу и она обеспечивает возможность крупномасштабной совместной работы с разметкой массивов изображений благодаря разделению разметчиков на команды.

### P.S. Все привиденные выше инструменты аннотирования являются Open Source решениями

### Source: https://habr.com/ru/post/665684/

## Emotion Miner

Emotion Miner - приложение для онлайн аннотирования аудио-видео файлов, специализирующееся на разметке файлов по эмоциональной составляющей людей, представленных в записях. В настоящее время проект закрыт.

Вот что писал о функционале один из разработчиков Emotion Miner:
"Что позволяет делать сайт в нынешнем состоянии:
1. Размещать аудио-видео файлы, предварительно извлеченные из любого доступного контента (ток-шоу, дебаты, монологи, интервью, публичные выступления, презентации и т.д.), отсортированные, нарезанные и разбитые на короткие сцены (хронометраж — до 5 сек – может меняться) штатными профессиональными аннотаторами, либо «подцеплять» более длительные оригинальные записи из сторонних каналов и источников, конечно с учетом юридически обязывающих моментов и прав владельцев контента;
2. Осуществлять множественную разметку (multiple annotation) упомянутых видеофрагментов руками сотен и тысяч сторонних аннотаторов, каждому из которых, как правило, не только интересно принять участие в инициативе такого рода с финансовой точки зрения (участие оплачивается), но и хочется «прокачать» свои изначальные навыки по распознаванию эмоций."

### Source: https://habr.com/ru/company/neurodatalab/blog/346952/
### Пример аннотирования: https://www.youtube.com/watch?v=x8aNglOJsyw&ab_channel=EmotionMiner