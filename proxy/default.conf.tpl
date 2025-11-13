server {
    listen 80;
    server_name ezma.uz www.ezma.uz 164.90.186.197;

    location /static/ {
        alias /vol/web/static/;
    }

    location /media/ {
        alias /vol/web/media/;
    }

    location /health/ {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}