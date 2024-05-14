#!/bin/bash

/usr/bin/mongod --fork --logpath /var/log/mongodb.log --bind_ip_all

echo "Waiting for MongoDB to start..."
until mongosh --eval 'print("Waiting for connection")'
do
    sleep 1
done

mongosh <<EOF
use challenge
db.createCollection("users")
db.users.insertOne({username: 'admin', password: '23a52f2902720d27c64bd1a6f797cd65'})
quit()
EOF

/usr/bin/python3 /app/app.py
