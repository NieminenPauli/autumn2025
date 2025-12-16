


from typing import List


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    """
    Sort PValues inplace using bubble sort.
    PAsc = True  -> ascending
    PAsc = False -> descending
    """
    n = len(PValues)
    
    for i in range(n - 1):  
        swapped = False
 
        for j in range(0, n - i - 1):
            if PAsc:
                do_swap = PValues[j] > PValues[j + 1]
            else:
                do_swap = PValues[j] < PValues[j + 1]

            if do_swap:
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                swapped = True

        if not swapped:
            break
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
