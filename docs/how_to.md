How to localy run project
-

##### Ubuntu:
* Install postgres `https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru`
* Install redis: `https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04`
* Install python requirements:
`pip3 install -r bms/requirements.txt`
* Install npm
`apt install npm`
* Install js requirements:
`cd jeth && npm install`
* Install migrations
`python3 bms/manage.py migrate --setings=bms.settingsdebug`
* Run django app:
`python3 bms/manage.py runserver 8000 --setings=bms.settingsdebug`
* Run node app:
`node jeth/main.js`

##### MacOS:

* Install redis: `brew install redis`.
* Makes the redis start with the start of computer: `ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents`
* Start Redis server via “launchctl”: `launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist`.
* Start Redis server using configuration file: `redis-server /usr/local/etc/redis.conf`.
* Stop Redis on autostart on computer start: `launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist`
* Location of Redis configuration file: `/usr/local/etc/redis.conf`
* Uninstall Redis and its files: `brew uninstall redis; rm ~/Library/LaunchAgents/homebrew.mxcl.redis.plist`
* Get Redis package information: `brew info redis`
* Test if Redis server is running: `redis-cli ping`
