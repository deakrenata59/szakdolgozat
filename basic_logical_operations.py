"""Operátorok sorrendje legerősebbtől a leggyengébbig."""
operator_sequence = ("¬", "∧", "∨", "→")
# TODO: implikációnál figyelni, hogy ott jobbról bontunk mindig!!

def convert_to_boolean(value):
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    raise ValueError

def delete_empty_str(list):
    new_list = []
    for i in range(len(list)):
        if list[i] != "":
            new_list.append(list[i])
    return new_list

def map_boolean(input, operator):
    input = delete_empty_str(input.split(operator))
    input = list(map(lambda x: x.strip(), input))
    input = list(map(lambda x:  convert_to_boolean(x), input))
    return input

def define_operation(input):
    """Kap egy egyszerű logikai kifejezést, melyben 2 vagy egy ítéletváltozó van,
    és egy logikai művetet, majd a művelet alapján eldönti, hogy melyik
    kiértékelő függvényt kell használni."""
    #TODO: zárójelek érzékelésének implementálása, szükség esetén zárójelez
    #TODO: ha elsőrendű logikai jeleket érzékel, (pl. minden vagy létezik), akkor arra hibát dobjon
    if "∧" in input:
        return eval_and(map_boolean(input, "∧"))
    elif "∨" in input:
        return eval_or(map_boolean(input, "∨"))
    elif "¬" in input:
        return eval_neg(map_boolean(input, "¬"))
    elif "→" in input:
        return eval_implication(map_boolean(input, "→"))
    


def eval_and(input):
    return input[0] and input[1]

def eval_or(input):
    return input[0] or input[1]

def eval_neg(input):
    return not input[0]

def eval_implication(input):
    if (input[0] is True) and (input[1] is False):
        return False
    return True

#TODO: a logikai műveletjel pozíciójának ellenőrzése, pl. A¬ helytelen, AB    V helytelen, ∧A   B is stb...
#TODO: extra karakterek felismerése... pl. több V vagy hiányzik stb