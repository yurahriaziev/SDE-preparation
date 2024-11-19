def main(products, searchedWord):
    products.sort()
    left, right = 0, len(products)-1 
    results = []

    for i in range(len(searchedWord)):
        search = searchedWord[i]
        while left <= right and (len(products[left]) <= i or products[left][i] != search):
            left += 1
        while left <= right and (len(products[right]) <= i or products[right][i] != search):
            right -= 1
        
        words_left = right - left + 1
        if words_left >= 3:
            results.append([products[left], products[left+1], products[left+2]])
        elif words_left == 2:
            results.append([products[left], products[left+1]])
        elif words_left == 1:
            results.append([products[left]])
        else:
            results.append([])

        return results


print(main(['mouse', 'mousepad', 'moneypad', 'money'], 'mouse'))
