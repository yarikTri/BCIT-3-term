def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        arg = args[0]
        return [ dict[arg] for dict in items if arg in dict and dict[arg] != None]
    else:
        res = [{ arg:dict[arg] for arg in args if arg in dict and dict[arg] != None} 
                for dict in items ]
        return list(filter(lambda dict: len(dict) != 0, res))

if __name__ == "__main__":
    goods = [
    {'title': 'Carpet', 'price': 2000, 'color': 'green'},
    {'title': 'Sofa for rest', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, 'title', 'price'))
    print(field(goods, 'title'))
