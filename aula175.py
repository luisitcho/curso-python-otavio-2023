# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

# from pytz import timezone

# data = datetime.now(timezone('America/Sao_Paulo'))


# data_str_data = '12/09/2024 19:09:23'
# data_str_fmt = '%d/%m/%Y %H:%M:%S'

# data_str_data = '12/09/2024'
# data_str_fmt = '%d/%m/%Y %H:%M:%S'

# data = datetime(2024, 12, 9, 19, 9, 23, tzinfo=timezone('America/Sao_Paulo'))
# data = datetime.strptime(data_str_data, data_str_fmt)

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1733785398.39969))
