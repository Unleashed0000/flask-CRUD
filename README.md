# flask-CRUD

### How to run through docker-compose.yaml:
In cmd or powershell:<br>
<code> docker-compose up --build </code> <br>

Against unused images in docker. <br>
<code> docker-compose up --build --force-recreate </code> <br>

Config options. <br>
<pre>
environment:
    - CONFIG=development # 'default', 'development', 'testing', 'production'
</pre>
