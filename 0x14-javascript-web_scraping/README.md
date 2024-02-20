# 0x14-javascript-web_scraping

## Resources
- [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
- [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
- [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)
- [Rules of Standard](https://intranet.alxswe.com/rltoken/W9rASrTqkF-xXjcwomrMLw)
- [Semicolons on top](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)
- [AirBnB style](https://intranet.alxswe.com/rltoken/NZR55f9vk1dZXj5q7UI5mQ)

## Learning Objectives
### Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

### Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)

$ sudo npm install semistandard --global

### Install request module and use it
[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)

$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).