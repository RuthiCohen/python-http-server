import os

nginx_src = '/opt/homebrew/etc/nginx/nginx.conf'

#update Nginx configuration
with open(nginx_src, 'r+') as f:
    config = f.read()
    f.seek(0)
    f.truncate()
    f.write(config.replace(
        'server {',
        'server {\n\n    location / {\n        proxy_pass http://localhost:8000;\n        proxy_set_header Host $host;\n        proxy_set_header X-Real-IP $remote_addr;\n    }'
    ))

# restart Nginx
os.system('sudo launchctl stop homebrew.mxcl.nginx')
os.system('sudo launchctl start homebrew.mxcl.nginx')