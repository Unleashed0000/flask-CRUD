# flask-CRUD

### How to run through docker-compose.yaml:
In cmd or powershell:<br>
<pre> docker-compose up --build </pre> <br>

Against unused images in docker. <br>
<code> docker-compose up --build --force-recreate </code> <br>

Config options. <br>
<code>
environment:<br>
    - CONFIG=development # 'default', 'development', 'testing', 'production'
</code>
