#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="response1" psql -h "$host" -d "response" -U "db_user" -c '\q'; do sleep 1; done

>&2 echo "Postgres is up - executing command"
exec $cmd