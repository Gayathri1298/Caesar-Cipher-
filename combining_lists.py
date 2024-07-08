
def merge_elements(elements1, elements2):
    def is_more_than_half_contained(pos1, pos2):
        length1 = pos1[1] - pos1[0]
        length2 = pos2[1] - pos2[0]
        
        
        if pos2[0] >= pos1[0] and pos2[1] <= pos1[1]:
            return (pos2[1] - pos2[0]) > length1 / 2
        elif pos1[0] >= pos2[0] and pos1[1] <= pos2[1]:
            return (pos1[1] - pos1[0]) > length2 / 2
        return False
    
   
    combined_list = elements1 + elements2
    combined_list.sort(key=lambda x: x["positions"][0])
    
    merged_list = []
    skip_indices = set()
    
    for i in range(len(combined_list)):
        if i in skip_indices:
            continue
        
        current_element = combined_list[i]
        current_pos = current_element["positions"]
        current_values = current_element["values"]
        
        for j in range(i + 1, len(combined_list)):
            if j in skip_indices:
                continue
            
            next_element = combined_list[j]
            next_pos = next_element["positions"]
            next_values = next_element["values"]
            
            if is_more_than_half_contained(current_pos, next_pos):
                current_values.extend(next_values)
                skip_indices.add(j)
        
        merged_list.append({
            "positions": current_pos,
            "values": current_values
        })
    
    return merged_list

# Example 
list1 = [
    {
        "positions": [1, 5],
        "values": [10, 20]
    },
    {
        "positions": [6, 10],
        "values": [30, 40]
    }
]

list2 = [
    {
        "positions": [3, 8],
        "values": [50, 60]
    },
    {
        "positions": [9, 12],
        "values": [70, 80]
    }
]

merged_list = merge_elements(list1, list2)
print(merged_list)