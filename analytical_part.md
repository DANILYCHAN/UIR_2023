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

#### P.S. Все привиденные выше инструменты аннотирования являются Open Source решениями

#### Source: https://habr.com/ru/post/665684/

### Emotion Miner

Emotion Miner - приложение для онлайн аннотирования аудио-видео файлов, специализирующееся на разметке файлов по эмоциональной составляющей людей, представленных в записях. В настоящее время проект закрыт.

Вот что писал о функционале один из разработчиков Emotion Miner:
"Что позволяет делать сайт в нынешнем состоянии:
1. Размещать аудио-видео файлы, предварительно извлеченные из любого доступного контента (ток-шоу, дебаты, монологи, интервью, публичные выступления, презентации и т.д.), отсортированные, нарезанные и разбитые на короткие сцены (хронометраж — до 5 сек – может меняться) штатными профессиональными аннотаторами, либо «подцеплять» более длительные оригинальные записи из сторонних каналов и источников, конечно с учетом юридически обязывающих моментов и прав владельцев контента;
2. Осуществлять множественную разметку (multiple annotation) упомянутых видеофрагментов руками сотен и тысяч сторонних аннотаторов, каждому из которых, как правило, не только интересно принять участие в инициативе такого рода с финансовой точки зрения (участие оплачивается), но и хочется «прокачать» свои изначальные навыки по распознаванию эмоций."

#### Source: https://habr.com/ru/company/neurodatalab/blog/346952/
#### Пример аннотирования: https://www.youtube.com/watch?v=x8aNglOJsyw&ab_channel=EmotionMiner

## Анализ подходов к аннотированию медиафайлов - сбору и разметку данных

### Сбор данных

Существует несколько подходов к сбору данных:

1. Ручной сбор данных.
Ручной сбор данных людьми, например, проведение опросов, интервью или наблюдений. Этот подход полезен, когда данных мало, но при этом они должны быть очень точными и последовательными.

2. Web Scraping.
Подход, который включает в себя извлечение данных с веб-сайтов и веб-страниц. Web Scraping полезен, когда необходимо собрать большие объемы данных, а ручной сбор невозможен.

3. Датчики и устройства IoT (устройства Интернета вещей).
Датчики и устройства IoT можно использовать для сбора данных в режиме реального времени. Этот подход полезен для сбора данных из физических сред или систем, таких как датчики температуры на заводе.

4. Мониторинг социальных сетей.
Платформы социальных сетей предоставляют множество данных, которые можно собирать и анализировать. Этот подход полезен для понимая поведения потребителей, анализа настроений и анализа социальных сетей.

5. Краудсорсинг.
Краудсорсинг предполагает аутсорсинг сбора данных большой группе людей, как правило, через онлайн-платформы. Этот подход полезен, когда данные уже доступны и нет необходимости в дополнительном сборе данных.

В целом выбор подхода к сбору данных зависит от конкретной задачи и типа необходимых данных. Важно убедиться, что данные репрезентативны, точны и актуальны для конкретного приложения.

### Разметка данных

Аннотирование данных — это процесс добавления метаданных, меток или тегов к необработанным данным, чтобы сделать их более понятными и полезными для приложений машинного обучения. Существует несколько подходов к аннотации данных, в том числе:

1. Ручная аннотация.
В этом подходе люди вручную маркируют данные. Например, в задачах распознавания изображений люди могут аннотировать изображения, рисуя ограничивающие рамки вокруг интересующих объектов. Этот подход требует много времени и средств, но позволяет получать высококачественные размеченные данные.

2. Полууправляемая аннотация.
Этот подход сочетает ручную аннотацию с автоматической аннотацией с использованием таких алгоритмов, как активное обучение или кластеризация. Аннотатор-человек помечает небольшую часть данных, а алгоритм учится на помеченных данных и автоматически помечает оставшиеся данные. Этот подход требует меньше времени и средств, чем ручное аннотирование, и в то же время дает высококачественные размеченные данные.

3. Аннотация толпы.
Аннотация толпы включает в себя передачу задачи маркировки большой группе людей, обычно через онлайн-платформы. Этот подход экономичен и быстр, но качество размеченных данных может варьироваться в зависимости от опыта аннотатора.

4. Трансферное обучение.
Трансферное обучение — это подход, который использует уже существующие помеченные данные для аннотирования новых данных. Например, предварительно обученную модель на большом наборе данных можно точно настроить на меньшем наборе данных для конкретной задачи. Этот подход полезен, когда данные, доступные для аннотации, ограничены.

5. Активное обучение.
Активное обучение — это подход, который включает в себя выбор наиболее информативных точек данных для аннотации для повышения производительности модели. Модель обучается на небольшом размеченном наборе данных, а затем алгоритм выбирает наиболее информативные точки данных, которые будут помечены людьми. Этот подход полезен, когда стоимость ручной аннотации высока.

Выбор подхода к аннотации данных зависит от конкретного приложения машинного обучения, типа данных и доступных ресурсов. Важно убедиться, что размеченные данные являются точными, репрезентативными и актуальными для конкретного приложения.

## Изучение характера эмоциональных данных

Конечная цель аннотирования эмоций в медиафайлах - понимание, какие эмоции проявляют люди в конкретных ситуациях. Для этого используются различные модели эмоций, которые могут помочь описать и классифицировать эмоции. 

Одной из наиболее известных моделей является семимерное пространство эмоций по Полу Экману. В этой модели предлагается, что все эмоции можно разделить на семь базовых категорий: радость, грусть, страх, отвращение, ярость, удивление и безразличие. Эти эмоции были выведены на основе исследований, проведенных Экманом в разных культурах, и считаются универсальными для всех людей. 

Трехмерное пространство эмоций, предложенное Джеймсом Расселом и Альбертом Мертоном, описывает эмоции в терминах трех основных измерений: valence (валентность), arousal (активация) и dominance (доминирование). Валентность отражает ощущение приятности или неприятности, которое вызывает определенная эмоция. Arousal отражает степень физиологической активации, связанной с эмоцией: от низкой (расслабленности) до высокой (возбуждения). Dominance отражает степень контроля над ситуацией: от низкой (чувство бессилия) до высокой (чувство контроля).

Таким образом, при аннотировании медиафайлов с эмоциями людей можно использовать как семимерное пространство эмоций, так и трехмерное пространство эмоций, а также комбинировать их для получения более точной оценки эмоций. Важно также помнить, что эмоции очень индивидуальны, и их восприятие может различаться в зависимости от культурных и личностных особенностей.

## Обоснование поставноки задачи

Цель данной исследовательской работы - разработать веб-приложение для аннотирования медиафайлов с эмоциями людей. Приложение должно позволять пользователям аннотировать эмоции в видео- и аудиофайлах, прикреплять к ним соответствующие метки и комментарии.

Для достижения этой цели необходимо решить следующие задачи:

1. Изучение существующих методов аннотирования эмоций в медиафайлах, включая используемые пространства эмоций и способы оценки эмоций людьми.

2. Разработка веб-приложения для аннотирования медиафайлов с эмоциями людей. Приложение должно позволять пользователям загружать медиафайлы, просматривать их и оценивать эмоции на основе выбранного пространства эмоций.

3. Организация процесса разметки данных. Для этого могут использоваться различные методы, такие как crowdsourcing или приглашение экспертов в области психологии эмоций.

4. Тестирование и оценка качества разработанного приложения с помощью эксперимента, в котором участвуют пользователи. Для этого могут использоваться различные метрики, такие как точность аннотации эмоций, время, затраченное на процесс аннотирования, и удобство использования приложения.

5. Анализ результатов эксперимента и обсуждение возможных путей улучшения разработанного приложения.

# Теоретическая часть

## Концептуальное моделирование предметной области онлайн-аннотирования медиафайлов

