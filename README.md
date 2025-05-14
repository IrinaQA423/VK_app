
# Cокращение ссылок и статистика по ним

Эта программа сокращает ссылки при помощи приложения `VK` и выдает статистику по сокращенным ссылкам.

## Что необходимо для  запуска? 

1. Установить на компьютер `Python3`.

2. Установить зависимости при  помощи `pip` (или `pip3`, есть конфликт с `Python2`)

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_4.png?raw=true)


### Как получить  токен?

1. [Создайте приложение в VK](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application#Sozdanie-prilozheniya).

2. Укажите в настройках приложения:

    * Тип приложения - `Web`

    * Базовый домен - `example.com`

    * Доверенный Redirect URL - `https://example.com`

3. [Получите сервисный токен приложения (скрин для примера)](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_5.png?raw=true)

### Где  хранить токен?

Токен - это "цифровой  ключ" для  безопасного доступа к сервисам. Он является конфиденциальной информацией, поэтому хранить его в коде опасно.
 
В корне проекта создайте файл `.env` и поместите в него токен. 

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_10.png?raw=true)

## Как запустить  программу?

Для работы со ссылкой ее необходимо ввести в терминал. После чего программа проверит, была ли эта ссылка сокращена через приложение в `VK`.

Если ссылка не была сокращена, то программа сокращает ее через это приложение и выдает результат.

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_3.png?raw=true)

Если же ссылка уже является сокращенной, то программа выдает статистику переходов по этой ссылке.

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_6.png?raw=true)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
