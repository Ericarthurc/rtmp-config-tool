from datetime import datetime


def conf(youtube, facebook):
    data = rf"""
    # GENERATED: {datetime.now()}
    worker_processes  1;
    events {{
        worker_connections  1024;
    }}
    http {{
        include       mime.types;
        default_type  application/octet-stream;
        sendfile        on;
        keepalive_timeout  65;
        server {{
            listen       444 ssl;
            server_name  wildwoodcalvarylive.com;

            ssl_certificate      /ssl/cert.pem;
            ssl_certificate_key  /ssl/privkey.pem;

            ssl_session_cache    shared:SSL:1m;
            ssl_session_timeout  5m;

            ssl_ciphers  HIGH:!aNULL:!MD5;
            ssl_prefer_server_ciphers  on;
        location /live {{
            types {{
                application/x-mpegURL m3u8;
                    application/dash+xml mpd;
                    video/MP2T ts;
                    video/mp4 mp4;
        }}
            alias /dash/live;
            add_header Cache-Control no-cache;
                add_header Cache-Control no-cache;
            add_header 'Access-Control-Allow-Origin' '*';
        }}
        location /stat {{
            rtmp_stat all;
                rtmp_stat_stylesheet stat.xsl;
        }}
        location /stat.xsl {{
            root /usr/local/nginx/html;
        }}
        location / {{
                root   html;
                index  index.html index.htm;
            add_header Cache-Control no-cache;
                add_header Cache-Control no-cache;
            add_header 'Access-Control-Allow-Origin' '*';
        }}
        }}
    }}
    rtmp {{
        server {{
            listen 1935;
            chunk_size 4096;
            application live {{
                live on;
                record off;
                allow publish all;
                allow play all;
                # RTMP REALY: format [push [rtmp server address]/[stream key];
                # Deafult Youtube RTMP
                # push rtmp://a.rtmp.youtube.com/live2/390s-967e-wdsb-b1hv;
                push rtmp://a.rtmp.youtube.com/live2/{youtube};
                # Deafult Facebook RTMP
                # push rtmp://live-api-s.facebook.com:80/rtmp/2619710981388821?s_bl=1&s_ps=1&s_sw=0&s_vt=api-s&a=AbyYLVq7uYfxzqfM;
                push rtmp://127.0.0.1:19350/rtmp/{facebook};
                # DASH configuration: web player
                dash on;
                dash_path /dash/live;
                    dash_fragment 5;
                        dash_playlist_length 30;
            }}
        }}
    }}
    """
    return data
