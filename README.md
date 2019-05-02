### Программа для проверки эффективности рекламы в социальной сети «ВКонтакте».

#### Описание:

Программа использует API VK для анализа количества упоминаний рекламируемой продукции и API Plot для построения графиков.

#### Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 

```
pip3 install -r requirements.txt
```

#### Запуск программы:

##### Перед первым запуском необходимо выполнить ряд обязательных условий :

1) Получить "Сервисный ключ доступа" VK

Для этого необходимо перейти по ссылке :

```
https://vk.com/dev
```
затем создать приложение в разделе "Мои приложения" Ссылка на него находится в шапке сайта(В качестве типа приложения укажите <b>standalone</b>) После создания приложения необходимо зайти в меню приложения "Настройки" и скопировав Сервисный ключ доступа присвоить его значение константе VK_TOKEN модуля settings.py

```
VK_TOKEN='Сервисный ключ доступа'
```
2) Получить Username и API KEY plot.ly

Для этого необходимо зарегистрироваться на сайте:

```
https://plot.ly

```
После регистрации перейти в разделе "Settings" в подраздел API Keys скопировав Username и API key(предварительно необходимо сгенерировать новый ключ кликнув Regenerate Key)  и присвоить значения константам ,соответственно ,PLOTLY_USERNAME и PLOTLY_TOKEN модуля settings.py

```
PLOTLY_USERNAME='You Username'
PLOTLY_TOKEN='API KEY'
```
Так же необходимо в модуле settings.py  указать период мониторинга (дней)  константе : SEARCH_INTERVAL
```
SEARCH_INTERVAL=7
```
Передать желаемый поисковый запрос константе :SEARCH_NAME
(допустимо использовать русские символы)
```
SEARCH_NAME='Coca-Cola'

```
После запуска программы к окне терминала отобразится ссылка на график.

```
$python3 main.py
https://plot.ly/~Dark_Dmake/16
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


##### Dark_Dmake
2019