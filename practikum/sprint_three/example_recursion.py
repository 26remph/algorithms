def countDown(start, indent=1, prefix="zero"):
    print("-" * indent, "UP:", start, prefix)
    if start == 0:
        # Здесь рекурсивный вызов 'countDown' прекратился, сначала
        #  печатается эта строчка, потом все, что было накоплено в стеке...
        print("-" * indent, "DOWN:", start, prefix)
    else:
        # Рекурсивный вызов 'countDown'
        countDown(start - 1, indent + 1, prefix="first")
        # Вызов 'countDown' не дает функции print выполнится
        countDown(start - 1, indent + 1, prefix="second")
        # и накапливает (откладывает) ее исполнение в стеке
        print("-" * indent, "END:", start, prefix)


countDown(3)
