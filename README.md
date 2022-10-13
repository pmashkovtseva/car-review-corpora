## car-review corpora
Здесь хранятся файлы проекта текстового корпуса обзоров на автомобили. Тексты взяты из сообщества <b><a href="https://vk.com/poyasni_za_tachku">"Поясни за тачку"</a></b>.
<br>
<br>
В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/primary_data.csv">primary_data.csv</a> находятся первичные данные, собранные с помощью <a href = "https://popsters.ru/">Popsters</a>.
<br>
В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/primary_data_processing.ipynb">primary_data_processing.ipynb</a> находится код токенизации, лемматизации (с помощью <a href="https://github.com/natasha/natasha">Natasha</a>), POS-разметки текстов и создания базы данных.
<br>
В файле <a href="https://https://github.com/pmashkovtseva/car-review-corpora/blob/main/tachka_database.db">tachka_database.db</a> находится собранная база данных.
<br>
В файле <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/searcher.py">searcher.py</a> реализован алгоритм поиска токенов по базе данных.
<br>
Файл <a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/main.py">main.py</a> и папка <a href="https://github.com/pmashkovtseva/car-review-corpora/tree/main/templates">templates</a> отвечают за реализацию Flask-приложения.
<br>
<br>
<br>
<b><a href="http://carrevcorp.pythonanywhere.com/">Ссылка на веб-приложение на PythonAnywhere</a></b>
<br>
<b><a href="https://github.com/pmashkovtseva/car-review-corpora/blob/main/car-review-slides.pdf">Ссылка на слайды с презентации</a></b>
<br>
<br>
### Исполнители проекта
Татьяна Перевощикова
<br>
Полина Черноморченко
<br>
Полина Машковцева
<br>
<br>
ФиКЛ НИУ ВШЭ, БКЛ-192
