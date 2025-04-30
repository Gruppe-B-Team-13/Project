from datetime import date, datetime
import sqlite3

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, lambda d: d.isoformat())

## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", lambda s: datetime.strptime(s.decode(), "%Y-%m-%d").date())