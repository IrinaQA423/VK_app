# Cокращение ссылок и статистика по ним

Эта программа сокращает ссылки при помощи приложения `VK` и выдает статистику по сокращенным ссылкам.

Для работы со ссылкой ее необходимо ввести в терминал.После чего программа проверит, была ли эта ссылка сокращена через приложение в `VK`.

Если ссылка не была сокращена, то программа сокращает ее через это приложение и выдает результат.

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_3.png?raw=true)

Если же ссылка уже является сокращенной, то программа выдает статистику переходов по этой ссылке.

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_6.png?raw=true)

### Что необходимо для запуска программы?

1. Установите на компьютер `Python3`.

2. Используйте `pip` (или `pip3`, есть конфликт с `Python2`) для установки зависимостей:

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_4.png?raw=true)

3. [Создайте приложение в VK](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application#Sozdanie-prilozheniya).

4. [Получите сервисный токен приложения (скрин для примера)](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_5.png?raw=true)

5. Укажите в настройках приложения:

* Тип приложения - Web

* Базовый домен - example.com

* Доверенный Redirect URL - https://example.com

6. Токен поместите в файл .env в корневой папке проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).