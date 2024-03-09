truth_evaluation_rules = {'∨' : {True : {'left' : True, 'operation' : 'or', 'right' : True, 'levels' : 1},
                                 False : {'left' : False, 'operation' : 'and', 'right' : False, 'levels' : 2}},
                          '∧' : {True : {'left' : True, 'operation' : 'and', 'right' : True, 'levels' : 2},
                                 False : {'left' : False, 'operation' : 'or', 'right' : False, 'levels' : 1}},
                          '→' : {True : {'left' : False, 'operation' : 'or', 'right' : True, 'levels' : 1},
                                 False : {'left' : True, 'operation' : 'and', 'right' : False, 'levels' : 2}},
                          '¬' : {True : {'right' : False, 'levels' : 1},
                                 False : {'right' : True, 'levels' : 1}}
                        }

def count_tree_levels():
    pass