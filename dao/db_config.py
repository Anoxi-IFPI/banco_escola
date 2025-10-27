import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_zuEkb7vg6WHq@ep-wispy-voice-acoq5mgs-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)