


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
 
    PMerge.clear()
    i = 0
    j = 0
    len_left = len(PLeft)
    len_right = len(PRight)

    while i < len_left and j < len_right:
        if PAsc:
            # ascending
            if PLeft[i] <= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
        else:
            # descending
            if PLeft[i] >= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1

    # jäljellä olevat
    while i < len_left:
        PMerge.append(PLeft[i])
        i += 1

    while j < len_right:
        PMerge.append(PRight[j])
        j += 1

    return None


def _mergeSort_internal(PValues: list[int], PAsc: bool) -> list[int]:
 
    if len(PValues) <= 1:
        return PValues[:]  

    mid = len(PValues) // 2
    left_part = _mergeSort_internal(PValues[:mid], PAsc)
    right_part = _mergeSort_internal(PValues[mid:], PAsc)

    merged: list[int] = []
    merge(left_part, right_part, merged, PAsc)
    return merged


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:

    sorted_values = _mergeSort_internal(PValues, PAsc)
    # kirjoitetaan takaisin samaan listaan
    PValues[:] = sorted_values
    return None


def readValues(PFilename: str) -> list[int]:

    values: list[int] = []
    with open(PFilename, "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content:
            
            normalized = content.replace(",", " ")
            parts = normalized.split()
            for p in parts:
                values.append(int(p))
    return values


def displayValues(PLabel: str, PFilename: str, PValues: list[int]) -> None:

    values_str = ", ".join(str(v) for v in PValues)
    print(f"{PLabel} '{PFilename}' -> {values_str}")
