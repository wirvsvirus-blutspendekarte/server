import psycopg2
import psycopg2.extras


def get_connection():
    return psycopg2.connect(
        "host='blutspendekarte.de' "
        "dbname='blutspendekarte' "
        "user='blutspendekarte' "
        "password='IchBin1Alpaka'"
    )