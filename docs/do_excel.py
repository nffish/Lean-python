#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

# worksheet.write('A1', 'Hello world')

expenses = (
    ['rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)

row = 0
col = 0

for item, cost in expenses:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
