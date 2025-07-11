# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2025))
# print(calendar.month(2025, 12))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 12)

# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2025, 12, ultimo_dia)])

# Exemplo de uso do calendar para imprimir os dias do mês de Outubro de 2025
print("Dias do mês de Outubro de 2025:")
for week in calendar.monthcalendar(2025, 10):
    for day in week:
        if day == 0:
            continue
        print(day)