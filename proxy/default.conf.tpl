server {
    listen 80;
    server_name ezma.uz www.ezma.uz 206.189.61.81;

    location /static/ {
        alias /vol/web/static/;
    }

    location /media/ {
        alias /vol/web/media/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass app:9000;
    }
}