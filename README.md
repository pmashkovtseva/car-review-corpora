<h3>Car-review corpora</h3>

Здесь хранятся файлы проекта текстового корпуса обзора на автомобили. Тексты взяты из сообщества <b><a href="https://vk.com/poyasni_za_tachku">"Поясни за тачку"</a></b>

В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/primary_data.csv">primary_data.csv</a> находятся первичные данные, собранные с помощью <a href = "https://popsters.ru/">Popsters</a>.
<br>
В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/primary_data_processing.ipynb">primary_data_processing.ipynb</a> находится код токенизации, лемматизации (с помощью <a href="https://github.com/natasha/natasha">Natasha</a>) текста и создания базы данных.
<br>
В файле <a href="https://https://github.com/pmashkovtseva/car-review-corpora/blob/main/tachka_database.db">tachka_database.db</a> находится собранная база данных.
<br>
В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/searcher.py">searcher.py</a> реализован алгоритм поиска токенов по базе данных.
<br>
Файлы <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/main.py">main.py</a> и папка <a href="https://github.com/pmashkovtseva/car-review-corpora/tree/main/templates">templates</a> отвечают за реализацию Flask-приложения.
